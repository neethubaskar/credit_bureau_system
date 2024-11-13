from django.urls import path
from .views import QuestionPopupView, ResultsView

urlpatterns = [
    path('questions/', QuestionPopupView.as_view(), name='question_popup'),
    path('results/', ResultsView.as_view(), name='results'),
]
