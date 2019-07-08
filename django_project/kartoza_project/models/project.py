from django.db import models
from mezzanine.core.fields import RichTextField
from mezzanine.utils.models import AdminThumbMixin


class Project(AdminThumbMixin, models.Model):

    name = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name='Project name'
    )

    short_description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Project short description'
    )

    project_details = RichTextField(
        null=True,
        blank=True,
        verbose_name='Project details'
    )

    thumbnail = models.ImageField(
        null=True,
        blank=True,
        upload_to='project',
        verbose_name='Project thumbnail'
    )

    categories = models.ManyToManyField(
        'kartoza_project.ProjectCategory',
        verbose_name='Categories',
        null=True,
        blank=True,
        related_name='project_category'
    )

    date_start = models.DateField(
        null=True,
        blank=True
    )

    date_end = models.DateField(
        null=True,
        blank=True
    )

    clients = models.ManyToManyField(
        'clients.Client',
        null=True,
        blank=True,
        related_name="clients"
    )

    admin_thumb_field = 'thumbnail'

    def __unicode__(self):
        return self.name



