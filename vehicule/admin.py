from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from vehicule.forms import UserChangeForm, UserCreationForm
from vehicule.models import (
    Utilisateur, Client, Vehicule)
# Register your models here.
# from django import forms
# from django.contrib import admin
from django.contrib.auth.models import Group
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UtilisateurAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('nom', 'prenom', 'sexe', 'adresse', 'num_tel')}),
        ('Permissions', {'fields': ('is_admin',)}),
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

# Now register the new UserAdmin...
admin.site.register(Utilisateur, UtilisateurAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
# admin.site.unregister(Group)


# @admin.register(Utilisateur)
# class UtilisateurAdmin(BaseUserAdmin):

#     list_display = ('nom', 'prenom','sexe','categorie','adresse',)


@admin.register(Client)
class Client(admin.ModelAdmin):

    list_display = ('nom', 'prenom', 'num_tel', 'adresse', 'date_enreg', 'num_permis',)


@admin.register(Vehicule)
class Vehicule(admin.ModelAdmin):
    list_display = ('matricule', 'couleur', 'model', 'montant', 'marque',)
