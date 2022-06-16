from django.db import models

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Cricketer(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    matches_played = models.IntegerField(default=0)
    match_allowance = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)


    def __str__(self):
        return "%s %s %s" %(self.first_name, self.last_name, self.phone)