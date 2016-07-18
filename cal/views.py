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

from .forms import UserForm, UserLoginForm, AddEventForm, OrgForm 
from .models import UserProfile, Events, Organization, Tags, TaggedTag


# Create your views here.
class Landing(View):
	def get(self, request):
		return render(request, "landing.html")

class Index(View):
	def get(self, request):
		user_creation_form = UserForm()
		user_login_form = UserLoginForm()
		org_creation_form = OrgForm()
		add_event_form = AddEventForm()

		context = {
			'user_creation_form': user_creation_form,
			'user_login_form': user_login_form,
			"org_creation_form": org_creation_form,
			"add_event_form": add_event_form,
		}
		return render(request, "index.html", context)


class User_Register(View):
	def post(self, request):
		if request.is_ajax():
			data = request.POST
		else:
			body = request.body.decode()
			if not body: 
				return JsonResponse ({"response":"Missing Body"})
			data = json.loads(body)

		user_form = UserForm(data)
		if user_form.is_valid():
			user = user_form.save()
			return JsonResponse({"Message": "Register succesfull", "success": True})
		else:
			return JsonResponse ({"response":"Invalid information", 'success' : False, 'errors': user_form.errors })


class User_Login(View):
	def post(self, request):
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			request.session.set_expiry(30000)
			return JsonResponse({"username":user.username, "success": True})
		else:
			return JsonResponse({'errors': form.errors})


class Org_Register(View):
	def post(self, request):
		if request.is_ajax():
			data = request.POST
		else:
			body = request.body.decode()
			if not body: 
				return JsonResponse ({"response":"Missing Body"})
			data = json.loads(body)

		if request.user.is_authenticated():
			form = OrgForm(request.POST)
			form.is_valid()
			# add the user to each organization 
			user = request.user
			org = form.save(commit=False)
			org.admin = user
			org.save()
			return JsonResponse({"Message":"added organization", "success": True})
		else:
			return JsonResponse({"success": False})


class Logout(View):
	def post(self, request):
		print(request)
		logout(request) # django built in logout 
		return JsonResponse ({"Message":"Logout Successful"})


class AddEvent(View):
	def post(self, request):
		# checks to make sure the user is logged in 
		if request.user.is_authenticated():
			form = AddEventForm(request.POST)
			form.is_valid()
			# add the user to each post 
			user = request.user
			event = form.save(commit=False)
			event.creator = user
			event.save()
			return JsonResponse({"Message":"added event", "success": True, "id": event.id})
		else:
			return JsonResponse({"success": False})


class ViewAll(View):
	def get(self, request):
		# this line gets the top 25 events that we have in the db and orders them by top votes
		events = Events.objects.filter(show=True).order_by('-created_at')[:25]
		# put all the values into a json dictionary with a method called from the models
		events = [event.to_json() for event in events]
		# print (events)
		return JsonResponse({"success": True, 'results': events})


class Delete_Event(View):
	def post(self, request, events_id=None):
		event = Events.objects.get(id=events_id)

		if request.user.is_authenticated():
			event.show = False
			event.save()
			return JsonResponse({"success": True})
		else:
			return JsonResponse({"success": False})


class Vote_Up_Event(View):
	def post(self, request, events_id=None):
		event = Events.objects.get(id=events_id)

		if request.user.is_authenticated():
			event.vote += 1
			event.save()
			return JsonResponse({"success": True})
		else:
			return JsonResponse({"success": False})


class Vote_Down_Event(View):
	def post(self, request, events_id=None):
		event = Events.objects.get(id=events_id)

		if request.user.is_authenticated():
			event.vote -= 1
			event.save()
			return JsonResponse({"success": True})
		else:
			return JsonResponse({"success": False})


class AddTags(View):
	def post(self, request, event_id=None):
		# get the tags 
		tag_names = request.POST.getlist('tag')
		tags = Tags.objects.filter(name__in=tag_names)

		# get the event 
		event = Events.objects.get(id=event_id)

		for tag in tags: 
			TaggedTag.objects.create(
				tag = tag,
				tagged_item = event
			)
		return JsonResponse({"success": True, "Message":"added tags", 'data': dict(request.POST)})


class My_Events(View):
	def get_user_tags(self, user):
		# this gets the user type
		user_type = ContentType.objects.get_for_model(user)
		# returns all the rows and tags that match the users type and id 
		tagged_tags = TaggedTag.objects.filter(
			content_type__pk=user_type.id, 
			object_id=user.id
		)
		
		user_tags = [row.tag for row in tagged_tags]
		return user_tags

	def get_events(self, tags):
		# this gets the event type
		event_type = ContentType.objects.get_for_model(Events)

		# returns all the rows that match the event type and tag ids 
		matching_events = TaggedTag.objects.filter(
			content_type__pk=event_type.id, 
			tag__id__in=[tag.id for tag in tags]
		).prefetch_related('tagged_item')#.order_by('-created_at')

		events = [matching_event.tagged_item for matching_event in matching_events]
		return events

	def get(self, request):
		user = request.user
		try: 
			tags = self.get_user_tags(user)
			events = self.get_events(tags)
			# makes all the events json 
			events = [event.to_json() for event in events]
			return JsonResponse({"success": True, 'results': events})
		except:
			return JsonResponse({"success": False})


class My_Tags(View):
	def post(self, request, event_id=None):
		# get the tags 
		tag_names = request.POST.getlist('tag')
		tags = Tags.objects.filter(name__in=tag_names)

		# get the user 
		user = request.user

		for tag in tags: 
			TaggedTag.objects.create(
				tag = tag,
				tagged_item = user
			)
		return JsonResponse({"success": True, "Message":"added tags", 'data': dict(request.POST)})


class RSVP(View):
	def post(self, request, event_id=None):
		event = Events.objects.get(id=event_id)

		if request.user.is_authenticated():
			event.rsvp += 1
			event.save()
			return JsonResponse({"success": True})
		else:
			return JsonResponse({"success": False})





