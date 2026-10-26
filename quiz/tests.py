from rest_framework.test import APITestCase
from .models import Choice, Exam, Question


class QuizAPITests(APITestCase):
    def setUp(self):
        self.exam = Exam.objects.create(title='API exam')
        self.payload = {'exam': self.exam.pk, 'text': 'What is Django?', 'score': 2,
                        'choices': [{'text': 'Framework', 'is_correct': True},
                                    {'text': 'Database', 'is_correct': False}]}

    def test_nested_create_and_read_only_fields(self):
        response = self.client.post('/api/questions/', {**self.payload, 'id': 900}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertNotEqual(response.data['id'], 900)
        self.assertEqual(len(response.data['choices']), 2)
        self.assertEqual(response.data['exam'], self.exam.pk)

    def test_exactly_one_correct_choice(self):
        for flags in [[], [False, False], [True, True]]:
            payload = {**self.payload, 'choices': [
                {'text': 'Option', 'is_correct': flag} for flag in flags]}
            self.assertEqual(self.client.post('/api/questions/', payload, format='json').status_code, 400)
        self.assertEqual(Question.objects.count(), 0)

    def test_missing_and_incorrect_type(self):
        self.assertEqual(self.client.post('/api/exams/', {}, format='json').status_code, 400)
        self.assertEqual(self.client.post('/api/questions/', {**self.payload, 'score': 'abc'}, format='json').status_code, 400)

    def test_patch_preserves_choices_and_rejects_invalid_replacement(self):
        question = self.client.post('/api/questions/', self.payload, format='json').data
        url = f"/api/questions/{question['id']}/"
        self.assertEqual(self.client.patch(url, {'text': 'Updated'}, format='json').status_code, 200)
        response = self.client.patch(url, {'choices': [{'text': 'Invalid', 'is_correct': False}]}, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Choice.objects.count(), 2)

    def test_choice_mutations_preserve_invariant(self):
        question = self.client.post('/api/questions/', self.payload, format='json').data
        correct, wrong = question['choices']
        self.assertEqual(self.client.delete(f"/api/choices/{correct['id']}/").status_code, 400)
        self.assertEqual(self.client.patch(f"/api/choices/{wrong['id']}/", {'is_correct': True}, format='json').status_code, 400)
        self.assertEqual(self.client.post('/api/choices/', {'question': question['id'], 'text': 'Extra', 'is_correct': False}, format='json').status_code, 201)
        self.assertEqual(self.client.delete(f"/api/choices/{wrong['id']}/").status_code, 204)

    def test_filter_search_and_pagination(self):
        for number in range(7):
            self.client.post('/api/questions/', {**self.payload, 'text': f'Python item {number}'}, format='json')
        other = Exam.objects.create(title='Other')
        self.client.post('/api/questions/', {**self.payload, 'exam': other.pk, 'text': 'Other'}, format='json')
        response = self.client.get(f'/api/questions/?exam={self.exam.pk}&search=Python')
        self.assertEqual(response.data['count'], 7)
        self.assertEqual(len(response.data['results']), 5)
        self.assertIsNotNone(response.data['next'])
        self.assertEqual(len(self.client.get(f'/api/questions/?exam={self.exam.pk}&page=2').data['results']), 2)
        self.assertEqual(self.client.get('/api/questions/?exam=abc').status_code, 400)

    def test_exam_crud_and_cascade(self):
        response = self.client.post('/api/exams/', {'title': 'Temporary'}, format='json')
        url = f"/api/exams/{response.data['id']}/"
        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.client.get(url).status_code, 200)
        self.assertEqual(self.client.patch(url, {'description': 'Updated'}, format='json').status_code, 200)
        self.client.post('/api/questions/', {**self.payload, 'exam': response.data['id']}, format='json')
        self.assertEqual(self.client.delete(url).status_code, 204)
        self.assertEqual(self.client.get(url).status_code, 404)
        self.assertEqual(Question.objects.count(), 0)
