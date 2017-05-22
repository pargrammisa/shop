from django.conf.urls import url
from .import views
urlpatterns=[
	url(r'^your_name/$',views.get_name),
]