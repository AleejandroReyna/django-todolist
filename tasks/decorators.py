from django.core.exceptions import PermissionDenied


def check_owner(function):

    def wrapper(request, *args, **kwargs):
        print(kwargs)
        if not request.user.is_authenticated:
            raise PermissionDenied
        if 'task_id' in kwargs:
            check_task = request.user.task_set.filter(id=kwargs['task_id'])
        elif 'pk' in kwargs:
            check_task = request.user.task_set.filter(id=kwargs['pk'])
        else:
            raise PermissionDenied
        if not check_task.exists():
            raise PermissionDenied
        return function(request, *args, **kwargs)

    return wrapper
