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
		pass
	# 	# checks to make sure the user is logged in 
	# 	if request.user.is_authenticated():
	# 		form = AddEventForm(request.POST)
	# 		form.is_valid()
	# 		# add the user to each post 
	# 		user = request.user
	# 		event = form.save(commit=False)
	# 		event.creator = user
	# 		event.save()
	# 		return JsonResponse({"Message":"added event", "success": True, "id": event.id})
	# 	else:
	# 		return JsonResponse({"success": False})


class ViewTop(View):
	def get(self, request):
		pass
	# 	# this line gets the top 25 events that we have in the db and orders them by top votes
	# 	events = Events.objects.filter(show=True).order_by('-created_at')[:25]
	# 	# put all the values into a json dictionary with a method called from the models
	# 	events = [event.to_json() for event in events]
	# 	# print (events)
	# 	return JsonResponse({"success": True, 'results': events})

