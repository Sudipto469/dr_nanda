from django.db import models
from django.contrib.auth.models import User


# Create your models here.
'''
This stores the doctors 
'''
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    description = models.TextField(null=True, blank=True)
    specialization = models.TextField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.rating)

class Hospital(models.Model):
    # fees = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    product = models.ManyToManyField(Product, related_name='hospitals',through='HospitalFee')
    image = models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    hospital_name = models.CharField(max_length=200, null=True, blank=True)
    hospital_address = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.hospital_name)

class Lab(models.Model):
    product = models.ManyToManyField(Product, related_name='labs')
    image = models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    lab_name = models.CharField(max_length=200, null=True, blank=True)
    lab_address = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True, editable=False)
    def __str__(self):
        return str(self.lab_name)

class Clinic(models.Model):
    product = models.ManyToManyField(Product, related_name='clinic')
    image = models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    clinic_name = models.CharField(max_length=200, null=True, blank=True)
    clinic_address = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.clinic_name)

class Disease(models.Model):
    product = models.ManyToManyField(Product, related_name='diseases')
    hospital = models.ManyToManyField(Hospital, related_name='diseases')
    lab = models.ManyToManyField(Lab, related_name='diseases')
    clinic = models.ManyToManyField(Clinic, related_name='diseases')
    disease_name = models.CharField(max_length=200, null=True, blank=True)
    disease_symptoms = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.disease_name)


class HospitalFee(models.Model):
        product_id = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="hospitalfees")
        hospital_id = models.ForeignKey(Hospital, on_delete=models.CASCADE,related_name="hospitalfees")
        fees = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
        createdAt = models.DateTimeField(auto_now_add=True)
        id = models.AutoField(primary_key=True, editable=False)

        class Meta:
            unique_together = [['product_id', 'hospital_id']]
        def __str__(self):
            return str(self.fees)

class ClinicFee(models.Model):
        product_id = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="clinicfees")
        clinic_id = models.ForeignKey(Clinic, on_delete=models.CASCADE,related_name="clinicfees")
        fees = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
        createdAt = models.DateTimeField(auto_now_add=True)
        id = models.AutoField(primary_key=True, editable=False)

        class Meta:
            unique_together = [['product_id', 'clinic_id']]
        def __str__(self):
            return str(self.fees)

class LabFee(models.Model):
        product_id = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="labfees")
        lab_id = models.ForeignKey(Lab, on_delete=models.CASCADE,related_name="labfees")
        fees = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
        createdAt = models.DateTimeField(auto_now_add=True)
        id = models.AutoField(primary_key=True, editable=False)

        class Meta:
            unique_together = [['product_id', 'lab_id']]
        def __str__(self):
            return str(self.fees)
