from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import (handler400, handler403, handler404, handler500)

from redir.feed import BlogFeed
from redir import views, serializers


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.indx_view),
    url(r'^jonas_salk/$', views.jonas_salk, name="jonas_salk"),
    url(r'^blog/category/(?P<cat_slug>[-\w]+)/$', views.blog, name='blog-cat'),
    url(r'^blog/post/(?P<post_slug>[-\w]+)/$', views.blog, name='blog-post'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^feed/$', BlogFeed()),

	#form processes
	url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^quotes/$', views.quotes, name='quotes'),
    url(r'^random_quotes_api/$', views.quotes_api, name='quotes'),
    url(r'^weather/$', views.weather, name='weather'),
    #url(r'^wikipedia/$', views.wikipedia, name='wikipedia'),
	url(r'^api/quotes/$', serializers.quote_list),
	url(r'^api/quotes/random/$', serializers.random_quote),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler400 = 'redir.views.bad_request'
handler403 = 'redir.views.permission_denied'
handler404 = 'redir.views.page_not_found'
handler500 = 'redir.views.server_error'
