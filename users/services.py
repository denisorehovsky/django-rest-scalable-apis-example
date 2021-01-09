from users.models import User


def create_user(*_, **user_data) -> User:
    user = User.objects.create_user(**user_data)
    user.email_user(subject='Account has been created.', message='Thanks!')
    return user
