import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key_9583453'