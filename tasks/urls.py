from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('<uuid:task_id>/', views.DetailTaskView.as_view(), name='task_detail'),
    path('<uuid:task_id>/edit/', views.UpdateTaskView.as_view(), name='task_update'),
    path('<uuid:task_id>/delete/', views.DeleteTaskView.as_view(), name='task_delete'),
    path('create/', views.CreateTaskView.as_view(), name='task_create')
]
