import django_filters
from server.apps.reports.models import Report


class HistoricalReportFilterSet(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='effective_from', lookup_expr='gte')
    end_date = django_filters.DateFromToRangeFilter(field_name='effective_from', lookup_expr='lte')
    title = django_filters.CharFilter(field_name='title')

    class Meta:
        model = Report
        exclude = ['effective_from', 'effective_to']
