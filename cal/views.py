from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, HttpResponseForbidden
from django.http import JsonResponse

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

import json
from django.db.models.query import Prefetch
from django.db import connections

from .forms import AddScoresForm 
from .models import Scores


class Index(View):
	def get(self, request):
		add_score_form = AddScoresForm()
		context = {
			'add_score_form': add_score_form,
		}
		return render(request, "index.html", context)


class AddScore(View):
	def post(self, request):
		if request.is_ajax():
			data = request.POST
		else:
			body = request.body.decode()
			if not body: 
				return JsonResponse ({"response":"Missing Body"})
			data = json.loads(body)

		player = data["player"]
		won = int(data["playerwon"])
		loss = int(data["playerloss"])
		print (player)

		try:
			score = Scores.objects.get(player=player)
			print ("in db")
			score.playerwon += won
			score.playerloss += loss
			score.save()
		except: 
			print ("adding to db")
			form = AddScoresForm(request.POST)
			form.is_valid()
			score = form.save(commit=False)
			score.save()

		if score:
			return JsonResponse({"Message":"added score", "success": True, "id": score.id})
		else:
			return JsonResponse({"success": False})


class ViewTop(View):
	def get(self, request):
		# this line gets the top 50 scores that we have in the db and orders them by top wins
		scores = Scores.objects.filter(show=True).order_by('-playerwon').order_by('playerloss')[:50]
		# put all the values into a json dictionary with a method called from the models
		scores = [score.to_json() for score in scores]
		return JsonResponse({"success": True, 'results': scores})


class ViewAll(View):
	def get(self, request):
		# this line gets the top 50 scores that we have in the db and orders them by top wins
		scores = Scores.objects.filter(show=True).order_by('playerloss').order_by('-playerwon')[:50]
		# put all the values into a json dictionary with a method called from the models
		scores = [score.to_json() for score in scores]
		return JsonResponse({"success": True, 'results': scores})


class EditScore(View):
	def post(self, request):
		if request.is_ajax():
			data = request.POST
		else:
			body = request.body.decode()
			if not body: 
				return JsonResponse ({"response":"Missing Body"})
			data = json.loads(body)

		player = data["player"]
		won = int(data["playerwon"])
		loss = int(data["playerloss"])
		print (player)


		try:
			score = Scores.objects.get(player=player)
			score.playerwon += won
			score.playerloss += loss
			score.save()
			return JsonResponse({"success": True})
		except:
			return JsonResponse({"success": False})




