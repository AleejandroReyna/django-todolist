from django.core.exceptions import PermissionDenied


def check_owner(function):

    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        check_task = request.user.task_set.filter(id=kwargs['task_id'])
        if not check_task.exists():
            raise PermissionDenied
        return function(request, *args, **kwargs)

    return wrapper
