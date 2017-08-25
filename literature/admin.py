from django.contrib import admin
from .models import EasyQuest, MediumQuest, HardQuest
# Register your models here.

models = [EasyQuest, MediumQuest, HardQuest]

for i in models:

	admin.site.register(i)