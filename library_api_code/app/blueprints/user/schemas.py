# from ...extensions import ma
from app.extensions import ma
from app.models import Users
from marshmallow import Schema, fields

class UserSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Users #Creates a schema that validates the data as defined by our Users Model

class LoginSchema(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)
login_schema = LoginSchema()