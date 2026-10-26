from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

from .models import Choice, Exam, Question
from .serializers import ChoiceSerializer, ExamSerializer, QuestionSerializer


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.order_by('id')
    serializer_class = ExamSerializer
    search_fields = ['title']


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.select_related('exam').prefetch_related('choices').order_by('id')
    serializer_class = QuestionSerializer
    search_fields = ['text']

    def get_queryset(self):
        queryset = super().get_queryset()
        exam = self.request.query_params.get('exam')
        if exam is not None:
            try:
                exam = int(exam)
            except (ValueError, TypeError):
                raise ValidationError({'exam': 'Enter an integer exam ID.'})
            queryset = queryset.filter(exam_id=exam)
        return queryset


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.select_related('question').order_by('id')
    serializer_class = ChoiceSerializer
    search_fields = ['text']

    def perform_destroy(self, instance):
        if instance.is_correct:
            raise ValidationError({'is_correct': 'Cannot delete the only correct choice. Replace choices through the question endpoint.'})
        instance.delete()
