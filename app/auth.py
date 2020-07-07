from flask import request
from functools import wraps
import jwt
from .config import Config
from .models import User


def require_auth(func):
  @wraps(func)
  def wrapped(*args, **kwargs):
    access_token = request.headers.get('Authorization', None)
    if not access_token:
      return {'error': 'authentication required'}, 401
    try:
      decoded = jwt.decode(access_token, Configuration.SECRET_KEY)
      user = User.query.filter(User.email == decoded.get('email')).first()
    except:
      return {'error': 'invalid auth token'}, 401
    return func(*args, **kwargs)
  return wrapped
