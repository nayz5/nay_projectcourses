from django.urls import path
from . import views

app_name = 'courseApp'

urlpatterns = [
    path('<int:course_id>/', views.details, name='details-page'),
    path('', views.courses, name='home-page'),
    path('<int:course_id>/yourchoice/', views.yourchoice, name='yourchoice'),
]
