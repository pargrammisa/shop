"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views

import books

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^time/$',views.current_datetime),
	url(r'^time/plus/(\d{1,2})/$',views.hours_ahead),
	url(r'^test/*p$',views.test),
	url(r'^test2/$',views.clss),
	url(r'^test3/$',views.test3),
	url(r'^test5/$',views.test5),
	url(r'^test6/$',views.test6),
	url(r'^test8/$',views.test8),
	url(r'^test9/$',views.test9),
	url(r'^test10/$',views.test10),	
	url(r'^test11/$',views.test11),	
	url(r'^test12/$',views.test12),	
	url(r'^test14/$',views.test14),
	url(r'^test15/$',views.test15),
	url(r'^test16/$',views.test16),
	#url(r'^test17/$',views.test17),
	url(r'^books/',include('books.urls')),
	url(r'^aaa/',include('aaa.urls')),
	url(r'^search/',books.views.search),
	url(r'^st/',include('static.urls')),
	url(r'^master/',include('master.urls')),
	url(r'^review/',include('review.urls')),
	url(r'^shop/',include('shop.urls')),
] 
