from django.shortcuts import render
from catalog.models import Product


def home(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Каталог'
    }
    return render(request, 'catalog/home.html', context)


def info(request):
    return render(request, 'catalog/info.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'User {name}, with phone {phone}, send message: {message}')
    return render(request, 'catalog/contacts.html')
