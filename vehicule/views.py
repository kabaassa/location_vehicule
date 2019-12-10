# from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from vehicule.forms import (
    ClientForm, UserCreationForm, VehiculeForm, LocationForm, LocationItemFormSet)
from vehicule.models import Client, Location, LocationItem, Utilisateur, Vehicule


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
    vehicules = Vehicule.objects.all()
    vehicules_d = vehicules.filter(status=Vehicule.D)
    vehicules_e = vehicules.filter(status=Vehicule.E)
    vehicules_em = vehicules.filter(status=Vehicule.EM)
    v_dispo_count = vehicules_d.count()
    v_en_location_count = vehicules_e.count()
    v_en_maintenance_count = vehicules_em.count()
    ctx = {
        'vehicules_d': vehicules_d,
        'vehicules_e': vehicules_e,
        'vehicules_em': vehicules_em,
        'v_dispo_count': v_dispo_count,
        'v_en_location_count': v_en_location_count,
        'v_en_maintenance_count': v_en_maintenance_count,
    }
    return render(request, 'home.html', ctx)


@login_required
def location(request):
    locations = Location.objects.all()
    location = Location()
    location_form = LocationForm(instance=location) # setup a form for the parent

    if request.method == "POST":
        location_form = LocationForm(request.POST)
        formset = LocationItemFormSet(request.POST, request.FILES)

        if location_form.is_valid():
            created_location = location_form.save(commit=False)
            formset = LocationItemFormSet(request.POST, request.FILES, instance=created_location)

            if formset.is_valid():
                created_location.save()
                formset.save()
                return redirect("location")
    else:
        location_form = LocationForm(instance=location)
        formset = LocationItemFormSet()

    return render(request, "add_location.html", {
        "location_form": location_form,
        "locations": locations,
        "formset": formset,
    })


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
def cahnge_status_vh(request, status, id):
    vh = Vehicule.objects.get(id=id)
    vh.status = status
    vh.save()
    return redirect('enrvehicule')


@login_required
def creatclt(request):
    cxt = {}
    clt = Client.objects.all()
    cxt.update({'clt': clt})

    if request.method == 'POST' and 'location' in request.POST:
        location_form = LocationForm(request.POST)
        if location_form.is_valid():
            location_form.save()
            return redirect('creatclt')
    else:
        location_form = LocationForm()
    cxt.update({'location_form': location_form})

    if request.method == 'POST' and 'client' in request.POST:
        client_form = ClientForm(request.POST)
        if client_form.is_valid():
            client_form.save()
            return redirect('creatclt')
    else:
        client_form = ClientForm()
    cxt.update({'form': client_form})
    return render(request, 'creatclt.html', cxt)


def enrvehicule(request):
    cxt = {}
    veh = Vehicule.objects.all()
    cxt.update({'veh': veh})

    if request.method == 'POST':
        vehicule_form = VehiculeForm(request.POST)
        if vehicule_form.is_valid():
            vehicule_form.save()
            return redirect('enrvehicule')
    else:
        vehicule_form = VehiculeForm()
    cxt.update({'form': vehicule_form, "status": Vehicule.STATUS.items()})
    return render(request, 'enrvehicule.html', cxt)
