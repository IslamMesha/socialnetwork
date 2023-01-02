import requests
from django.conf import settings
from rest_framework.exceptions import ValidationError

api_key = settings.ABSTRACT_API_KEY


def is_valid_email(data):
    return (
        data["is_valid_format"]["value"]
        and data["is_smtp_valid"]["value"]
        and data["deliverability"] == "DELIVERABLE"
    )


def validate_email(email):
    api_url = "https://emailvalidation.abstractapi.com/v1/?api_key=" + api_key
    response = requests.get(api_url + "&email=" + email).json()
    is_valid = is_valid_email(response)
    if not is_valid:
        raise ValidationError("Enter a valid email address.")
    return email


def get_user_country(ip):
    # Handel retries requests
    api_url = "https://ipgeolocation.abstractapi.com/v1/?api_key=" + api_key
    response = requests.get(api_url + "&ip_address=" + ip).json()
    return response["country"]


def get_user_holidays(user):
    api_url = "https://holiday.abstractapi.com/v1/?api_key=" + api_key
    response = requests.get(
        f"{api_url}&country={user.country}&year={user.created_at.year}"
        f"&month={user.created_at.month}&day={user.created_at.day}"
    ).json()
    return response["name"]
