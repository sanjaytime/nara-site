from django.shortcuts import render

# Create your views here.
def beats_index(request):
	return render(request, 'music_index.html')