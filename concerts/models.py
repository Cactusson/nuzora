from django.db import models
from django.urls import reverse


class Band(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('band_detail', args=[str(self.pk)])


class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('city_detail', args=[str(self.pk)])


class Concert(models.Model):
    GRADE_CHOICES = [(_, _) for _ in range(1, 11)]
    bands = models.ManyToManyField(Band, related_name='concerts', blank=True)
    city = models.ForeignKey(City, related_name='concerts', blank=True)
    date = models.DateField()
    ticket_price = models.PositiveIntegerField(default=0)
    grade = models.PositiveIntegerField(choices=GRADE_CHOICES, default=1)
    text = models.TextField()

    def __str__(self):
        bands = self.get_band_name()
        return '{} - {}'.format(bands, self.date)

    def get_band_amount(self):
        return len(list(self.bands.all()))

    def get_band_name(self):
        if self.bands is not None:
            bands = [str(band) for band in list(self.bands.all())]
        else:
            bands = ['---']
        bands = ', '.join(bands)
        return bands

    def get_absolute_url(self):
        return reverse('concert_detail', args=[str(self.pk)])
