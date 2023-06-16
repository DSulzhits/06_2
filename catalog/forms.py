from django import forms

from catalog.models import Product, BlogRecord, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created', 'updated',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        banned_names_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                             'радар']
        if cleaned_data.lower() in banned_names_list:
            raise forms.ValidationError(f'Наименование {cleaned_data} запрещено к использованию')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    # def clean_sign_of_current_version(self):
    #     cleaned_data = self.cleaned_data['sign_of_current_version']
    #     if cleaned_data:
    #         return cleaned_data
    #     else:
    #         return "Версия неактивна"


class BlogRecordForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = BlogRecord
        fields = ('title', 'slug', 'content', 'preview')
