from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, reverse, render
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
import csv

from django.utils import timezone
from .forms import LstAction, CatAction
from .models import Site, Action

def home(request):
	return render(request, 'action/home.html',)

def sites_liste(request):
	sites = Site.objects.filter()
	return render(request, 'action/sites_list.html', {'sites':sites})


def site_detail(request, pk):
	site = get_object_or_404(Site, pk=pk)
	return render(request, 'action/site_detail.html', {'site': site})


def lstdetail(request):
	res = Site.objects.filter()
	return render(request, 'action/listesite.html', {'res':res})



def nouveau_site(request):
	if request.method == "POST":
		form = LstAction(request.POST)
		if form.is_valid():
			obj = Site()
			obj.nom = form.cleaned_data['nom']
			obj.lstaction = form.cleaned_data['lstaction']
			obj.save()
			return redirect('site_detail', pk=obj.pk)
	else:
		form = LstAction()
	return render(request, 'action/site_nouveau.html', {'form':form})

def delete_site(DeleteView):
	model = Site
	success_url = reverse_lazy('sites_liste')
	template_name = 'site_delete.html'

def catalogue_liste(request):
	actions = Action.objects.filter()
	return render(request, 'action/catalogue_list.html', {'actions':actions})


def catalogue_detail(request, pk):
	action = get_object_or_404(Action, pk=pk)
	return render(request, 'action/catalogue_detail.html', {'action': action})

def nouveau_catalogue(request):
	if request.method == "POST":
		form = CatAction(request.POST)
		if form.is_valid():
			obj = Action()
			obj.nomfiche = form.cleaned_data['nomfiche']
			obj.catenjeux = form.cleaned_data['catenjeux']
			obj.codecouleur = form.cleaned_data['codecouleur']
			obj.numfiche = form.cleaned_data['numfiche']
			obj.typeaction = form.cleaned_data['typeaction']
			obj.constat = form.cleaned_data['constat']
			obj.objectif = form.cleaned_data['objectif']
			obj.ccible = form.cleaned_data['ccible']
			obj.objmoyen = form.cleaned_data['objmoyen']
			obj.factreu = form.cleaned_data['factreu']
			obj.porteur = form.cleaned_data['porteur']
			obj.intervenant = form.cleaned_data['intervenant']
			obj.planning = form.cleaned_data['planning']
			obj.impacts = form.cleaned_data['impacts']
			obj.indicateurs = form.cleaned_data['indicateurs']
			obj.indicateurs_tp = form.cleaned_data['indicateurs_tp']
			obj.cinvestdet = form.cleaned_data['cinvestdet']
			obj.cinvestchi = form.cleaned_data['cinvestchi']
			obj.cfonctiondet = form.cleaned_data['cfonctiondet']
			obj.cfonctionchi = form.cleaned_data['cfonctionchi']
			obj.periodicite = form.cleaned_data['periodicite']
			obj.tellmemore = form.cleaned_data['tellmemore']
			obj.save()
			return redirect('catalogue_detail', pk=obj.pk)
	else:
		form = CatAction()
	return render(request, 'action/catalogue_nouveau.html', {'form':form})

def batch_catalogue(request):
	with open('catimport.csv') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=';',)
		for row in reader:
			obj = Action()
			obj.nomfiche = row['nomfiche']
			obj.catenjeux = row['catenjeux']
			obj.codecouleur = row['codecouleur']
			obj.numfiche = row['numfiche']
			obj.save()
		return render(request, 'action/catalogue_list.html', {'actions':actions})
