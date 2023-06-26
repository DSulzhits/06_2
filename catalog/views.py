from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.http import Http404

from catalog.services import send_email
from catalog.models import Product, BlogRecord, Version
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, reverse, redirect
from catalog.forms import BlogRecordForm, ProductForm, VersionForm


class HomeView(LoginRequiredMixin, generic.TemplateView):
    """Контроллер для работы с домашней страницей, показывает только 4 первых продукта"""
    template_name = 'catalog/home.html'
    extra_context = {
        'object_list': Product.objects.all()[:4],
        'title': 'Домашняя страница'
    }


class ProductListView(LoginRequiredMixin, generic.ListView):
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


class ProductDetailView(LoginRequiredMixin, generic.DetailView):
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

class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    """Контроллер для создания продукта"""
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:products_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ParentFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = ParentFormset(self.request.POST, instance=self.object)
        else:
            formset = ParentFormset(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    """Контроллер для обновления продукта"""
    model = Product
    form_class = ProductForm

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.creator != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object

    def get_success_url(self):
        return reverse('catalog:product_update', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ParentFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = ParentFormset(self.request.POST, instance=self.object)
        else:
            formset = ParentFormset(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, generic.DeleteView):
    """Контроллер для удаления продукта"""
    model = Product
    success_url = reverse_lazy('catalog:products_list')


class VersionListView(LoginRequiredMixin, generic.ListView):
    model = Version
    extra_context = {
        'title': 'Список активных версий',
    }

    def get_queryset(self):
        """Метод благодаря которому отображаются только активные записи"""
        queryset = super().get_queryset()
        queryset = queryset.filter(sign_of_current_version=True)
        return queryset


class VersionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Version
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')


class VersionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:products_list')


class VersionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Version

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_object()
        return context_data


class ContactsView(LoginRequiredMixin, generic.TemplateView):
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

class BlogRecordListView(LoginRequiredMixin, generic.ListView):
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


class BlogRecordDeactivatedListView(LoginRequiredMixin, generic.ListView):
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


class BlogRecordDetailView(LoginRequiredMixin, generic.DetailView):
    """Контроллер для отображения одной блоговой записи в подробностях"""
    model = BlogRecord

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # context_data['title'] = context_data['object']
        context_data['title'] = self.get_object()
        object = self.get_object()
        increase = get_object_or_404(BlogRecord, pk=object.pk)
        increase.views_count()
        if increase.views == 100:
            send_email(increase)
        return context_data


class BlogRecordCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    """Контроллер для создания блоговой записи"""
    model = BlogRecord
    form_class = BlogRecordForm
    permission_required = 'catalog.add_blogrecord'
    success_url = reverse_lazy('catalog:blog_records')

    def form_valid(self, form):
        self.object = form.save()
        self.object.author = self.request.user
        self.object.save()

        return super().form_valid(form)


class BlogRecordUpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    """Контроллер для обновления блоговой записи"""
    model = BlogRecord
    form_class = BlogRecordForm
    permission_required = 'catalog.change_blogrecord'
    success_url = reverse_lazy('catalog:blog_records')


class BlogRecordDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    """Контроллер для удаления блоговой записи"""
    model = BlogRecord
    permission_required = 'catalog.delete_blogrecord'
    success_url = reverse_lazy('catalog:blog_records')


def toggle_activity(request, slug):
    blog_record_item = get_object_or_404(BlogRecord, slug=slug)
    if blog_record_item.sign_of_publication:
        blog_record_item.sign_of_publication = False
    else:
        blog_record_item.sign_of_publication = True
    blog_record_item.save()
    return redirect(reverse('catalog:blog_records'))
