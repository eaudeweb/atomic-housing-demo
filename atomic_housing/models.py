from django.contrib.auth.models import User
from django.contrib import admin
from django.db import models

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
    (0, 'no heating'),
)

(ACCOUNT_NEW,
 ACCOUNT_ACTIVE,
 ACCOUNT_PASSIVE) = range(3)
ACCOUNT_STATUSES = (
    (ACCOUNT_NEW, 'new'),
    (ACCOUNT_ACTIVE, 'active'),
    (ACCOUNT_PASSIVE, 'passive'),
)

(LISTING_NEW,
 LISTING_ACTIVE,
 LISTING_PASSIVE,
 LISTING_OCCUPIED) = range(4)
LISTING_STATUSES = (
    (LISTING_NEW, 'new'),
    (LISTING_ACTIVE, 'active'),
    (LISTING_PASSIVE, 'passive'),
    (LISTING_OCCUPIED, 'occupied'),
)

(CONTRACT_NEW,
 CONTRACT_EXPIRED) = range(2)
CONTRACT_STATUSES = (
    (CONTRACT_NEW, 'new'),
    (CONTRACT_EXPIRED, 'expired')
)

_NATIONALITIES = (
    'Afghan',
    'Albanian',
    'Algerian',
    'American',
    'Andorran',
    'Angolan',
    'Antiguans',
    'Argentinean',
    'Armenian',
    'Australian',
    'Austrian',
    'Azerbaijani',
    'Bahamian',
    'Bahraini',
    'Bangladeshi',
    'Barbadian',
    'Barbudans',
    'Batswana',
    'Belarusian',
    'Belgian',
    'Belizean',
    'Beninese',
    'Bhutanese',
    'Bolivian',
    'Bosnian',
    'Brazilian',
    'British',
    'Bruneian',
    'Bulgarian',
    'Burkinabe',
    'Burmese',
    'Burundian',
    'Cambodian',
    'Cameroonian',
    'Canadian',
    'Cape Verdean',
    'Central African',
    'Chadian',
    'Chilean',
    'Chinese',
    'Colombian',
    'Comoran',
    'Congolese',
    'Congolese',
    'Costa Rican',
    'Croatian',
    'Cuban',
    'Cypriot',
    'Czech',
    'Danish',
    'Djibouti',
    'Dominican',
    'Dominican',
    'Dutch',
    'Dutchman',
    'Dutchwoman',
    'East Timorese',
    'Ecuadorean',
    'Egyptian',
    'Emirian',
    'Equatorial Guinean',
    'Eritrean',
    'Estonian',
    'Ethiopian',
    'Fijian',
    'Filipino',
    'Finnish',
    'French',
    'Gabonese',
    'Gambian',
    'Georgian',
    'German',
    'Ghanaian',
    'Greek',
    'Grenadian',
    'Guatemalan',
    'Guinea-Bissauan',
    'Guinean',
    'Guyanese',
    'Haitian',
    'Herzegovinian',
    'Honduran',
    'Hungarian',
    'I-Kiribati',
    'Icelander',
    'Indian',
    'Indonesian',
    'Iranian',
    'Iraqi',
    'Irish',
    'Irish',
    'Israeli',
    'Italian',
    'Ivorian',
    'Jamaican',
    'Japanese',
    'Jordanian',
    'Kazakhstani',
    'Kenyan',
    'Kittian and Nevisian',
    'Kuwaiti',
    'Kyrgyz',
    'Laotian',
    'Latvian',
    'Lebanese',
    'Liberian',
    'Libyan',
    'Liechtensteiner',
    'Lithuanian',
    'Luxembourger',
    'Macedonian',
    'Malagasy',
    'Malawian',
    'Malaysian',
    'Maldivan',
    'Malian',
    'Maltese',
    'Marshallese',
    'Mauritanian',
    'Mauritian',
    'Mexican',
    'Micronesian',
    'Moldovan',
    'Monacan',
    'Mongolian',
    'Moroccan',
    'Mosotho',
    'Motswana',
    'Mozambican',
    'Namibian',
    'Nauruan',
    'Nepalese',
    'Netherlander',
    'New Zealander',
    'Ni-Vanuatu',
    'Nicaraguan',
    'Nigerian',
    'Nigerien',
    'North Korean',
    'Northern Irish',
    'Norwegian',
    'Omani',
    'Pakistani',
    'Palauan',
    'Panamanian',
    'Papua New Guinean',
    'Paraguayan',
    'Peruvian',
    'Polish',
    'Portuguese',
    'Qatari',
    'Romanian',
    'Russian',
    'Rwandan',
    'Saint Lucian',
    'Salvadoran',
    'Samoan',
    'San Marinese',
    'Sao Tomean',
    'Saudi',
    'Scottish',
    'Senegalese',
    'Serbian',
    'Seychellois',
    'Sierra Leonean',
    'Singaporean',
    'Slovakian',
    'Slovenian',
    'Solomon Islander',
    'Somali',
    'South African',
    'South Korean',
    'Spanish',
    'Sri Lankan',
    'Sudanese',
    'Surinamer',
    'Swazi',
    'Swedish',
    'Swiss',
    'Syrian',
    'Taiwanese',
    'Tajik',
    'Tanzanian',
    'Thai',
    'Togolese',
    'Tongan',
    'Trinidadian or Tobagonian',
    'Tunisian',
    'Turkish',
    'Tuvaluan',
    'Ugandan',
    'Ukrainian',
    'Uruguayan',
    'Uzbekistani',
    'Venezuelan',
    'Vietnamese',
    'Welsh',
    'Welsh',
    'Yemenite',
    'Zambian',
    'Zimbabwean',
)
NATIONALITIES = zip(_NATIONALITIES, _NATIONALITIES)

