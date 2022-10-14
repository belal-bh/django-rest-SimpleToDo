import email
from django.contrib.auth import get_user_model

User = get_user_model()

def get_normalized_username(user_name):
    username = user_name.strip()
    return username

def generate_email_from_username(username):
    username = get_normalized_username(username)
    words = username.split(' ')
    email = "_".join(words) + "@example.com"
    return email

def get_or_create_user(user_name):
    username = get_normalized_username(user_name)
    email = generate_email_from_username(username)
    return User.objects.get_or_create(username=username, email=email)

def get_user_or_none(user_name):
    username = get_normalized_username(user_name)
    try:
        user = User.objects.get(username=username)
    except:
        return None
    return user
