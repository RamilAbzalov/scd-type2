from server.core.graphql.mutations.base import BaseMutation
from server.apps.reports.graphql import inputs, types
from server.apps.reports.models import Report


class CreateReportMutation(BaseMutation):
    permission_classes = []
    Input = inputs.CreateReportInput()
    Output = types.ReportType

    @classmethod
    def mutate(cls, info, input_):
        return Report.objects.create(**input_)


class Mutation:
    """Reports mutations."""

    create_report = CreateReportMutation.Field()
