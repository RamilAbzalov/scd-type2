from django.contrib.auth import get_user_model
from django.db import models
from server.core.scd.models import FactQuerySet, FactTable

User = get_user_model()


class ReportQuerySet(FactQuerySet):
    """Report QS."""


class Report(FactTable):

    title = models.CharField(max_length=255, verbose_name='Title')
    user_from = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reports_by_from',
        verbose_name='User from',
    )
    user_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reports_by_to',
        verbose_name='User to',
    )

    objects = ReportQuerySet.as_manager()

    class Meta:
        identity_lookup = ('title', )
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'
