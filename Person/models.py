from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def validate_esprit_email(value):
    if not value.endswith("@esprit.tn"):
        raise ValidationError("Email must end with @esprit.tn")


class Person(User):
    cin = models.CharField(
        max_length=8,
        primary_key=True,
        validators=[MinLengthValidator(8)],
    )

    def clean(self):
        super().clean()
        validate_esprit_email(self.email)