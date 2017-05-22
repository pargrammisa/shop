from django.conf.urls import url
from .import views
app_name="shop"
urlpatterns=[
	url(r'^index/$',views.index,name="index"),
	url(r'^detail/(?P<item_id>[0-9]+)$',views.detail,name="detail"),
	url(r'^result/(?P<item_id>[0-9]+)$',views.result,name="result"),
	url(r'^add/(?P<item_id>[0-9]+)$',views.add,name="add"),
]