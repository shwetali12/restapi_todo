from django.urls import path
from .views import *


urlpatterns = [
    path("<int:pk>", detail.as_view()),
    path('', listtodo.as_view()),
    path('create',create.as_view()),
    path('delete/<int:pk>', delete.as_view()),
]