from django.http import HttpResponse, Http404
from django.template import loader

from django.shortcuts import render, get_object_or_404			#important

from .models import Album, Song



def index1(request):		#old format  -- traditional, way to render html
	all_albums = Album.objects.all()
	html = ''
	for album in all_albums:
		url = '/music/'+str(album.id)+ '/'
		html += '<a href="'+url+'">'+album.album_title+'</a><br/>'
	return HttpResponse(html)

def index2(request):			# old way of using htmlrespomse 
	all_albums = Album.objects.all()
	template = loader.get_template('music/index.html')
	context = {'all_albums':all_albums}
	return HttpResponse(template.render(context, request))

def index(request):
	all_albums = Album.objects.all()
	context = {'all_albums':all_albums}
	return render(request, 'music/index.html', context)

def detail1(request, album_id):			# old way of htmlrespomse
	return HttpResponse(''+str(album_id))

def detail2(request, album_id):			# old and lengthy way to call 404
	try:
		album = Album.objects.get(pk=album_id)
		context = {'album':album}
	except Album.DoesNotExist:
		raise Http404("Album does not exist")
	return render(request, 'music/detail.html', context)

def detail(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	context = {'album':album}
	return render(request, 'music/detail.html', context)

def favorite(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	try:
		selected_song = album.song_set.get(pk=request.POST['song'])
	except:
		return render(request, 'music/detail.html', {
			'album': album,
			'error_message':'Song Does not exists',
			})
	else:
		selected_song.is_favorite = True
		selected_song.save()
		return render(request, 'music/detail.html', {'album': album})
