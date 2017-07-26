from functools import lru_cache

from django.shortcuts import render
from django.shortcuts import render
from django.conf import settings

from .forms import ContactForm
from .models import Contacts, Post, Cat


def indx_view(request):
    if request.method == 'POST':
        previous_page = request.get_full_path()

        form = ContactForm(request.POST)

        if form.is_valid():
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            sender = form.cleaned_data['email']
            msg = Contacts.objects.create(name=name, email=sender, message=message)
            msg.save()

            return render(request, 'redir/thanks.html', {'save_contact': True, 'previous_page': previous_page })
        else:
            return render(request, 'redir/form_error.html', {'save_contact': True, 'previous_page': previous_page })
    else:
        form = ContactForm()

    return render(request, 'redir/index.html', {'form': form })


@lru_cache(maxsize=None)
def blog(request, **kwargs):
    cats_en = Cat.objects.filter(lang=0)
    cats_lt = Cat.objects.filter(lang=1)

    try:
        cat_slug = kwargs['cat_slug']
    except:
        cat_slug = None
    
    try:
        post_slug = kwargs['post_slug']
    except:
        post_slug = None

    if (not post_slug is None) & (cat_slug is None):
        #if post is requested
        posts = Post.objects.filter(slug=post_slug)
        return render(request, 'redir/blog.html', {'cats_en': cats_en,
            'cats_lt': cats_lt, 'posts': posts, 'post_slug': post_slug, 'blog': True })
    elif (not cat_slug is None) & (post_slug is None):
        #if category is requested
        cat = Cat.objects.get(slug=cat_slug)
        posts = Post.objects.filter(cat=cat)
        return render(request, 'redir/blog.html', {'cats_en': cats_en, 
            'cats_lt': cats_lt, 'posts': posts, 'cat_slug': cat_slug, 'blog': True })
    else:
        #if main blog page requestewd
        return render(request, 'redir/blog.html', {'cats_en': cats_en, 
            'cats_lt': cats_lt, 'first': True, 'blog': True, 'home': True })


def thanks(request):
    return render(request, 'registration/thanks.html')


def quotes(request):
    return render(request, 'redir/quotes.html')


def quotes_api(request):
    return render(request, 'redir/quotes_api.html')


def weather(request):
    return render(request, 'redir/weather.html')


def wikipedia(request):
    return render(request, 'redir/wikipedia.html')


def page_not_found(request):
    return render(request, template_name='redir/404.html', context=None, content_type=None, status=404, using=None)


def jonas_salk(request):
	return render(request, 'redir/jonas_salk.html')


def permission_denied(request):
    return render(request, template_name='redir/403.html', context=None, content_type=None, status=403, using=None)


def server_error(request):
    return render(request, template_name='redir/500.html', context=None, content_type=None, status=500, using=None)


def bad_request(request):
    return render(request, template_name='redir/400.html', context=None, content_type=None, status=400, using=None)
