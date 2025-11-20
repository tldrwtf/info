# from ...blueprints.user import users_bp
from app.blueprints.user import users_bp
from .schemas import user_schema, users_schema, login_schema
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import Users, db
from app.extensions import limiter
from werkzeug.security import generate_password_hash,check_password_hash
from app.util.auth import encode_token, token_required

@users_bp.route('/login', methods=['POST'])
@limiter.limit("5 per 10 minute")
def login():
  try:
    # get my user credentials - responsibility for my client
    data = login_schema.load(request.json) #JSON -> Python
  except ValidationError as e:
    return jsonify(e.messages), 400 #Returning the error as a response so the client can see whats wrong with the status code
  
  user = db.session.query(Users).where(Users.email==data['email']).first() #Search my db for a user with the email in the request

  if user and check_password_hash(user.password, data['password']):
    #Create token for user
    token = encode_token(user.id, role=user.role)
    return jsonify({
      "message": f"Welcome {user.first_name}",
      "token": token,
    }), 200


# CREATE USER ROUTE
# Decorator or wrapper
@users_bp.route('', methods=['POST'])
# @limiter.limit("2 per day")
def create_user():
  try:
    # get my user data - responsibility for my client
    data = user_schema.load(request.json) #JSON -> Python
  except ValidationError as e:
    return jsonify(e.messages), 400 #Returning the error as a response so the client can see whats wrong with the status code
  
  data["password"] = generate_password_hash(data["password"]) #resetting the password key's value, to the hash of the current value

  # Create a User object from my user data
  # new_user = Users(first_name=data['first_name'],)
  new_user = Users(**data)
  # add User to session
  db.session.add(new_user)
  # commit to session
  db.session.commit()
  #Python -> JSON
  return user_schema.jsonify(new_user), 201 #Successful creation status code

# READ USERS ROUTE
@users_bp.route("", methods=["GET"]) #Endpoint to get user information
def read_users():
  users = db.session.query(Users).all()
  return users_schema.jsonify(users), 200 #Returns the list of users as JSON and HTTP status 200

# Read Individual User - using a Dynamic Endpoint
@users_bp.route('/profile', methods=['GET'])
@limiter.limit("15 per hour")
@token_required
def read_user():
  user_id = request.logged_in_user_id
  user = db.session.get(Users, user_id)
  return user_schema.jsonify(user), 200

# Delete a User
@users_bp.route("", methods=["DELETE"])
@token_required
def delete_user():
  token_id = request.logged_in_user_id
  user = db.session.get(Users, token_id) #look up whoever the token belongs to (aka whos logged it)
  
  db.session.delete(user)
  db.session.commit()
  return jsonify({"message": f"Successfully deleted user {token_id}"}), 200

#UPDATE A USER
@users_bp.route("", methods=["PUT"])
# @limiter.limit("1 per month")
@token_required
def update_user():
  #Query the user by id
  user_id = request.logged_in_user_id
  user = db.session.get(Users, user_id) #Query for our user to update
  if not user: #Checking if I got a user with that id
    return jsonify({"message": "User not found"}), 404 
  #Validate and Deserialize the updates that they are sending in the body of the request
  try:
    user_data = user_schema.load(request.json)
  except ValidationError as e:
    return jsonify({"message": e.messages}), 400
  # for each of the values that they are sending, we will change the value of the queried object

  user_data["password"] = generate_password_hash(user_data["password"]) #resetting the password key's value, to the hash of the current value

  # if user_data['email']:
  #   user.email = user_data["email"]

  for key, value in user_data.items():
    setattr(user, key, value) #setting object, Attribute, value to replace
  # commit the changes
  db.session.commit()
  # return a response
  return user_schema.jsonify(user), 200