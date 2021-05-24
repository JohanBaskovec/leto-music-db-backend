from rest_framework.schemas.openapi import SchemaGenerator


class CustomSchemaGenerator(SchemaGenerator):
    def get_schema(self, *args, **kwargs):
        schema = super().get_schema(*args, **kwargs)
        schema['servers'] = [
            {
                'url': 'http://127.0.0.1:8000'
            }
        ]
        schema["components"]["securitySchemes"] = {
            "Authorization": {
                "type": "apiKey",
                "in": "header",
                "name": "Authentication"
            }
        }
        schema["security"] = [{"Authorization": []}]
        return schema
