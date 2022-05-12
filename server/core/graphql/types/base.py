import graphene
from graphene_django import DjangoObjectType


class DjangoRelayObjectType(DjangoObjectType):
    """Django object type without base64 encoding."""

    id = graphene.ID(required=True, description='ID of the object')

    class Meta:
        abstract = True

    @classmethod
    def node_resolver(cls, _, info, id):  # noqa: WPS125
        """Removing base64 encoding in ID field."""
        return cls.get_node(info, id)

    @classmethod
    def NodeField(cls):  # noqa: N802
        """New Node field."""
        node_field = graphene.relay.Node.Field(cls)
        node_field.wrap_resolve = lambda parent: cls.node_resolver
        return node_field