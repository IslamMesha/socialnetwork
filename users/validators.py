from django.conf import settings
from rest_framework.exceptions import ValidationError

from users.utils import retry_session

ABSTRACT_EMAIL_API_KEY = settings.ABSTRACT_EMAIL_API_KEY
ABSTRACT_HOLIDAY_API_KEY = settings.ABSTRACT_HOLIDAY_API_KEY
ABSTRACT_GEOLOCATION_API_KEY = settings.ABSTRACT_GEOLOCATION_API_KEY


def is_valid_email(data):
    return (
        data["is_valid_format"]["value"]
        and data["is_smtp_valid"]["value"]
        and data["deliverability"] == "DELIVERABLE"
    )


def validate_email(email):
    session = retry_session(retries=5)
    api_url = (
        "https://emailvalidation.abstractapi.com/v1/?api_key=" + ABSTRACT_EMAIL_API_KEY
    )
    response = session.get(api_url + "&email=" + email).json()
    is_valid = is_valid_email(response)
    if not is_valid:
        raise ValidationError("Enter a valid email address.")
    return email


def get_user_country(ip):
    ip = "156.206.168.188"
    session = retry_session(retries=5)
    api_url = (
        "https://ipgeolocation.abstractapi.com/v1/?api_key="
        + ABSTRACT_GEOLOCATION_API_KEY
    )
    response = session.get(api_url + "&ip_address=" + ip).json()
    return response["country_code"]


def get_user_holidays(user):
    session = retry_session(retries=5)
    api_url = "https://holidays.abstractapi.com/v1/?api_key=" + ABSTRACT_HOLIDAY_API_KEY
    response = session.get(
        f"{api_url}&country={user.country}&year={user.created_at.year}"
        f"&month={user.created_at.month}&day={user.created_at.day}"
    ).json()
    return [holiday["name"].split(",") for holiday in response]
