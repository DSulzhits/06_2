from django.shortcuts import render
from catalog.models import Product
from django.views import generic


class HomeView(generic.TemplateView):
    template_name = 'catalog/home.html'
    extra_context = {
        'object_list': Product.objects.all(),
        'title': 'Каталог'
    }


# def home(request):
#     context = {
#         'object_list': Product.objects.all(),
#         'title': 'Каталог'
#     }
#     return render(request, 'catalog/home.html', context)


def product(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object': product_item,
        'title': product_item.name
    }
    return render(request, 'catalog/product.html', context)


class ContactsView(generic.TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {
        'title': 'Контакты'
    }

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        print(f'User {name}, with phone {phone}, send message: {message}')
        return render(request, self.template_name)

# def contacts(request):
#    if request.method == "POST":
#        name = request.POST.get('name')
#        phone = request.POST.get('phone')
#        message = request.POST.get('message')
#        print(f'User {name}, with phone {phone}, send message: {message}')
#    return render(request, 'catalog/contacts.html')
