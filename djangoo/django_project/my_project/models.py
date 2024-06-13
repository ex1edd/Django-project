from django.db import models

class Owner(models.Model):
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.full_name}"

class Pet(models.Model):
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=20)
    age = models.IntegerField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type}; {self.name}; {self.sex}; {self.age}; {self.owner.full_name}; {self.owner.phone_number}"



