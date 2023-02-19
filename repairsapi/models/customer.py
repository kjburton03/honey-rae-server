from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """

    # Relationship to the built-in User model which has name and email
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional address field to capture from the client
    address = models.CharField(max_length=155)

    @property
    def full_name(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return f'{self.user.first_name} {self.user.last_name}'
        