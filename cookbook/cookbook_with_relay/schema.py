import graphene

import cookbook_with_relay.ingredients.schema


class Query(cookbook_with_relay.ingredients.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
