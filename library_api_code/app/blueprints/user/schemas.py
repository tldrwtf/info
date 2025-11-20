# from ...extensions import ma
from app.extensions import ma
from app.models import Users

class UserSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Users #Creates a schema that validates the data as defined by our Users Model

user_schema = UserSchema()
users_schema = UserSchema(many=True)
login_schema = UserSchema(exclude=['first_name', 'last_name', 'role'])