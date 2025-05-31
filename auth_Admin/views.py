from rest_framework import generics
from .models import UserSubmission
from .serializers import UserSubmissionSerializer

class UserSubmissionCreateView(generics.CreateAPIView):
    queryset = UserSubmission.objects.all()
    serializer_class = UserSubmissionSerializer
