import graphene
from graphene_django.debug import DjangoDebug

import cookbook.ingredients.schema


class Query(cookbook.ingredients.schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')


schema = graphene.Schema(query=Query)
