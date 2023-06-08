from django.shortcuts import render
from catalog.models import Product, BlogRecord
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, reverse, redirect


class HomeView(generic.TemplateView):
    """Контроллер для работы с домашней страницей, показывает только 4 первых продукта"""
    template_name = 'catalog/home.html'
    extra_context = {
        'object_list': Product.objects.all()[:4],
        'title': 'Домашняя страница'
    }


class ProductListView(generic.ListView):
    """Контроллер для работы со страницей, со всеми продуктами"""
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
    """Контроллер для работы со страницей продукта (подробная информация о продукте)"""
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
    """Контроллер для работы страницы с контактами"""
    template_name = 'catalog/contacts.html'
    extra_context = {
        'title': 'Контакты'
    }

    def post(self, request, *args, **kwargs):
        """Метод для отправки данных пост запросом на сервер"""
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
    """Контроллер для отображения блоговых записей"""
    model = BlogRecord
    extra_context = {
        'title': 'Список записей'
    }

    def get_queryset(self):
        """Метод благодаря которому отображаются только активные записи"""
        queryset = super().get_queryset()
        queryset = queryset.filter(sign_of_publication=True)
        return queryset


class BlogRecordDeactivatedListView(generic.ListView):
    """Контроллер для отображения блоговых записей"""
    model = BlogRecord
    extra_context = {
        'title': 'Список деактивированных записей'
    }

    def get_queryset(self):
        """Метод благодаря которому отображаются только неактивные записи"""
        queryset = super().get_queryset()
        queryset = queryset.filter(sign_of_publication=False)
        return queryset


class BlogRecordDetailView(generic.DetailView):
    """Контроллер для отображения одной блоговой записи в подробностях"""
    model = BlogRecord

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # context_data['title'] = context_data['object']
        context_data['title'] = self.get_object()
        object = self.get_object()
        increase = get_object_or_404(BlogRecord, pk=object.pk)
        increase.views_count()
        # if increase.views == 100:
        #     send_email(increase)
        return context_data


class BlogRecordCreateView(generic.CreateView):
    """Контроллер для создания блоговой записи"""
    model = BlogRecord
    fields = ('title', 'slug', 'content', 'preview')
    success_url = reverse_lazy('catalog:blog_records')


class BlogRecordUpdateView(generic.UpdateView):
    """Контроллер для обновления блоговой записи"""
    model = BlogRecord
    fields = ('title', 'slug', 'content', 'preview')
    success_url = reverse_lazy('catalog:blog_records')


class BlogRecordDeleteView(generic.DeleteView):
    """Контроллер для удаления блоговой записи"""
    model = BlogRecord
    success_url = reverse_lazy('catalog:blog_records')


def toggle_activity(request, slug):
    blog_record_item = get_object_or_404(BlogRecord, slug=slug)
    if blog_record_item.sign_of_publication:
        blog_record_item.sign_of_publication = False
    else:
        blog_record_item.sign_of_publication = True
    blog_record_item.save()
    return redirect(reverse('catalog:blog_records'))
