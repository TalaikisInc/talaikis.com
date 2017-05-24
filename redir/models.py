from __future__ import unicode_literals

from django.utils.translation import ugettext as T
from django.db import models


class QuoteCat(models.Model):
	id = models.BigAutoField(primary_key=True)
	cat = models.CharField(max_length=140, verbose_name=T("Category"), unique=True)

	def __unicode__(self):
		return u'%s' %(self.cat)

	def __str__(self):
		return u'%s' %(self.cat)


class Cat(models.Model):
	id = models.BigAutoField(primary_key=True)
	cat = models.CharField(max_length=140, verbose_name=T("Category"), unique=True)

	def __unicode__(self):
		return u'%s' %(self.cat)

	def __str__(self):
		return u'%s' %(self.cat)


class QuoteAuthor(models.Model):
	id = models.BigAutoField(primary_key=True)
	author = models.CharField(max_length=140, verbose_name=T("Author"), unique=True)

	def __unicode__(self):
		return u'%s' %(self.author)

	def __str__(self):
		return u'%s' %(self.author)


class Post(models.Model):
	id = models.BigAutoField(primary_key=True)
	title = models.CharField(max_length=250, verbose_name=T("Title"), unique=True)
	content = models.TextField(verbose_name=T("Content"))
	cat = models.ForeignKey(Cat, verbose_name=T("Category"))

	def __unicode__(self):
		return u'%s %s' %(self.title, self.cat)

	def __str__(self):
		return u'%s %s' %(self.title, self.cat)


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
