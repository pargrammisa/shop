from django.conf.urls import url
from . import views
app_name="aaa"
urlpatterns=[
	url(r'^$',views.index,name="test")
]
