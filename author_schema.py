from marshmallow import Schema, fields, validate, ValidationError

class AuthorSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    birth_date = fields.Date(required=False)
    nationality = fields.String(required=False, validate=validate.Length(max=100))

    def validate(self, data):
        errors = self.validate(data)
        if errors:
            raise ValidationError(errors)
        return data
