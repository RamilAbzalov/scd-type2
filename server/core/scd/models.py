from django.db import models
from django.utils import timezone

DEFAULT_END_TIME = timezone.datetime(9999, 1, 1)


class FactQuerySet(models.QuerySet):

    def filter_identity_fact(self, kwargs):
        lookup = {}
        identity_lookup = self.model._meta.identity_lookup  # noqa
        for identity_key in identity_lookup:
            lookup[identity_key] = kwargs.get(identity_key)
        return self.filter(**lookup)

    def filter_active_identity_facts(self, kwargs):
        return self.filter_identity_fact(kwargs).filter(change_type=self.model.ADD)

    def create(self, **kwargs):
        qs = self.filter_active_identity_facts(kwargs)
        if not qs.exists():
            kwargs.update(change_type=self.model.ADD)
            return super().create(**kwargs)
        instance = qs.get()
        instance.modify()
        return instance.add(data=kwargs)


class FactTable(models.Model):
    DELETE = 0
    MODIFY = 1
    ADD = 2

    CHANGE_TYPES = (
        (DELETE, 'Deleted'),
        (MODIFY, 'Modified'),
        (ADD, 'Actual'),
    )

    change_type = models.PositiveIntegerField(choices=CHANGE_TYPES)
    effective_from = models.DateTimeField(default=timezone.now)
    effective_to = models.DateTimeField(default=DEFAULT_END_TIME)

    objects = FactQuerySet.as_manager()

    class Meta:
        abstract = True
        identity_lookup = ('id', )

    def clone(self, change_type=None):
        self.pk = None
        if change_type:
            self.change_type = change_type
        return self

    def delete(self):
        self.change_type = self.DELETE
        self.effective_to = timezone.now()
        self.save()

    def modify(self):
        self.change_type = self.MODIFY
        self.effective_to = timezone.now()
        self.save()

    def add(self, **data):
        clone = self.clone(change_type=self.ADD)
        for key, value in data:
            setattr(clone, key, value)
        clone.save(force_insert=True)
        return clone
