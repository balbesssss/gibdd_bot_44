"""Проверка, находится ли инспектор в патруле"""

from database.models import User, Patrol


def get_active_patrol(user_id):
    """Проверяет, находится ли инспектор в патруле"""
    inspector = User.get(tg_id=user_id)
    is_patrol = Patrol.get_or_none(
        (Patrol.inspector == inspector) &
        (Patrol.end.is_null())
        )
    return [inspector, is_patrol]
