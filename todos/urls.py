from django.conf.urls import url
import todos.views

urlpatterns = [
	url(r'^$', todos.views.TodoListView.as_view(), name='todo-list'),
	url(r'^new$', todos.views.NewItemView.as_view(), name='new-item'),
	url(r'^edit/(?P<pk>\d+)/$', todos.views.UpdateItemView.as_view(), name='item-edit'),
	url(r'^delete/(?P<pk>\d+)/$', todos.views.DeleteItemView.as_view(), name='item-delete'),
	url(r'^(?P<pk>\d+)/$', todos.views.TodoItemView.as_view(), name='item-view'),
]
