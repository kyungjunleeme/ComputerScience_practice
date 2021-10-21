from django.urls import path
from . import views

app_name = "monitoring"  # URL Reverse에서 namespace역할을 하게 됨

urlpatterns = [
    path("async/", views.async_view, name="async_view"),
    path("sync/", views.sync_view, name="sync_view"),
    path("index/", views.index, name="index"),
]
