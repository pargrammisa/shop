from django.conf.urls import url
from .import views
app_name="review"
urlpatterns=[
	#***********************************************************************
	#url(r'^review/$',views.review,name="index"),
	#***********************************************************************
	
	
	#url(r'^index/$',views.IndexView.as_view(),name="index"),
	#url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
	url(r'^integrate/$',views.integrate,name="integrate"),
	url(r'^test1/test2/(?P<var1>[0-9]+)/test3/(?P<var2>[0-9]+)$',views.urltest,name='urltest'),	
	#**************************************************************************************************
	url(r'^(?P<question_id>[0-9]+)/result/$',views.result,name='result'),
	url(r'^vote/(?P<question_id>[0-9]+)/$',views.vote,name="vote"),
	url(r'^detail/(?P<question_id>[0-9]+)/$',views.detail,name="detail"),
	url(r'^index/$',views.index,name="index"),

]