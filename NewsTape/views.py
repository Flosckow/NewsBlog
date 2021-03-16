from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from .forms import NewsFormPost, GalleryForm
from .models import News, Gallery


class GetAllNews(View):

    def get(self, request):
        news = News.objects.all()
        try:
            number_range_page = request.GET.get('item')
            paginator = Paginator(news, int(number_range_page))
        except:
            number_range_page = 10
            paginator = Paginator(news, int(number_range_page))
        page = request.GET.get('page')
        try:
            news_list = paginator.page(page)
        except PageNotAnInteger:
            # Если страница не является целым числом, поставим первую страницу
            news_list = paginator.page(1)
        except EmptyPage:
            # Если страница больше максимальной, доставить последнюю страницу результатов
            news_list = paginator.page(paginator.num_pages)
        return render(request, 'news_list.html', {'page': page, 'news_list': news_list})


class GetOneNews(View):

    def get(self, request, id):
        news = News.objects.get(pk=id)
        context = {'news': news}
        return render(request, 'one_news.html', context)


def post_news(request):

    ImageFormSet = modelformset_factory(Gallery, form=GalleryForm, extra=4)

    if request.method == "POST":
        form = NewsFormPost(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Gallery.objects.none())
        if form.is_valid() and formset.is_valid():
            news = form.save(commit=False)
            news.save()

            for form in formset:
                try:
                    photo = Gallery(news=news, image=form.cleaned_data['image'])
                    photo.save()
                except Exception as e:
                    break

            return redirect("get_all_news")
        else:
            print(form.errors, formset.errors)
    else:
        form = NewsFormPost()
        formset = ImageFormSet(queryset=Gallery.objects.none())
    return render(request, 'post_news.html', {'form': form, 'formset': formset})











