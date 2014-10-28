from django.contrib.auth.models import User
from django.contrib import admin
from django.db import models
from atomic_housing import definitions

ACCOMODATION_TYPES = (
    (0, 'Apartment'),
    (1, 'Single House'),
    (2, 'Duplex'),
    (3, 'Other'),
)

OUTDOOR_TYPES = (
    (0, 'Garden'),
    (1, 'Terrace'),
    (2, 'Balcony'),
)

PARKING_TYPES = (
    (2, 'No Parking'),
    (0, 'Private'),
    (1, 'Garage'),
)

LEASE_TYPES = (
    (0, 'short term'),
    (1, '3 year contract'),
    (2, '5 year contract'),
    (3, 'unlimited'),
)

HEATING_TYPES = (
    (0, 'Gas Central Heating'),
    (1, 'House Central Heating'),
    (2, 'City/Alternate Central Heating'),
)

(ACCOUNT_NEW,
 ACCOUNT_ACTIVE,
 ACCOUNT_PASSIVE,
 ACCOUNT_TERMINATED) = range(4)
ACCOUNT_STATUSES = (
    (ACCOUNT_NEW, 'new'),
    (ACCOUNT_ACTIVE, 'active'),
    (ACCOUNT_PASSIVE, 'passive'),
    (ACCOUNT_TERMINATED, 'terminated'),
)

(LISTING_NEW,
 LISTING_INACTIVE,
 LISTING_ACTIVE,
 LISTING_PASSIVE,
 LISTING_OCCUPIED,
) = range(5)
LISTING_STATUSES = (
    (LISTING_NEW, 'new'),
    (LISTING_INACTIVE, 'modified'),
    (LISTING_ACTIVE, 'active'),
    (LISTING_PASSIVE, 'passive'),
    (LISTING_OCCUPIED, 'occupied'),
)

(CONTRACT_NEW,
 CONTRACT_ACTIVE,
 CONTRACT_EXPIRED) = range(3)
CONTRACT_STATUSES = (
    (CONTRACT_NEW, 'new'),
    (CONTRACT_ACTIVE, 'active'),
    (CONTRACT_EXPIRED, 'expired')
)


class Landlord(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    status = models.IntegerField(choices=ACCOUNT_STATUSES, default=ACCOUNT_NEW)
    registered = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=255)

    def __unicode__(self):
        return u"{} {}".format(self.first_name, self.last_name)


class Customer(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    status = models.IntegerField(choices=ACCOUNT_STATUSES, default=ACCOUNT_NEW)
    registered = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=255)
    nationality = models.CharField(choices=definitions.NATIONALITIES,
                                   max_length=32)

    favorites = models.ManyToManyField('Listing', blank=True)

    def __unicode__(self):
        return u"{} {}".format(self.first_name, self.last_name)


class Listing(models.Model):
    owner = models.ForeignKey(User)
    status = models.IntegerField(choices=LISTING_STATUSES, default=LISTING_NEW)
    posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # info
    description = models.TextField(blank=True)
    address_city = models.CharField(max_length=255)
    address_address = models.CharField(max_length=255)
    address_zipcode = models.CharField(max_length=10)
    address_district = models.CharField(max_length=32,
                                        choices=definitions.DISTRICTS)
    accomodation = models.IntegerField(choices=ACCOMODATION_TYPES)
    availability = models.DateField(null=True, blank=True, default=None)
    year = models.IntegerField('Building Year')
    size = models.IntegerField(help_text='Square meters')
    outdoor = models.IntegerField(choices=OUTDOOR_TYPES, null=True, blank=True)
    outdoor_size = models.IntegerField(null=True, blank=True)
    rooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField()
    toilets = models.IntegerField()
    bedrooms = models.IntegerField()
    floor = models.IntegerField()
    elevator = models.BooleanField(blank=True, default=False)
    parking = models.IntegerField(choices=PARKING_TYPES, null=True, blank=True)
    furnished = models.BooleanField(default=False)
    heating = models.IntegerField(choices=HEATING_TYPES, null=True, blank=True)
    heating_emission = models.FloatField(blank=True, default=None, null=True)
    lease = models.IntegerField(choices=LEASE_TYPES)
    rent = models.IntegerField()
    rent_vat = models.BooleanField(default=False)
    rent_maintenance = models.IntegerField(default=0)
    deposit = models.IntegerField()

    @property
    def title(self):
        return u"{accomodation}, {rooms} {no_rooms}".format(
            accomodation=self.get_accomodation_display(),
            rooms=self.rooms,
            no_rooms= 'rooms' if (self.rooms > 1) else 'room'
        )

    @property
    def accomodation_type(self):
        return u"{}".format(self.get_accomodation_display())

    @property
    def lease_type(self):
        return u"{}".format(self.get_lease_display())

    @property
    def address(self):
        return u"{}, {} - {}, {}".format(
            self.address_address, 
            self.address_district, 
            self.address_zipcode, 
            self.address_city
        )

    @property
    def landlord(self):
        return self.owner.landlord

    @property
    def cover_photo(self):
        if self.photos.count():
            return self.photos.all()[0]
        return None

    def __unicode__(self):
        return u"{} in {}".format(self.title, self.address)


class ListingPhoto(models.Model):

    listing = models.ForeignKey(Listing, related_name='photos')
    name = models.ImageField(upload_to='listing')


class Contract(models.Model):
    status = models.IntegerField(choices=CONTRACT_STATUSES,
                                 default=CONTRACT_NEW)
    listing = models.ForeignKey(Listing)
    customer = models.ForeignKey(Customer)
    awarded = models.DateTimeField(auto_now_add=True)


admin.site.register(Listing)
admin.site.register(Landlord)
admin.site.register(Customer)
admin.site.register(Contract)
admin.site.register(ListingPhoto)
