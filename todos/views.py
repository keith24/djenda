from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from todos.models import TodoItem


class TodoOwnerMixin(object):
	def get_object(self, queryset=None):
		"""Returns the object the view is displaying.  """

		if queryset is None:
			queryset = self.get_queryset()

		pk = self.kwargs.get(self.pk_url_kwarg, None)
		queryset = queryset.filter(pk=pk, owner=self.request.user)

		try: obj = queryset.get()
		except ObjectDoesNotExist:
			raise PermissionDenied

		return obj

class LoggedInMixin(object):
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class TodoListView(LoggedInMixin, TodoOwnerMixin, ListView):
	model = TodoItem
	template_name = 'todo_list.html'
	
	def get_queryset(self):
		return TodoItem.objects.filter(owner=self.request.user)

class TodoItemView(LoggedInMixin, DetailView):
	model = TodoItem
	template_name = 'item.html'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(TodoItemView, self).dispatch(*args, **kwargs)

class DeleteItemView(LoggedInMixin, DeleteView):
	model = TodoItem
	template_name = 'delete_item.html'

	def get_success_url(self):
		return reverse('todo-list')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(DeleteItemView, self).dispatch(*args, **kwargs)

class UpdateItemView(LoggedInMixin, UpdateView):
	model = TodoItem
	template_name = 'edit_item.html'
	fields = ['text', 'due_date', 'todo_date', 'start_time', 'end_time']

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super(UpdateItemView, self).form_valid(form)

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(UpdateItemView, self).dispatch(*args, **kwargs)

	def get_success_url(self):
		return reverse('todo-list')

	def get_context_data(self, **kwargs):
		context = super(UpdateItemView, self).get_context_data(**kwargs)
		context['action'] = reverse('item-edit', kwargs={'pk': self.get_object().id})
		return context

class NewItemView(LoggedInMixin, CreateView):
	model = TodoItem
	template_name = 'edit_item.html'
	fields = ['text', 'due_date', 'todo_date', 'start_time', 'end_time']

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super(NewItemView, self).form_valid(form)

	def get_success_url(self):
		return reverse('todo-list')

	def get_context_data(self, **kwargs):
		context = super(NewItemView, self).get_context_data(**kwargs)
		context['action'] = reverse('new-item')
		return context

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(NewItemView, self).dispatch(*args, **kwargs)

