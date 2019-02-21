from django.db import models


# Create your models here.
# Mom model
class Mom(models.Model):
    mom_first_name = models.CharField(max_length=40)
    mom_last_name = models.CharField(max_length=40)
    mom_phone_number = models.CharField(max_length=14)

    def __str__(self):
        return f'{self.mom_first_name} {self.mom_last_name}'

#Child model
class Child(models.Model):
    child_first_name = models.CharField(max_length=40)
    child_last_name = models.CharField(max_length=40)
    child_mom = models.ForeignKey(Mom, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.child_first_name} {self.child_last_name}'
