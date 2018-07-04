from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, reverse
from django.utils import timezone
from .models import Player
from .forms import PlayerForm

def listeplayers(request):
	players = Player.objects.filter().order_by('published_date')
	return render(request,'velo/listeplayers.html',{'players':players})


def detailsplayer(request, pk):
	players = get_object_or_404(Player, pk=pk)
	return render(request, 'velo/detailsplayer.html', {'players':players})

def home(request):
	return render(request, 'velo/home.html', {})

def ihome(request):
	return render(request, 'doc/guidons/index.html', {})


def newplayer(request):
	if request.method == "POST":
		form = PlayerForm(request.POST)
		if form.is_valid():
			players = form.save(commit=False)
			players.published_date = timezone.now()
			players.freq = 30
			
			players.save()
			return redirect('detailsplayer', pk=players.pk)
	else:
		form = PlayerForm()
	return render(request, 'velo/newplayer.html', {'form':form})

