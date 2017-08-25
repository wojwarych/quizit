from django.contrib import admin
from .models import RankingTennis, RankingLiterature, RankingMusic

models = [RankingTennis, RankingLiterature, RankingMusic]

for i in models:

	admin.site.register(i)