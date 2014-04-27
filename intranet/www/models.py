#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.comments.moderation import moderator
from django.conf import settings
from tinymce.models import HTMLField
from django_akismet_comments import AkismetModerator


class News(models.Model):
    class Meta:
        ordering = ("-date",)

    title = models.CharField(verbose_name="Naslov", max_length=150)
    text = HTMLField(verbose_name="Novica")
    image = models.ImageField(blank=True,
                              null=True,
                              upload_to='announce/%Y/%m/',
                              verbose_name="Slika ob objavi")
    date = models.DateTimeField(auto_now_add=True, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    author = models.ForeignKey(User)
    #the field for calendar id's which can not be matched by title to stories
    # TODO: make this foreignkeys to events
    calendar_id = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=2,
                                default='sl',
                                choices=settings.LANGUAGES,
                                blank=True,
                                null=True)

    def get_absolute_url(self):
        return reverse('intranet.www.views.news_detail', args=[self.id,
                                                               self.slug])

    def __unicode__(self):
        return self.title


moderator.register(News, AkismetModerator)
