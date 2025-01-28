from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UploadedFile
from .serializer import FileUploadSerializer
from django.http import JsonResponse

class FileUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class FileContentView(APIView):
    def get(self, request, file_id, *args, **kwargs):
        try:
            file_record = UploadedFile.objects.get(id=file_id)
            file_path = file_record.file.path
            
            data = {
                    "id": file_id,
                    "file_name": file_record.file.name,
                    "file_path": file_path,
                    "uploaded_at": file_record.uploaded_at
                }
            return JsonResponse(data, safe=False)
        except UploadedFile.DoesNotExist:
            return Response({"error": "File not found"}, status=404)
