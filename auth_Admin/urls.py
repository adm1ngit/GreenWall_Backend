from django.urls import path
from .views import UserSubmissionCreateView

urlpatterns = [
    path('submit/', UserSubmissionCreateView.as_view(), name='submit-user'),
]
