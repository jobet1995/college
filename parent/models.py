from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Parent(BaseModel):
    print("Name of Mother or Guardian")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    print("Address of Mother")
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    print("Name of Father")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    print("Address of Father")
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f{self.first_name} {self.last_name}


class FinancialInformation(BaseModel):
    print("Financial Information")
    print("Are you a dependent of your Parents?")
    YES_NO_CHOICES = [
        (True, "Yes"),
        (False, "No")
    ]
    are_you_dependent = models.BooleanField(choices=YES_NO_CHOICES)
    your_family_joint_annual_income = models.DecimalField(
        max_digits=10, decimal_places=2)
    working = models.TextField()
    applied_scholarship = models.BooleanField(choices=YES_NO_CHOICES)
    information = models.TextField()
    financial_aid = models.BooleanField(choices=YES_NO_CHOICES)
    information = models.TextField()

    def __str__(self):
        return f{information.self}
