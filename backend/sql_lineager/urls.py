from django.urls import path
from .views import FileUploadView, FileContentView

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('files/<int:file_id>/', FileContentView.as_view(), name='file-content')
]