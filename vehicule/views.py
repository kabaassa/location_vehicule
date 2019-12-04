# from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from vehicule.forms import ClientForm, UserCreationForm, VehiculeForm
from vehicule.models import Client, Utilisateur, Vehicule


@login_required
def index(request):
    return render(request, 'base.html', {})


@login_required
def listveh(request):
    return render(request, 'listveh.html', {})


@login_required
def navgerant(request):
    return render(request, 'navgerant.html', {})


@login_required
def login(request):
    return render(request, 'login.html', {})


@login_required
def home(request):
    ctx = {'my_name': 'KABA', 'data': [8, 3, 5, 9, 'Totote']}

    return render(request, 'home.html', ctx)


@login_required
def users(request):
    cxt = {}
    ut = Utilisateur.objects.all()
    cxt.update({'ut': ut})

    utilisateur_form = UserCreationForm()
    if request.method == 'POST':
        utilisateur_form = UserCreationForm(request.POST)
        if utilisateur_form.is_valid():
            utilisateur_form.save()
            return redirect('users')
            # do something.
    cxt.update({'form': utilisateur_form})
    return render(request, 'users.html', cxt)


@login_required
def desactivate_user(request, username):
    user = Utilisateur.objects.get(username=username)
    user.is_active = False
    user.save()
    return redirect('users')


@login_required
def activate_user(request, username):
    user = Utilisateur.objects.get(username=username)
    user.is_active = True
    user.save()
    return redirect('users')


@login_required
def edit_user(request, username):
    user = Utilisateur.objects.get(username=username)
    user.is_active = False
    user.save()
    return redirect('users')


@login_required
def creatclt(request):
    cxt = {}
    clt = Client.objects.all()
    cxt.update({'clt': clt})

    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        if client_form.is_valid():
            client_form.save()
            return redirect('creatclt')
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
