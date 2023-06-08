from django.shortcuts import render
from .models import *
def home(Request):
    return render(Request,'index.html')

def shop(Request,category):
    cat=Website_Category.objects.all()
    data=Product.objects.filter(product_category=Website_Category.objects.get(category=category))
    
    return render(Request,'buy.html',{'data':data,'cat':cat})

def EnquiryPage(Request,id):
    if(Request.method=="POST"):
        data=Product.objects.get(product_id=id)
        e=Enquiry()
        e.client_name=Request.POST.get('name')
        e.client_email=Request.POST.get('email')
        e.client_phone=Request.POST.get('phone')
        e.client_subject=Request.POST.get('subject')
        e.client_message=Request.POST.get('message')
        e.product_id=data.product_id
        e.product_name=data.product_name
        e.product_image=data.product_image
        e.product_price=data.product_price
        e.product_web_link=data.product_web_link
        e.product_technology=data.product_technology
        e.save()
        
    return render(Request,'enquiry.html')

def CustomizedEnquiryPage(Request):
    if(Request.method=="POST"):
        e=Enquiry()
        e.client_name=Request.POST.get('name')
        e.client_email=Request.POST.get('email')
        e.client_phone=Request.POST.get('phone')
        e.client_subject=Request.POST.get('subject')
        e.client_message=Request.POST.get('message')
        e.save()
        
    return render(Request,'enquiry.html')

