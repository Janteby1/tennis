from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db.models.query import Prefetch
from .models import UserProfile, Events, Organization, Tags, TaggedTag
from django.db import connections

def get_user(username):
	return User.objects.get(username=username)

def get_user_tags(user):
	user_type = ContentType.objects.get_for_model(user)
	tagged_tags = TaggedTag.objects.filter(content_type__pk=user_type.id, object_id=user.id)
	user_tags = [row.tag for row in tagged_tags]
	return user_tags

def main():

	conn = connections['default']
	queries = conn.queries_log

	user = get_user('test')
	# print(vars(user))
	tags = get_user_tags(user)
	print(len(queries))
	queries.clear()
	print("clear",len(queries))
	event_type = ContentType.objects.get_for_model(Events)
	# events_pre = Prefetch(
	# 	'tagged_item',
	# 	to_attr='event',
	# 	queryset=Events.objects.all()
	# )
	matching_events = TaggedTag.objects.filter(
		content_type__pk=event_type.id, 
		tag__id__in=[tag.id for tag in tags]
	).prefetch_related('tagged_item')

	print("after TaggedTag:",len(queries))
	events = [matching_event.tagged_item for matching_event in matching_events]
	print("After matching_events:",len(queries))

	return events, tags, user

if __name__ == '__main__':
	events, tags, user = main()





	