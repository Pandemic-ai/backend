from django.urls import path, include
from . import views

# ListAPIView
urlpatterns = [
    path('coronavirus/volunteer/', views.Volunt.as_view()),
    path('coronavirus/report/', views.Report.as_view()),
]
