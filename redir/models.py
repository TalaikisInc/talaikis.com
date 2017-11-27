from __future__ import unicode_literals
from datetime import datetime

from django.template.defaultfilters import slugify
from django.utils.translation import ugettext as T
from django.db import models


class AutoSlugifyOnSaveModel(models.Model):
    """
    http://www.laurencegellert.com/2016/04/django-automatic-slug-generator/
    Models that inherit from this class get an auto filled slug property based on the models name property.
    Correctly handles duplicate values (slugs are unique), and truncates slug if value too long.
    The following attributes can be overridden on a per model basis:
    * value_field_name - the value to slugify, default 'name'
    * slug_field_name - the field to store the slugified value in, default 'slug'
    * max_interations - how many iterations to search for an open slug before raising IntegrityError, default 1000
    * slug_separator - the character to put in place of spaces and other non url friendly characters, default '-'
    """

    def save(self, *args, **kwargs):
        pk_field_name = self._meta.pk.name
        value_field_name = getattr(self, 'value_field_name', 'title')
        slug_field_name = getattr(self, 'slug_field_name', 'slug')
        max_interations = getattr(self, 'slug_max_iterations', 1000)
        slug_separator = getattr(self, 'slug_separator', '-')

        # fields, query set, other setup variables
        slug_field = self._meta.get_field(slug_field_name)
        slug_len = slug_field.max_length
        queryset = self.__class__.objects.all()

        # if the pk of the record is set, exclude it from the slug search
        current_pk = getattr(self, pk_field_name)

        if current_pk:
            queryset = queryset.exclude(**{pk_field_name: current_pk})

        # setup the original slug, and make sure it is within the allowed length
        slug = slugify(getattr(self, value_field_name)).replace('-', '_')

        if slug_len:
            slug = slug[:slug_len]

        original_slug = slug

        # iterate until a unique slug is found, or max_iterations
        counter = 2
        while queryset.filter(**{slug_field_name: slug}).count() > 0 and counter < max_interations:
            slug = original_slug
            suffix = '%s%s' % (slug_separator, counter)
            if slug_len and len(slug) + len(suffix) > slug_len:
                slug = slug[:slug_len-len(suffix)]
            slug = '%s%s' % (slug, suffix)
            counter += 1

        if counter == max_interations:
            raise IntegrityError('Unable to locate unique slug')

        setattr(self, slug_field.attname, slug)

        super(AutoSlugifyOnSaveModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class QuoteCat(models.Model):
	id = models.BigAutoField(primary_key=True)
	cat = models.CharField(max_length=140, verbose_name=T("Category"), unique=True)

	def __unicode__(self):
		return u'%s' %(self.cat)

	def __str__(self):
		return u'%s' %(self.cat)


class Cat(AutoSlugifyOnSaveModel):
	LANGUAGES = (
        (0, 'English'),
        (1, 'Lietuvių')
    )
	id = models.BigAutoField(primary_key=True)
	title = models.CharField(max_length=140, verbose_name=T("Category"), unique=True)
	slug = models.CharField(max_length=140, verbose_name=T("Slug"), blank=True, null=True)
	lang = models.SmallIntegerField(choices=LANGUAGES, default=0)

	def __unicode__(self):
		return u'%s' %(self.title)

	def __str__(self):
		return u'%s' %(self.title)


class QuoteAuthor(models.Model):
	id = models.BigAutoField(primary_key=True)
	author = models.CharField(max_length=140, verbose_name=T("Author"), unique=True)

	def __unicode__(self):
		return u'%s' %(self.author)

	def __str__(self):
		return u'%s' %(self.author)


class Post(AutoSlugifyOnSaveModel):
	RATINGS = (
		(0, 'Not applicable'),
        (1, 'Very bad'),
        (2, 'Poor'),
		(3, 'Average'),
		(4, 'Very good'),
		(5, 'Excellent')
    )

	id = models.BigAutoField(primary_key=True)
	title = models.CharField(max_length=250, verbose_name=T("Title"), unique=True)
	date_time = models.DateTimeField(verbose_name=T("Date"), default=datetime.now())
	content = models.TextField(verbose_name=T("Content"))
	cat = models.ForeignKey(Cat, verbose_name=T("Category"), blank=True, null=True)
	slug = models.CharField(max_length=250, verbose_name=T("Slug"), blank=True, null=True)
	rate = models.SmallIntegerField(choices=RATINGS, default=0)
	image = models.ImageField(upload_to="uploads/", blank=True, null=True, verbose_name=T("Image"))

	def __unicode__(self):
		return u'%s %s' %(self.title, self.cat)

	def __str__(self):
		return u'%s %s' %(self.title, self.cat)
	
	class Meta:
		ordering = ['-date_time']


class Quotes(models.Model):
	id = models.BigAutoField(primary_key=True)
	quote = models.TextField(verbose_name=T("Quote"))
	author = models.ForeignKey(QuoteAuthor, verbose_name=T("Author"))
	cat = models.ForeignKey(QuoteCat, verbose_name=T("Category"))

	def __unicode__(self):
		return u'%s %s %s' %(self.quote, self.author, self.cat)

	def __str__(self):
		return u'%s %s %s' %(self.quote, self.author, self.cat)

	class Meta:
		unique_together = ["quote", "author"]


class Contacts(models.Model):
	id = models.BigAutoField(primary_key=True)
	name = models.CharField(max_length=140, verbose_name=T("Name"))
	email = models.EmailField(max_length=150, verbose_name=T("Email"))
	message = models.TextField(verbose_name=T("Message"))

	def __unicode__(self):
		return u'%s' %(self.name)

	def __str__(self):
		return u'%s' %(self.name)


class Subscriber(models.Model):
	id = models.BigAutoField(primary_key=True)
	name = models.CharField(max_length=140, verbose_name=T("Name"))
	email = models.EmailField(max_length=150, verbose_name=T("Email"))
	cat = models.ForeignKey(Cat, verbose_name=T("Category"), blank=True, null=True)

	def __unicode__(self):
		return u'%s' %(self.name)

	def __str__(self):
		return u'%s' %(self.name)
