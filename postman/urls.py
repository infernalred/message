from django.urls import path

from postman.views import PostmanView

urlpatterns = [
    path("", PostmanView.as_view(), name="postman")
]
