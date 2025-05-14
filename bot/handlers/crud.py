import databes.models as models


def create_user_profile (    
    tg_id : int | None = None,
    username : str | None = None,
    last_name : str | None = None,
    first_name : str | None = None,
    telephone : int | None = None
    ):
    user = models.User.get_or_create(
        tg_id = tg_id,
        username = username,
        last_name = last_name,
        first_name = first_name,
        telephone = telephone
    )
    return user