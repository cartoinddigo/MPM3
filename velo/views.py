from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, reverse
from django.utils import timezone
from .models import Player
from .forms import PlayerForm
import csv
from django.http import HttpResponse


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

def excsv(request):
	from django.utils.encoding import smart_str
	from django.template import Context, loader
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="export.csv"'
	writer = csv.writer(response, csv.excel)
	response.write(u'\ufeff'.encode('utf8'))
	
	writer.writerow([
        smart_str(u"entrep"),
        smart_str(u"nom"),
        smart_str(u"ville"),
		smart_str(u"nbsal"),
        smart_str(u"freq"),
		smart_str(u"dist"),
        smart_str(u"access"),
        smart_str(u"ctxgeolib"),
		smart_str(u"pccycliste"),
        smart_str(u"g1"),
        smart_str(u"g2"),
        smart_str(u"g3"),
		smart_str(u"g4"),
		smart_str(u"PM"),
		smart_str(u"pvelo"),
		smart_str(u"score"),
    ])

	players = Player.objects.all()
	for p in players:
		writer.writerow([
			smart_str(p.entrep),
			smart_str(p.nom),
			smart_str(p.ville),
			smart_str(p.nbsal),
			smart_str(p.freq),
			smart_str(p.dist),
			smart_str(p.access),
			smart_str(p.ctxgeolib),
			smart_str(p.pccycliste),
			smart_str(p.g1),
			smart_str(p.g2),
			smart_str(p.g3),
			smart_str(p.g4),
			smart_str(p.PM),
			smart_str((p.pvelo()/p.nbsal)*100),
			smart_str(p.score()),
		])




	return response

def export(request):
	from .resources import Playerexp
	player_ex = Playerexp()
	dataset = player_ex.export()
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = 'attachment; filename="palyer_export.xls"'
	return response


