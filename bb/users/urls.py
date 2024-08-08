from django.urls import path

from .api import UserListApi

urlpatterns = [path("", UserListApi.as_view(), name="list")]
