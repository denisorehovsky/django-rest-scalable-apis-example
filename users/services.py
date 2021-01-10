from users.models import User


def create_user(*_, **user_data) -> User:
    user = User.objects.create_user(**user_data)
    user.email_user(subject='Account has been created.', message='Thanks!')
    return user


def delete_user(*, user: User):
    user.delete()


def update_user(*, user: User, password=None, **user_data) -> User:
    for attr, value in user_data.items():
        setattr(user, attr, value)

    if password is not None:
        user.set_password(password)

    user.save()
    return user
