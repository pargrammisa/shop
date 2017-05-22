from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FirstForm
# Create your views here.
def get_name(request):
	if request.method=="post":
		form=FirstForm(request.Post)
		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		form=FirstForm()
	return render(request,'name.html',{'form':form})
def algorithms(request):
	'''read from data base or taking from users
	vt=
	tm=
	vo=
	ve=
	tmin=
	tmax=
	landa1=
	landa2=
	'''
	vT=vo-vt
	k_prim=ve-vo
	#f=antegral(tmin-td p(t))
	m=safetymargin
	k=vd/vo
	a2=vo*((1-kprim)*(tm-tmin)-(k-1)*(tmax-tm))
	a4=vo*(k-kprim)
	a3=vo*(1-k)
	a=(vo*(tmax-tm))/2
	b=(vT*tm)+((vo*((1-kprim)*(tm-tmin)-(tmax-tm)))/2)
	ctotal=vT+tm+vo*((1-kprim)*f*(tm-tmin+m)+(k-1)*(1-f)*(tmax-tm-m))
	fo=((a2+a4*(tmax-tm))*(a3+a4)/(a4*(a2+(a4*mo))))-(a3/a4)	
	mo_k=((tmax-tm)*((fo-1)*k)+landa1)/((fo-1)*k)+y2
	c0=vT*tm
	c1=a*k+b
	#fmo=f(mo)
	c2=a1+(a2*fmo)+(a3*mo)+(a4*fmo*mo)
	return render_to_response("totalc.html",{"totalc":ctotal,"optimalf":fo,"mo":mo_k,"c0":c0,"c1":c1,"c2":c2})
	
def integrate(request):
	user_input = input("enter the function: " )
	function = lambda x: eval(user_input)
	start=input("enter start point: ")
	end=input("enter end point: ")
	result=integrate.quad(function.start,end)
	return render_to_response(result)

	