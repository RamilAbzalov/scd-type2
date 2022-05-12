import graphene


class CreateReportInput(graphene.InputObjectType):
    title = graphene.String()
    user_from_id = graphene.Int()
    user_to_id = graphene.Int()
