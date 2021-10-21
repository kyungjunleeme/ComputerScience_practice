from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from accounts.models import Phone

import pyotp

from twilio.rest import Client as TwilioClient
import pyotp
from hello_async.settings import base


account_sid = base.account_sid
auth_token = base.auth_token
twilio_phone = base.twilio_phone

client = TwilioClient(account_sid, auth_token)

User = get_user_model()


def generate_key():
    key = pyotp.random_base32()
    if is_unique(key):
        return key
    generate_key()


def is_unique(key):
    try:
        Phone.objects.get(key=key)
    except Phone.DoesNotExist:
        return True
    return False


@receiver(pre_save, sender=Phone)
def create_key(sender, instance, **kwargs):
    if not instance.key:
        instance.key = generate_key()
        time_otp = pyotp.TOTP(instance.key, interval=300)
        time_otp = str(time_otp.now())
        raw_input = instance.number.__dict__["raw_input"]
        if raw_input.startswith("010"):
            preprocess_input = raw_input.lstrip("0")
            raw_input = "+82" + preprocess_input
        else:
            pass
        client.messages.create(
            body="Your verification code is " + time_otp,
            from_=twilio_phone,
            to=raw_input,
        )
