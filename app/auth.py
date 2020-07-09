from flask import request
from functools import wraps
import jwt
from .config import Config
from .models.users import User


def require_auth(func):
  @wraps(func)
  def wrapped(*args, **kwargs):
    access_token = request.headers.get('Authorization', None)
    print(access_token)
    if not access_token:
      return {'error': 'authentication required'}, 401
    try:
      decoded_jwt = jwt.decode(access_token, Config.SECRET_KEY)
      print("Decoded:", decoded_jwt)
      user = User.query.filter(User.email == decoded_jwt.get('email')).first()
      print("Auth Success!")
    except:
      return {'error': 'invalid auth token'}, 401
    return func(*args, **kwargs)
  return wrapped
