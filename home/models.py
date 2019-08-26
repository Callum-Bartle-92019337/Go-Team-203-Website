import logging

from django.contrib.auth.signals import user_login_failed
from django.dispatch import receiver
from django.utils import timezone
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

log = logging.getLogger(__name__)

# log failed login and user name to identify brute force attacks
@receiver(user_login_failed)
def user_login_failed_callback(sender, credentials, **kwargs):
    log.warning('login failed for: {credentials}'.format(
        credentials=credentials['username'],
    ))


class Review(models.Model):

    TYPE_CHOICES =(
        ('Food' ,'Food'),
        ('Activities', 'Activities'),
        ('Accommodation','Accommodation')
    )

    title = models.CharField(max_length=50)
    type = models.CharField(choices=TYPE_CHOICES, max_length=30, default=2)
    content = models.CharField(max_length=4096)
    poster = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    posted = models.CharField(max_length=10, default=timezone.now)
    image = models.ImageField(upload_to='review_Images/')

    readonly_fields=('posted', 'poster')

    def __str__(self):
        return self.title + ' - ' + self.poster.username
