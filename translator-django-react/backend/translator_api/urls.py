from django.urls import path

from . import views

urlpatterns = [
    path("languages/", views.languages_view, name="languages"),
    path("detect/", views.detect_view, name="detect"),
    path("translate/", views.translate_view, name="translate"),
    path("speak/", views.speak_view, name="speak"),
    path("upload/", views.upload_view, name="upload"),
]
