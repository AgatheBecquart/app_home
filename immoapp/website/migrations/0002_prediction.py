# Generated by Django 4.1.6 on 2023-02-24 20:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bedrooms', models.IntegerField(verbose_name='Nombre de chambres')),
                ('bathrooms', models.FloatField(verbose_name='Nombre de salles de bain')),
                ('m2_living', models.FloatField(verbose_name='Surface habitable (m²)')),
                ('m2_lot', models.FloatField(verbose_name='Surface du terrain (m²)')),
                ('floors', models.FloatField(verbose_name="Nombre d'étages")),
                ('waterfront', models.IntegerField(choices=[(1, 'Oui'), (0, 'Non')], verbose_name='Vue mer')),
                ('view', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)], verbose_name='Note de la vue')),
                ('condition', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Condition')),
                ('grade', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(13)], verbose_name='Note de qualité')),
                ('m2_above', models.FloatField(verbose_name="Surface habitable à l'étage (m²)")),
                ('yr_built', models.CharField(choices=[('pre1950', 'Avant 1950'), ('1950_to_1975', '1950 à 1975'), ('1975_to_1997', '1975 à 1997'), ('1997_to_2015', '1997 à 2015')], max_length=12, verbose_name='Année de construction')),
                ('zipcode', models.IntegerField(choices=[(98001, 98001), (98002, 98002), (98003, 98003), (98004, 98004), (98005, 98005), (98006, 98006), (98007, 98007), (98008, 98008), (98010, 98010), (98011, 98011), (98014, 98014), (98019, 98019), (98022, 98022), (98023, 98023), (98024, 98024), (98027, 98027), (98028, 98028), (98029, 98029), (98030, 98030), (98031, 98031), (98032, 98032), (98033, 98033), (98034, 98034), (98038, 98038), (98039, 98039), (98040, 98040), (98042, 98042), (98045, 98045), (98052, 98052), (98053, 98053), (98055, 98055), (98056, 98056), (98058, 98058), (98059, 98059), (98065, 98065), (98070, 98070), (98072, 98072), (98074, 98074), (98075, 98075), (98077, 98077), (98092, 98092), (98102, 98102), (98103, 98103), (98105, 98105), (98106, 98106), (98107, 98107), (98108, 98108), (98109, 98109), (98112, 98112), (98115, 98115), (98116, 98116), (98117, 98117), (98118, 98118), (98119, 98119), (98122, 98122), (98125, 98125), (98126, 98126), (98133, 98133), (98136, 98136), (98144, 98144), (98146, 98146), (98148, 98148), (98155, 98155), (98166, 98166), (98168, 98168), (98177, 98177), (98178, 98178), (98188, 98188), (98198, 98198), (98199, 98199)], verbose_name='Code Postal')),
                ('has_basement', models.IntegerField(choices=[(1, 'Oui'), (0, 'Non')], verbose_name='Sous-sol')),
                ('was_renovated', models.IntegerField(choices=[(1, 'Oui'), (0, 'Non')], verbose_name='Rénové')),
            ],
        ),
    ]
