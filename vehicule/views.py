from django.http import HttpResponse 
from django.shortcuts import render
from django.shortcuts import redirect
from vehicule.forms import  ClientForm, UtilisateurForm, VehiculeForm
from vehicule.models import Client, Utilisateur, Vehicule

def index(request):
    return render(request, 'base.html', {})

def listveh(request):
    return render(request, 'listveh.html', {})

def navgerant(request):
    return render(request, 'navgerant.html', {})

def login(request):
    return render(request, 'login.html', {})

def home(request):
	ctx = {'my_name': 'KABA', 'data': [8, 3, 5, 9, 'Totote']}

	return render(request, 'home.html', ctx)

def users(request):
    cxt={}
    ut = Utilisateur.objects.all()
    cxt.update({'ut': ut})
    print('FFF')
    if request.method == 'POST':
        print('POST')
        utilisateur_form = UtilisateurForm(request.POST)
        if utilisateur_form.is_valid():
            print('is valide')
            utilisateur_form.save()
            print('is save')
            redirect('enrvehicule')
            # do something.
    else:
        utilisateur_form = UtilisateurForm()
    cxt.update({'form': utilisateur_form})
    return render(request, 'users_.html', cxt)

def creatclt(request):
    cxt={}
    clt = Client.objects.all()
    cxt.update({'clt': clt})

    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        if client_form.is_valid():
           client_form.save()
            # do something.
    else:
        client_form = ClientForm()
    cxt.update({'form': client_form})
    return render(request, 'creatclt.html', cxt)

def enrvehicule(request):
    cxt={}
    veh = Vehicule.objects.all()
    cxt.update({'veh': veh})

    if request.method == 'POST':
        vehicule_form = VehiculeForm(request.POST)
        if vehicule_form.is_valid():
           vehicule_form.save()
            # do something.
    else:
        vehicule_form = VehiculeForm()
    cxt.update({'form': vehicule_form})
    return render(request,'enrvehicule.html',cxt)

def listveh(request):
    return render(request,'listveh.html', {})

