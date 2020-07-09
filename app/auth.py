from flask import request
from functools import wraps
import jwt
from .config import Config
from .models import User


def require_auth(func):
  @wraps(func)
  def wrapped(*args, **kwargs):
    access_token = request.headers.get('Authorization', None)
    print(request.headers)
    if not access_token:
      return {'error': 'authentication required'}, 401
    try:
      decoded = jwt.decode(access_token, Config.SECRET_KEY)
      print("Decoded:", decoded)
      user = User.query.filter(User.email == decoded.get('email')).first()
      print("Auth Success!")
      return {'message': "Authorization Sucessful"}
    except:
      return {'error': 'invalid auth token'}, 401
    return func(*args, **kwargs)
  return wrapped
