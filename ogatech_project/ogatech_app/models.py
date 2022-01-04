from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from shop.models.address import BaseShippingAddress, ISO_3166_CODES, BaseBillingAddress, CountryField
# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    # additional classes
    phone_regex = RegexValidator(regex='', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=20, blank=True) # validators should be a list

    address1 = models.CharField(
        _("Address line 1"),
        max_length=1024,
    )

    address2 = models.CharField(
        _("Address line 2"),
        max_length=1024,
        blank=True,
        null=True,
    )

    zip_code = models.CharField(
        _("ZIP / Postal code"),
        max_length=12,
    )

    city = models.CharField(
        _("City"),
        max_length=1024,
    )

    country = CountryField(_("Country"))

    def __str__(self):
        return self.user.username


# class AddressModelOtech(models.Model):
#     user_shipping = models.OneToOneField(User, related_name='shipping_address', blank=False, null=True, on_delete=models.DO_NOTHING)   
#     # user_billing = models.OneToOneField(User, related_name='billing_address', blank=True, null=True, on_delete=models.DO_NOTHING)

#     address1 = models.CharField(
#         _("Address line 1"),
#         max_length=1024,
#     )

#     address2 = models.CharField(
#         _("Address line 2"),
#         max_length=1024,
#         blank=True,
#         null=True,
#     )

#     zip_code = models.CharField(
#         _("ZIP / Postal code"),
#         max_length=12,
#     )

#     city = models.CharField(
#         _("City"),
#         max_length=1024,
#     )

#     country = CountryField(_("Country"))

    # class Meta:
    #     verbose_name = _("Shipping Address")
#       verbose_name_plural = _("Shipping Addresses")


# class ShippingAddress(BaseShippingAddress, AddressModelOtech):
#     user_shipping = models.OneToOneField(User, related_name='shipping_address', blank=False, null=True, on_delete=models.DO_NOTHING)
#     class Meta:
#         verbose_name = _("Shipping Address")
#         verbose_name_plural = _("Shipping Addresses")


# class BillingAddress(BaseBillingAddress, AddressModelOtech):
#     class Meta:
#         verbose_name = _("Billing Address")
#         verbose_name_plural = _("Billing Addresses")
