from django.contrib.auth.models import User
from django.db import models

from taggit.managers import TaggableManager


COMFORT_LEVELS = (
    (0, 'Casual'),
    (1, 'Engaged'),
    (2, 'Expert'),
)

class Bundle(models.Model):
    """A bundle, a virtual envelope for links
    """

    title = models.CharField(max_length=120)
    description = models.TextField(default='', blank=True)

    # meta
    curator = models.ForeignKey(User, related_name='bundles')
    at = models.DateTimeField(auto_now_add=True)

    tags = TaggableManager()

    def __unicode__(self):
        return self.title


class Link(models.Model):
    title = models.CharField(max_length=240)
    url = models.URLField()
    read_time = models.PositiveIntegerField() # in seconds
    is_public = models.BooleanField(default=True)
    published_at = models.DateField()

    def __unicode__(self):
        return self.title


class BundleLink(models.Model):
    link = models.ForeignKey(Link)
    bundle = models.ForeignKey(Bundle)
    curator = models.ForeignKey(User)

    # relative to bundle
    comfort_level = models.PositiveSmallIntegerField(choices=COMFORT_LEVELS) 

    tags = TaggableManager()

    def __unicode__(self):
        return '%s - %s' % (self.link.title, self.bundle.title)
