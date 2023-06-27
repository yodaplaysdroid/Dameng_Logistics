from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("mysql_input/", include("mysql_input.urls")),
    path("hdfs_input/", include("hdfs_input.urls")),
    path("minio_input/", include("minio_input.urls")),
]
