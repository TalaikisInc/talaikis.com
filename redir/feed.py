from functools import lru_cache
from datetime import datetime, timedelta

from django.contrib.syndication.views import Feed
from django.utils.html import strip_tags

from .models import Post


@lru_cache(maxsize=128)
class BlogFeed(Feed):
    title = 'Talaikis blog, trading, developing and changing the world.'
    link = "https://talaikis.com"

    def items(self):
        posts = Post.objects.filter(date_time__gte=(datetime.now() - \
            timedelta(days=30))).order_by('date_time').reverse()
        return posts

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return datetime.combine(item.date_time, time())

    def item_category(self, item):
        return item.cat

    def item_link(self, item):
        return "{0}/{1}/".format(self.link, item.slug)

    def item_description(self, item):
        text = strip_tags(item.content)[:1500]
        return text
