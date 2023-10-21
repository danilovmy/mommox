from django.db import models

from django.contrib.auth.models import AbstractUser, UserManager
from settings import translator as _


class CustomerManager(UserManager):

    @classmethod
    def normalize_email(cls, email):
        return super().normalize_email(email).lower()

    def create_user(self, email, *args, **kwargs):
        return super().create_user(email, email, *args, **kwargs)

    def create_superuser(self, email, *args, **kwargs):
        return super().create_superuser(email, email, *args, **kwargs)


class Customer(AbstractUser):
    """ Abstract service customer."""
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    email = models.EmailField(_("email address"), null=False, blank=False, unique=True)
    username = models.CharField(_('username, not used'), max_length=255, blank=True, null=False)

    objects = CustomerManager()


class Seller(Customer):
    """ User who sell something """

    class Meta:
        proxy = True
        verbose_name = _("Seller")
        verbose_name_plural = _("Sellers")


class Visitor(Customer):
    """ User who simply visited the shop"""

    class Meta:
        proxy = True
        verbose_name = _("Shop Visitor")
        verbose_name_plural = _("Shop Visitors")
