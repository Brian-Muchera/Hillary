from django.core.mail import EmailMultiAlternatives
from  django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

def send_inquiry(subject,name,message,client,myaccount):
    Muchera='mucherabrian2@gmail.com'
    
    text_content=render_to_string('inquiry.txt',{'message':message,'name':name})
    html_content=render_to_string('inquiry.html',{'message':message,'name':name})
    
    msg=EmailMultiAlternatives(subject,text_content,client,[myaccount])
    msg.attach_alternative(html_content,'text/html')
    
    msg.send()