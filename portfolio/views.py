from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import Blog,Inquiry
from django.contrib.auth.models import User
from .forms import InquiryForm
from django.contrib import messages
#from .email import send_inquiry
#from django.core.mail import send_mail
from django.conf import settings



# Create your views here.
def index(request):
    blogs=Blog.objects.order_by('-posted')
    user=User.objects.get(pk=1)
    form=InquiryForm()
   
    return render(request,'portfolio/index.html',{'blogs':blogs,'user':user,'form':form})

#ajax inquiry view functon
def inquiry(request):
    name=request.POST.get('your_name')
    print(name)
    message=request.POST.get('your_message')
    print(message)
    client=request.POST.get('your_email')
    print(client)
    subject=request.POST.get('subject')
    print(subject)
    
      

    
    message=InquiryForm(request.POST)
    message.save()
    data={'success':'{}, Your inquiry has been received, your request will be processed as soon as possible. Thank You!'.format(name)}
    return JsonResponse(data)



def blog(request,blog_id):
    blog_modal=get_object_or_404(Blog,pk=blog_id)
    return render(request,'portfolio/index.html',{'blog_modal':blog_modal})
