from django.contrib import admin
from pets_core.models.adopter import Adopter
from pets_core.models.shelter import Shelter
from pets_core.models.pet import Pet

admin.site.register(Adopter)
admin.site.register(Shelter)
admin.site.register(Pet)
