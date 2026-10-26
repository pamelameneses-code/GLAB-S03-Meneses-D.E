from rest_framework.routers import DefaultRouter

from .api_views import ChoiceViewSet, ExamViewSet, QuestionViewSet

router = DefaultRouter()
router.register('exams', ExamViewSet)
router.register('questions', QuestionViewSet)
router.register('choices', ChoiceViewSet)
urlpatterns = router.urls
