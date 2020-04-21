from django.urls import path
from . import views  # ??


urlpatterns = [
    path('/', views.Image_Classifier.as_view(), name='predict'),
]
