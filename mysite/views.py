from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime
def current_datetime(request):
	now=datetime.datetime.now()
	html="<html><body>it is now %s.</body></html>" %now
	return HttpResponse(html)
def hours_ahead(request,digit):
	digit=int(digit)
	time=datetime.datetime.now()+datetime.timedelta(hours=digit)
	html="<html><body>in %s hours,it will be %s</html></body>"%(digit,time)
	return HttpResponse(html)
def test(request):
	test="aaaafarin"
	return HttpResponse(test)

def clss(request):
	class Person():
		def __init__(self,name,family):
			self.first_name,self.last_name=name,family
	t=Template('hello,{{obj.first_name}},{{obj.last_name}}.')
	c=Context({'obj':Person('parisa','babamohammadi')})
	return HttpResponse(t.render(c))
def test3(request):
	person={'name':"parisa","age":23}
	t=Template('{{var.name}} is {{var.age}} year old')


	c=Context({"var":person})
	return HttpResponse(t.render(c))
def test4(request):
	person={'name':"parisa","age":23}
	t=Template('{{var.name}} is {{var.age}} year old')
	c=Context({"var":person})
	return HttpResponse(t.render(c))
def test5(request):
	t=Template('{{var.upper}} is {{var}}')
	c=Context({"var":"parisa"})
	return HttpResponse(t.render(c))
def test6(request):
	t=Template('{{var.1}} is {{var.0.upper}}')
	c=Context({"var":["parisa","sheri"]})
	return HttpResponse(t.render(c))	
"""def test7(request):
	t=Template(
  ('{% if athlete_list %}
		<p>the athlit list is:{{athlete_list}}.</p>
	{%else%}
		<p>there is no athlete</p>
		{%if coach_list%}
			<p>here is coach list:{{coach_list}}</p>
		{%endif%}
	<%endif%>')
	c=Context({"athlete_list":["at1","at2","at3"],"coach_list":["c1","c2","c3"]})
	return HttpResponse(t.render(c))"""
def test8(request):
	now = datetime.datetime.now()
	t = get_template('current_datetime.html')
	c={'current_date':now}
	html = t.render(c)
	return HttpResponse(html)
"""best practice for writing template"""
from django.shortcuts import render_to_response
def test9(request):
	now=datetime.datetime.now()
	return render_to_response('current_datetime.html',{'current_date':now})
def test10(request):#wrong
	now=datetime.datetime.now()
	return render_to_response('current_datetime.html',locals())
def test11(request):#vaghti template dar adrese asli ke baraye template dar setting gharar dadehim nabashad
	now=datetime.datetime.now()
	return render_to_response('tem1/current_datetime.html',{'current_date':now})
def test12(request):#include kardan yek template dar template
	now=datetime.datetime.now()
	return render_to_response('temp2.html',{'current_date':now,'name':"soosan"})
def test13(request):#test include kardan current_datetime.html dar temp1.html baraye var haye ke dar template include shodeh lazem hastand niz bayad meghdar dahim dar gheyre insoorat neshan dadeh nemishavand.wrong:javab nemidahad
	now=datetime.datetime.now()
	return render_to_response('temp2.html',{"family":"abc"})
def test14(request):#sahih balaye
	now=datetime.datetime.now()
	return render_to_response('temp2.html',{"current_date":now,"family":"abc"})
def test15(request):#ers bari(best practice).tarif paye baraye har safhe
	return render_to_response('base.html',{"var":15})
def test16(request):#ers bordan az safhe bala
	return render_to_response('basesec.html',{"name":"pargrammisa"})
