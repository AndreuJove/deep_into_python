from marshmallow import Schema, fields
from marshmallow.exceptions import ValidationError


fields.String


class MatrixSchema(Schema):

    matrix = fields.List(fields.List(fields.Integer))


data = {"javi": [[1]]}

try:
    result = MatrixSchema().load(data)
except ValidationError as error:

    breakpoint()
