# coding=utf-8
import json

from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50, default="无名")
    artistId = models.IntegerField()
    artist = models.CharField(max_length=50, default="无名")
    categoryId = models.IntegerField()
    category = models.CharField(max_length=50, default="普通")
    vol = models.CharField(max_length=50, default="2014000000")
    like = models.IntegerField()
    share = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True, editable=True)
    paintings = models.CharField(max_length=1000, default="")

    def __unicode__(self):
        return self.name

    def to_json(self):
        obj_dict = dict(id=self.id, name=self.name, artistId=self.artistId,
                        artist=self.artist, categoryId=self.categoryId,
                        category=self.category, vol=self.vol, like=self.like,
                        share=self.share, time=self.time.isoformat(), paintings=self.paintings, )
        return json.dumps(obj_dict)

    class Meta:
        ordering = ('id',)