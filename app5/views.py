from django.shortcuts import render
from django.http import HttpResponse
from .serializers import courseserializer
from rest_framework import viewsets
from .models import Course

from django.forms import contactform

class CourseView(viewsets.ModelViewSet):
	queryset=Course.objects.all()
	serializer_class=courseserializer
# Create your views here.
def home(request):

	#https://www.youtube.com/watch?v=TfuJSXTE9Rk

	return render(request,'app5/home.html',data)
	#data['4. close'].plot()
	#plt.title('Intraday TimeSeries Google')
	#plt.show()




	#return render(request,'app5/home.html',{})

#def about(request):
	#return render(request,'app5/about.html',{})

def contact(request):
	form=contactform(request.POST or None)
	if form.isvaild():
		print(form.cleaned_data)
	return render(request,'app5/contact.html',{})

#def faq(request):
	#return render(request,'app5/faq.html',{})
