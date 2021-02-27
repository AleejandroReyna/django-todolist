from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('<uuid:task_id>/', views.DetailTaskView.as_view(), name='task_detail'),
    path('create/', views.CreateTaskView.as_view(), name='task_create')
]
