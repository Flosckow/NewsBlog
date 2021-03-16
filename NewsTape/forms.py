from django import forms
from .models import News, Gallery


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('image', )


class NewsFormPost(forms.ModelForm):
    class Meta:
        model = News
        fields = ('__all__')
