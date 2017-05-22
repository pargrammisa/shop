from django.shortcuts import render_to_response,render,get_object_or_404
from .models import Item
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
# Create your views here.

def index(request):
	items=Item.objects.all()
	return render_to_response("shop/index.html",{"items":items})

def detail(request,item_id)	:
	selected_item=Item.objects.get(pk=item_id)
	return render(request,"shop/detail.html",{"item":selected_item})
	
def add(request,item_id):
	item=get_object_or_404(Item,pk=item_id)
	try:
		selecte_choice=item.option_set.get(pk=request.POST["option"])
	except:
		return render(request,"shop/detail.html",{"error_message":"you didnt choose anything,try again","item":item})
	else:
		selecte_choice.number += 1
		selecte_choice.save()
		return HttpResponseRedirect(reverse('shop:result',args=(item.id,)))

def result(request,item_id):
	item=get_object_or_404(Item,pk=item_id)
	sum = 0
	for any_item in Item.objects.all():
		for any_option in any_item.option_set.all():
			if (any_option.number != 0):
				sum += any_option.number*any_item.price
	return render_to_response("shop/result.html",{"item":item,"sum":sum})
	