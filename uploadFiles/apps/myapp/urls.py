from django.urls import path
from myapp import views
urlpatterns = [
    path("", views.index,name="index"),

    #file操作
    path("files", views.indexfiles, name="indexfiles"),
    path("download/<int:fileid>", views.download_file, name="downloadfile"),

    #upload
    path("upload", views.uploadPage, name="uploadpage"),
    path("doUpload", views.upload_file ,name="doupload"),
]
