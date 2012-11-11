from django.db import models

from intranet.org.models import Event


class Video(models.Model):
    event = models.ForeignKey(Event, blank=True, null=True, related_name="video")
    image_url = models.CharField(max_length=240)
    play_url = models.CharField(max_length=240)
    pub_date = models.DateField(db_index=True)
    title = models.CharField(max_length=240, blank=True, null=True)
    remote_id = models.CharField(max_length=100, unique=True, null=True)

    def __unicode__(self):
        return self.videodir

    def get_absolute_url(self):
        return self.play_url
