from __future__ import annotations

from peewee import fn

from config import ADMINS
from models.user import User


def count_users() -> int:
    query = User.select(fn.COUNT(User.id))
    return query.scalar()

def get_user_ids():
    query = User.select(User.id)

    return list(query)

def get_users() -> list[User]:
    query = User.select()

    return list(query)


def get_user(id: int) -> User:
    return User.get_or_none(User.id == id)


def update_user(user: User, username: str = None) -> User:
    user.username = username
    if user.id in ADMINS:
        user.is_admin = True
    user.save()

    return user


def create_user(id: int, username: str = None) -> User:
    new_user = User.create(id=id, username=username)

    if id in ADMINS:
        new_user.is_admin = True
        new_user.save()

    return new_user


def get_or_create_user(
    id: int, username: str = None
) -> User:
    user = get_user(id)

    if user:
        user = update_user(user, username)

        return user

    return create_user(id, username)

def delete_user(id: int):
    user = get_user(id)
    return user.delete_instance()