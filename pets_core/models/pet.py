from django.db import models
from pets_core.constants.enums import PetCategory, PetSize, PetGender, PetStatus
from pets_core.models.shelter import Shelter
from pets_core.models.adopter import Adopter


class Pet(models.Model):
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
    PetStatus_Choice = (
        (PetStatus.AVAILABLE.value, PetStatus.AVAILABLE.value),
        (PetStatus.ADOPTED.value, PetStatus.ADOPTED.value)
    )
    pet_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    age = models.IntegerField(blank=True, null=True)
    pet_category = models.CharField(max_length=20, choices=PetCategory_Choice, default=None, null=True)
    pet_size = models.CharField(max_length=20, choices=PetSize_Choice, default=None, null=True)
    gender = models.CharField(max_length=20, choices=PetGender_Choice, default=None, null=True)
    status = models.CharField(max_length=20, choices=PetStatus_Choice, blank=True, null=True)
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE, related_name='pets', blank=True, null=True)
    adopter = models.ForeignKey(Adopter, on_delete=models.CASCADE, related_name='pets', blank=True, null=True)

    def __str__(self):
        return self.name
