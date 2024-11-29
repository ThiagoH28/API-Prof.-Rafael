from marshmallow import Schema, fields, validate, ValidationError

class BookSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(min=1, max=255))
    genre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    year = fields.Integer(required=True, validate=validate.Range(min=0))
    available = fields.Boolean(required=True)
    author_id = fields.Integer(required=True)

    def validate(self, data):
        errors = self.validate(data)
        if errors:
            raise ValidationError(errors)
        return data
