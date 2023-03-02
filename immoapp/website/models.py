from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms.widgets import RadioSelect


class User(AbstractUser):
    profile_photo = models.ImageField(verbose_name='Photo de profil')
    
class Prediction(models.Model):
    YEAR_CHOICES = (
        ('pre1950', 'Avant 1950'),
        ('1950_to_1975', '1950 à 1975'),
        ('1975_to_1997', '1975 à 1997'),
        ('1997_to_2015', '1997 à 2015')
    )
    ZIPCODES = [
        98103, 98038, 98115, 98052, 98117, 98042, 98034, 98118, 98023, 98006,
        98133, 98059, 98058, 98155, 98074, 98033, 98027, 98125, 98056, 98053,
        98001, 98075, 98126, 98092, 98144, 98106, 98116, 98029, 98004, 98199,
        98065, 98122, 98146, 98008, 98028, 98040, 98198, 98003, 98031, 98072,
        98168, 98112, 98055, 98107, 98136, 98178, 98030, 98177, 98166, 98022,
        98105, 98045, 98002, 98077, 98011, 98019, 98108, 98119, 98005, 98007,
        98188, 98032, 98014, 98070, 98109, 98102, 98010, 98024, 98148, 98039
    ]
    
    CHOICES = [(1, 'Oui'), (0, 'Non')]
    
    VIEW_CHOICES = (
        (0, '0 - Sans intérêt'),
        (1, '1 - Moyenne'),
        (2, '2 - Agréable'),
        (3, '3 - Belle'),
        (4, '4 - Exceptionnelle')
    )
    
    CONDITION_CHOICES = (
        (1, '1 - Mauvais état'),
        (2, '2 - État moyen'),
        (3, '3 - Bon état'),
        (4, '4 - Très bon état'),
        (5, '5 - Neuf')
    )
    
    QUALITY_CHOICES = [(i, str(i)) for i in range(1, 14)]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(verbose_name='Adresse', max_length=255, null=True, blank=True)
    zipcode = models.IntegerField(verbose_name='Code Postal', choices=[(zipcode, zipcode) for zipcode in sorted(ZIPCODES)], default=98001)
    bedrooms = models.IntegerField(verbose_name='Nombre de chambres')
    bathrooms = models.FloatField(verbose_name='Nombre de salles de bain')
    m2_living = models.FloatField(verbose_name='Surface habitable (m²)')
    m2_above = models.FloatField(verbose_name='Surface habitable à l\'étage (m²)')
    has_basement = models.IntegerField(verbose_name='Sous-sol', choices=CHOICES, default=CHOICES[1])
    m2_lot = models.FloatField(verbose_name='Surface du terrain (m²)')
    floors = models.FloatField(verbose_name='Nombre d\'étages')
    waterfront = models.IntegerField(verbose_name='Vue mer', choices=CHOICES, default=CHOICES[1])
    view = models.IntegerField(verbose_name='Note de la vue', choices=VIEW_CHOICES, validators=[MinValueValidator(0), MaxValueValidator(4)], default=0)
    condition = models.IntegerField(verbose_name='Condition', choices=CONDITION_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    grade = models.IntegerField(verbose_name='Note de qualité', choices=QUALITY_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(13)], default=1)
    yr_built = models.CharField(verbose_name='Année de construction', max_length=12, choices=YEAR_CHOICES, default=YEAR_CHOICES[0])
    was_renovated = models.IntegerField(verbose_name='Rénové', choices=CHOICES, default=CHOICES[1])
    predicted_price = models.IntegerField(null=True, blank=True)

