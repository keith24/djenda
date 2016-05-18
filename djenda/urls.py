from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^admin/', include(admin.site.urls), name='admin'),
	url('^accounts/', include('django.contrib.auth.urls')),

	url(r'^', include('todos.urls'), name='todos'),
]
