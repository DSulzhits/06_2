from django.shortcuts import render
from catalog.models import Product, BlogRecord
from django.views import generic
from django.urls import reverse_lazy


class HomeView(generic.TemplateView):
    template_name = 'catalog/home.html'
    extra_context = {
        'object_list': Product.objects.all()[:4],
        'title': 'Домашняя страница'
    }


class ProductListView(generic.ListView):
    model = Product
    extra_context = {
        'title': 'Каталог'
    }


# def home(request):
#     context = {
#         'object_list': Product.objects.all(),
#         'title': 'Каталог'
#     }
#     return render(request, 'catalog/home.html', context)


class ProductDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_object()
        return context_data


# def product(request, pk):
#     product_item = Product.objects.get(pk=pk)
#     context = {
#         'object': product_item,
#         'title': product_item.name
#     }
#     return render(request, 'catalog/product.html', context)


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

class BlogRecordListView(generic.ListView):
    model = BlogRecord
    extra_context = {
        'title': 'Список записей'
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=True)
        return queryset


class BlogRecordDetailView(generic.DetailView):
    model = BlogRecord

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # context_data['title'] = context_data['object']
        context_data['title'] = self.get_object()
        return context_data


class BlogRecordCreateView(generic.CreateView):
    model = BlogRecord
    fields = ('title', 'slug', 'content', 'preview')
    success_url = reverse_lazy('catalog: blog_records_list')


class BlogRecordUpdateView(generic.UpdateView):
    model = BlogRecord
    fields = ('title', 'slug', 'content', 'preview')
    success_url = reverse_lazy('catalog: blog_records_list')


class BlogRecordDeleteView(generic.DeleteView):
    model = BlogRecord
    success_url = reverse_lazy('catalog: blog_records_list')
