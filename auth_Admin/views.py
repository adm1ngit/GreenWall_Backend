from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserSubmission
from .serializers import UserSubmissionSerializer
from rest_framework.permissions import AllowAny

class UserSubmissionCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Ma'lumot muvaffaqiyatli saqlandi!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
