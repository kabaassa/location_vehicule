from django import forms
from django.forms.models import inlineformset_factory
from django.contrib.auth.forms import ReadOnlyPasswordHashField
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from vehicule.models import (
    Utilisateur, Client, Vehicule, Location, LocationItem)


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        exclude = []
        fields = '__all__'


class LocationItemForm(forms.ModelForm):
    class Meta:
        model = LocationItem
        exclude = ()
        fields = '__all__'

LocationItemFormSet = inlineformset_factory(
    Location, LocationItem,
    fields=(
        'vehicule',
        'location',
        'date_retour',
        'montant',),
    extra=10,
    can_delete=False,)


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'num_tel': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control'}),
            'num_docu': forms.TextInput(attrs={'class': 'form-control'}),
        }
        fields = [
            'nom',
            'prenom',
            'num_tel',
            'adresse',
            'num_docu',
        ]


class VehiculeForm(forms.ModelForm):
    class Meta:
        model = Vehicule
        fields = [
            'modele',
            'marque',
            'matricule',
            'couleur',
        ]
        exclude = ['date_enr']


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Utilisateur
        fields = ('__all__')
        exclude = ('datecreat', 'password')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Utilisateur
        fields = ('username', 'password', 'is_active', 'is_admin')
        exclude = ('datecreat', )

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
