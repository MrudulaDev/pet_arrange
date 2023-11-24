from django.contrib.auth.models import AbstractUser
from django.db import models
from pets_core.constants.enums import PetCategory, PetSize, PetGender


class Adopter(models.Model):
    PetCategory_Choice = (
        (PetCategory.DOG.value, PetCategory.DOG.value),
        (PetCategory.CAT.value, PetCategory.CAT.value),
        (PetCategory.PARROT.value, PetCategory.PARROT.value),
        (PetCategory.RABBIT.value, PetCategory.RABBIT.value),
        (PetCategory.OTHERS.value, PetCategory.OTHERS.value)
    )
    PetSize_Choice = (
        (PetSize.SMALL.value, PetSize.SMALL.value),
        (PetSize.MEDIUM.value, PetSize.MEDIUM.value),
        (PetSize.LARGE.value, PetSize.LARGE.value),
    )
    PetGender_Choice = (
        (PetGender.MALE.value, PetGender.MALE.value),
        (PetGender.FEMALE.value, PetGender.FEMALE.value)
    )
    user_id = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    preferred_pet_category = models.CharField(max_length=20, choices=PetCategory_Choice, default=None, null=True)
    preferred_pet_size = models.CharField(max_length=20, choices=PetSize_Choice, default=None, null=True)
    preferred_pet_gender = models.CharField(max_length=20, choices=PetGender_Choice, default=None, null=True)

    def __str__(self):
        return self.name
