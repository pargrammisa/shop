from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponse
from review.models import Question,Choice
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

def review(request):
	obj2=[]
	q=Question(question_text="what's new parisa joon?",pub_date=timezone.now())
	q.save()
	id=q.id
	text=q.question_text
	date=q.pub_date
	q.choice_set.create(choice_text="ch1",votes=2)
	q.choice_set.create(choice_text="ch2",votes=4)
	q.choice_set.create(choice_text="ch3",votes=6)
	obj12=q.choice_set.all()	
	c=Question.objects.filter(id=96)
	c.delete()
	#obj2=Question.objects.filter(id=27).count()
	obj3=Question.objects.all()
	obj4=Question.objects.exists()
	#obj5=Question.objects.get(id=27)
	obj6=list(Question.objects.all())
	obj7=type(obj6)
	obj8=len(Question.objects.all())
	obj9=Question.objects.values_list('id')
	obj10="numbr of records %i" %(Question.objects.all().count())
	return render_to_response("review/review.html",{"q":q,"id":id,"text":text,"date":date,"obj2":obj2,"obj3":obj3,"obj4":obj4,"obj6":obj6,"obj7":obj7,"obj8":obj8,"obj9":obj9,"obj10":obj10,"obj12":obj12})
	#def detail(request,question_id):
	#return HttpResponse("you are looking at question %s."%question_id)


def test_error(request,question_id):
	question=get_object_or_404(Question,pk=question_id)
	return render_to_response('review/test.html',{'question':question})
def urltest(request,var1,var2):
	sum=int(var1)+int(var2)
	return render_to_response('review/urltest.html',{"sum":sum})
	
	
#**********************************************************************************************************************************************	
def index(request):
	question_list=Question.objects.all()
	return render_to_response("review/index.html",{"ql":question_list})


	
def detail(request,question_id):
	q=Question.objects.get(id=question_id)
	
	return render(request,'review/detail.html',{"question":q})

	
def result(request,question_id):
	question=get_object_or_404(Question,pk=question_id)
	return render_to_response('review/results.html',{'question':question})
	
	
def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
		
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'review/detail.html', {
			'question': question, 
			'error_message': "you didnt choose anything"
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('review:result',args=(question.id,)))

		
		
#****************************************************************************************************************************************************
		
		"""print ("="*30)
		print ("inside vote second else")
		print ("Testing the reverse function:")
		print ("Question ID is: ", question.id)
		made_url = reverse('review:result',args=(question.id,))
		print ("The reverse function result is: ", made_url)
		print ("The type of reverse function result is:", type(made_url))
		
		print ("="*30)
		
		print ("What is in the request object?: ", request)
		print ("What is the type of request?: ", type(request))
		print ("What is User Browser", request.META['HTTP_USER_AGENT'])
		
		print ("="*30)
		#return HttpResponseRedirect("http://www.google.com")
		#return HttpResponse("Hello")
		#my_response = HttpResponse(r"<h1> Hello </h1>")
		#print ("The response object is: ", my_response)
		#my_response["Content-Type"]="img/jpg"
		#return my_response"""
		
	

"""class IndexView(generic.ListView):
	template_name = 'review/index.html'
	context_object_name = 'ql'
	
	def get_queryset(self):
		print ("Query set is run")
		Return the last five published questions.
		return Question.objects.order_by('-pub_date')[:1]
	
class DetailView(generic.DetailView):
	print ("Detail view is used")
	model = Question
	template_name = 'review/detail.html'"""

	

def integrate(request):
	user_input = input("enter the function: " )
	function = lambda x: eval(user_input)
	start=input("enter start point: ")
	end=input("enter end point: ")
	result=integrate.quad(function,start,end)
	return render_to_response(result)