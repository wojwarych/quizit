from django.shortcuts import render
from .models import RankingTennis, RankingLiterature, RankingMusic


def ranking(request):

	tennis_rank_easy = (
		RankingTennis.objects.only('username', 'easyquest').filter(easyquest__isnull=False).
		order_by('-easyquest')[:5])
	tennis_rank_medium = (
		RankingTennis.objects.only('username', 'mediumquest').filter(mediumquest__isnull=False).
		order_by('-mediumquest')[:5])
	tennis_rank_hard = (
		RankingTennis.objects.only('username', 'hardquest').filter(hardquest__isnull=False).
		order_by('-hardquest')[:5])

	literature_rank_easy = (
		RankingLiterature.objects.only('username', 'easyquest').filter(easyquest__isnull=False).
		order_by('-easyquest')[:5])
	literature_rank_medium = (
		RankingLiterature.objects.only('username', 'mediumquest').filter(mediumquest__isnull=False).
		order_by('-mediumquest')[:5])
	literature_rank_hard = (
		RankingLiterature.objects.only('username', 'hardquest').filter(hardquest__isnull=False).
		order_by('-hardquest')[:5])

	music_rank_easy = (
		RankingMusic.objects.only('username', 'easyquest').filter(easyquest__isnull=False).
		order_by('-easyquest')[:5])
	music_rank_medium = (
		RankingMusic.objects.only('username', 'mediumquest').filter(mediumquest__isnull=False).
		order_by('-mediumquest')[:5])
	music_rank_hard = (
		RankingMusic.objects.only('username', 'hardquest').filter(hardquest__isnull=False).
		order_by('-hardquest')[:5])

	context = {
		'tennis_rank_easy': tennis_rank_easy,
		'tennis_rank_medium': tennis_rank_medium,
		'tennis_rank_hard': tennis_rank_hard,
		'literature_rank_easy': literature_rank_easy,
		'literature_rank_medium': literature_rank_medium,
		'literature_rank_hard': literature_rank_hard,
		'music_rank_easy': music_rank_easy,
		'music_rank_medium': music_rank_medium,
		'music_rank_hard': music_rank_hard,
		}

	return render(request, 'ranking/ranking.html', context)