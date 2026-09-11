from django.shortcuts import render, get_object_or_404
from .models import Exam


def exam_list(request):
    exams = Exam.objects.all()
    return render(request, "quiz/exam_list.html", {"exams": exams})


def exam_detail(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    return render(request, "quiz/exam_detail.html", {"exam": exam})