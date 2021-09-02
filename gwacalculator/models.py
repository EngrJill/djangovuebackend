from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

class Subjs(models.Model):
  subjectName = models.CharField(max_length=200)
  equivalentUnits = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
  grades = models.FloatField(null=True, blank=True, default=None)
  semester = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)])
  year = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])
  course = models.CharField(max_length=200)
  created_at = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
    return self.subjectName
  class Meta:
    verbose_name_plural = "Subjects"
