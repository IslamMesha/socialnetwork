from socialnetwork.celery import app
from users.models import User
from users.validators import get_user_country, get_user_holidays


@app.task
def enrich_geolocation_data(user_pk):
    # Enrich user geolocation data
    user = User.objects.get(pk=user_pk)
    if user.ipaddress:
        user.country = get_user_country(user.ipaddress)
        user.holidays = get_user_holidays(user)
        user.save()
