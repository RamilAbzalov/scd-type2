import graphene
from graphene.relay import Node
from server.core.graphql.types.base import DjangoRelayObjectType
from server.apps.reports.models import Report


class ReportType(DjangoRelayObjectType):

    change_type = graphene.String()
    user_from = graphene.Int()
    user_to = graphene.Int()

    class Meta:
        interfaces = (Node, )
        model = Report
        exclude = ('effective_from', 'effective_to')

    def resolve_change_type(self, _):
        return self.get_change_type_display()

    def resolve_user_from(self, _):
        return self.user_from.id

    def resolve_user_to(self, _):
        return self.user_to.id

    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset.filter(change_type__gt=Report.DELETE)
