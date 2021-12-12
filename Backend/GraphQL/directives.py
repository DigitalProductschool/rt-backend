from ariadne import SchemaDirectiveVisitor
from graphql import default_field_resolver, GraphQLError
from functools import partial


class IsAuthenticatedDirective(SchemaDirectiveVisitor):
    def visit_object(self, object_):
        self.ensure_fields_wrapped(object_)

    def visit_field_definition(self, field, object_type):
        self.ensure_fields_wrapped(object_type)

    def ensure_fields_wrapped(self, object_type):

        def resolve_is_authenticated(_, info,f=None, o=None):
            user = info.context.get('user')
            if user is None:
                raise GraphQLError(message="User does not have permissions")
            result = original_resolver(_, info)
            return result

        for _, field in object_type.fields.items():
            original_resolver = field.resolve or default_field_resolver
            field.resolve = partial(
                resolve_is_authenticated, f=field, o=object_type)
