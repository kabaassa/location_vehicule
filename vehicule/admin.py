from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from vehicule.forms import UserChangeForm, UserCreationForm
from vehicule.models import (Utilisateur, Client, Vehicule, Location, LocationItem)
# Register your models here.
# from django import forms
# from django.contrib import admin
from django.contrib.auth.models import Group


class UtilisateurAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'is_admin')
    list_filter = ('is_admin', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('nom', 'prenom', 'sexe', 'adresse', 'num_tel')}),
        ('Permissions', {'fields': ('is_admin', 'categorie')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'nom', 'prenom', 'sexe', 'adresse', 'num_tel',
                       'categorie', 'password1', 'password2')}),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

admin.site.register(Utilisateur, UtilisateurAdmin)
# admin.site.register(Location)
# admin.site.register(LocationItem)


class LocationItemInline(admin.TabularInline):
    model = LocationItem


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = [
        LocationItemInline,
    ]


# @admin.register(LocationItem)
# class LocationItem(admin.ModelAdmin):
#     # fields = ['__all__']
#     # exclude = []

#     model = LocationItem
#     # inlines = [
#     #     LocationInline,
#     # ]


@admin.register(Client)
class Client(admin.ModelAdmin):

    list_display = ('nom', 'prenom', 'num_tel', 'adresse', 'date_enr', 'num_docu',)


@admin.register(Vehicule)
class Vehicule(admin.ModelAdmin):
    list_display = ('__str__', 'status', )
