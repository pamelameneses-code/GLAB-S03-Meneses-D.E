from django.db import transaction
from rest_framework import serializers

from .models import Choice, Exam, Question


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'title', 'description', 'created_at']
        read_only_fields = ['id', 'created_at']


class NestedChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'text', 'is_correct']
        read_only_fields = ['id']


class QuestionSerializer(serializers.ModelSerializer):
    choices = NestedChoiceSerializer(many=True, required=True)

    class Meta:
        model = Question
        fields = ['id', 'exam', 'text', 'score', 'choices']
        read_only_fields = ['id']

    def validate(self, attrs):
        choices = attrs.get('choices')
        if choices is None and self.instance:
            choices = list(self.instance.choices.values('is_correct'))
        if choices is not None and sum(c.get('is_correct', False) for c in choices) != 1:
            raise serializers.ValidationError({
                'choices': 'A question must have exactly one correct choice.'
            })
        return attrs

    @transaction.atomic
    def create(self, validated_data):
        choices = validated_data.pop('choices')
        question = Question.objects.create(**validated_data)
        for choice in choices:
            Choice.objects.create(question=question, **choice)
        return question

    @transaction.atomic
    def update(self, instance, validated_data):
        # Nested choices replace the complete list when supplied.
        choices = validated_data.pop('choices', None)
        instance = super().update(instance, validated_data)
        if choices is not None:
            instance.choices.all().delete()
            for choice in choices:
                Choice.objects.create(question=instance, **choice)
        return instance


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'question', 'text', 'is_correct']
        read_only_fields = ['id']

    def validate(self, attrs):
        question = attrs.get('question', getattr(self.instance, 'question', None))
        if self.instance and question.pk != self.instance.question_id:
            raise serializers.ValidationError({'question': 'Moving choices is not allowed.'})
        if question:
            others = question.choices.all()
            if self.instance:
                others = others.exclude(pk=self.instance.pk)
            correct = attrs.get('is_correct', getattr(self.instance, 'is_correct', False))
            if others.filter(is_correct=True).count() + int(correct) != 1:
                raise serializers.ValidationError({
                    'is_correct': 'A question must have exactly one correct choice. Use the question endpoint to replace choices together.'
                })
        return attrs
