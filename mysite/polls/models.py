# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(verbose_name = _('question'), max_length=200)
    pub_date = models.DateTimeField(verbose_name = _('publish_date'))

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = _('q_publish_recently')

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = _('poll')
        verbose_name_plural = _('polls')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, verbose_name = _('option'))
    votes = models.IntegerField(default=0, verbose_name = _('number_of_votes'))

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = _('option')
        verbose_name_plural = _('options')

