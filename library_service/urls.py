from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/library/", include("books.urls", namespace="books")),
    path("api/user/", include("users.urls", namespace="users")),
]
