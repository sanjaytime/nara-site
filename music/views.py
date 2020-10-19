from django.shortcuts import render

# Create your views here.
def music_index(request):
	return render(request, 'music_index.html')