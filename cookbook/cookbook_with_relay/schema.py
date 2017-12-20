import graphene
from graphene_django.debug import DjangoDebug

import cookbook_with_relay.ingredients.schema


class Query(cookbook_with_relay.ingredients.schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')


schema = graphene.Schema(query=Query)
