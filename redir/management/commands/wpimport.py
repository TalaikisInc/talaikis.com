from os.path import join
import csv

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from redir.models import Post, Cat


class Command(BaseCommand):
    help = 'Import posts from CSV.'

    def handle(self, *args, **options):
        
        file_name = join(settings.BASE_DIR, "imports", "admin_sekmet_posts.csv")
        category = "LT"

        try:
            cat = Cat.objects.get(title=category)
        except:
            cat = Cat.objects.create(title=category)
        
        with open(file_name, 'r', encoding='utf-8') as f:
            rows = csv.reader(f, delimiter=',', quotechar='"')
            for row in rows:
                try:
                    dte = row[0].split("+")[0]
                    title = row[1]
                    #for langer replaces use replace_all from QProb
                    content = row[2].replace("https://sekmestechnologija.lt", "https://talaikis.com").replace("https://www.sekmestechnologija.lt", "https://talaikis.com")

                    post = Post.objects.create(title=title, date_time=dte, content=content, cat=cat)
                    post.save()
                    print("Wrote post")
                except Exception as err:
                    print(err)

        self.stdout.write(self.style.SUCCESS('Successfully done jobs.'))
