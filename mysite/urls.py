from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", include("polls.urls")),
    # http://127.0.0.1:8000
    path("polls/", include("polls.urls")),
    # http://127.0.0.1:8000/polls/

    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")), 
]
