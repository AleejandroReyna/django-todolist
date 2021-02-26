from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('create/', views.CreateTaskView.as_view(), name='create')
]