_DISTRICTS = (
    'District 1',
    'District 2',
)
DISTRICTS = zip(_DISTRICTS, _DISTRICTS)

_MUNICIPALITIES = (
    'Municipality 1',
    'Municipality 2',
)
MUNICIPALITIES = zip(_MUNICIPALITIES, _MUNICIPALITIES)


class Landlord(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    status = models.IntegerField(choices=ACCOUNT_STATUSES)
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
    status = models.IntegerField(choices=ACCOUNT_STATUSES)
    registered = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=255)
    nationality = models.CharField(choices=NATIONALITIES, max_length=32)

    def __unicode__(self):
        return u"{} {}".format(self.first_name, self.last_name)


class Listing(models.Model):
    owner = models.ForeignKey(User)
    status = models.IntegerField(choices=LISTING_STATUSES, default=LISTING_NEW)
    posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # info
    address_city = models.CharField(max_length=255)
    address_address = models.CharField(max_length=255)
    address_zipcode = models.CharField(max_length=10)
    address_district = models.CharField(max_length=32, choices=DISTRICTS)
    address_municipality = models.CharField(max_length=32,
                                            choices=MUNICIPALITIES)
    accomodation = models.IntegerField(choices=ACCOMODATION_TYPES)
    availability = models.DateField(blank=True, default=None)
    year = models.IntegerField()
    size = models.IntegerField()
    outdoor = models.IntegerField(choices=OUTDOOR_TYPES, blank=True)
    outdoor_size = models.IntegerField(blank=True)
    rooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField()
    toilets = models.IntegerField()
    bedrooms = models.IntegerField()
    floor = models.IntegerField()
    elevator = models.NullBooleanField(blank=True)
    parking = models.IntegerField(choices=PARKING_TYPES, blank=True)
    furnished = models.BooleanField(default=False)
    heating = models.IntegerField(choices=HEATING_TYPES)
    heating_emission = models.FloatField(blank=True)
    lease = models.IntegerField(choices=LEASE_TYPES)
    rent = models.IntegerField()
    deposit = models.IntegerField()

    @property
    def title(self):
        return u"{rooms} rooms {type}".format(
            rooms=self.rooms, type=self.get_accomodation_display()
        )

    @property
    def address(self):
        return u"{} {} {}".format(
            self.address_zipcode, self.address_address, self.address_city,
        )

    def __unicode__(self):
        return u"{} in {}".format(self.title, self.address)


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
