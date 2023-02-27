from django.shortcuts import render
from .models import Product, Category, Rating
from django.conf import settings
from django.core.mail import send_mail

def home(request):
    product = Product.objects.all()
    ratings = Rating.objects.all()
    feature = Product.objects.filter(products_featured=True)
    context = {"product":product, "ratings":ratings, "feature":feature} 
    return render(request, 'index.html', context)

def category(request,id):
    category = Category.objects.get(id=id)
    products = Product.objects.filter(category = id)
    return render(request, 'category.html', {"category":category, "products":products})

def product(request,id):
    products = Product.objects.get(id = id)
    return render(request, 'product.html', {"products":products , "category":category})

def contact(request):
    return render(request, 'contact.html')

def sendmail(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        message = request.POST['message']
        subject = 'Form Detail'
        info = "Username " + name +" email " + email + " number " + number + " message " +message
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['sahardevjani635@gmail.com']
        send_mail( subject, info, email_from, recipient_list )

        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')
    
