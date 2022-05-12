from server.core.graphql.fields.connection_fields import FilterConnectionField
from server.apps.reports.graphql import types, filters


class Query:
    """Reports queries."""

    historical_reports = FilterConnectionField(types.ReportType, filterset_class=filters.HistoricalReportFilterSet)
