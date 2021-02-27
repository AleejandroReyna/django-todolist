from django.views.generic import DetailView, CreateView, UpdateView, RedirectView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from tasks import models


class DetailTaskView(LoginRequiredMixin, DetailView):
    model = models.Task
    login_url = reverse_lazy('pages:login')
    redirect_field_name = 'next'
    pk_url_kwarg = 'task_id'


class CreateTaskView(LoginRequiredMixin, CreateView):
    model = models.Task
    fields = ('name', 'content', 'status')
    login_url = reverse_lazy('pages:login')

    def get_context_data(self, **kwargs):
        c = super(CreateTaskView, self).get_context_data(**kwargs)
        c['action'] = 'Create'
        return c

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTaskView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "The task has been added.")
        return reverse_lazy('pages:dashboard')


class UpdateTaskView(LoginRequiredMixin, UpdateView):
    model = models.Task
    fields = ('name', 'content', 'status')
    login_url = reverse_lazy('pages:login')
    pk_url_kwarg = 'task_id'

    def get_context_data(self, **kwargs):
        c = super(UpdateTaskView, self).get_context_data(**kwargs)
        c['action'] = 'Edit'
        return c

    def get_success_url(self):
        messages.success(self.request, "The task has been updated.")
        return reverse_lazy('pages:dashboard')


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = models.Task
    login_url = reverse_lazy('pages:login')
    pk_url_kwarg = 'task_id'

    def get_success_url(self):
        messages.success(self.request, "The task has been deleted.")
        return reverse_lazy('pages:dashboard')


class GoBackTaskView(LoginRequiredMixin, RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        task = get_object_or_404(self.request.user.task_set.all(), id=kwargs['task_id'])
        task.level_down()
        messages.success(self.request, "The task has been updated.")
        return reverse_lazy('pages:dashboard')


class GoNextTaskView(LoginRequiredMixin, RedirectView):
    pass