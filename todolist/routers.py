from tasks.api_views import TaskViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)

