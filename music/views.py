from django.http import Http404
from django.shortcuts import render
from .models import Album

def index(request):
	# grab all the albums from the database and assign them to an object
	all_albums = Album.objects.all()
	
	# provide 'context' to the view that allows it to access to the object holding the data
	context = {"all_albums" : all_albums,}	

	# render the page, while passing it the data
	return render(request, 'music/index.html', context)

def detail(request, album_id):
	try:
		album = Album.objects.get(pk=album_id)
	except Album.DoesNotExist:
		raise Http404(" Album does not exist")
	return render(request, 'music/detail.html', {'album': album})
