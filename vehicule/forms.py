from django import forms
from vehicule.models import Utilisateur, Client, Vehicule



class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        print(dir(forms))
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'num_tel': forms.NumberInput(attrs={'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control'}),
            'login': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'categorie': forms.Select (attrs={'class': 'form-control'}),
            'sexe': forms.Select (attrs={'class': 'form-control'}),
            

        }
        fields = [
        'nom',
        'prenom',
        'sexe',
        'categorie',
        'num_tel',
        'adresse',
        'login',
        'password',
        'email',
        ] 

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}), 
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'num_tel': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control'}), 
            'num_permis': forms.TextInput(attrs={'class': 'form-control'}), 
        }
        fields = [
        'nom',
        'prenom',
        'num_tel',
        'adresse',
        'num_permis',
        ] 


class VehiculeForm(forms.ModelForm):
    class Meta:
        model = Vehicule
        widgets = {
            'matricule': forms.TextInput(attrs={'class': 'form-control'}),
            'couleur' : forms.TextInput(attrs={'class': 'form-control'}),
            'modele' : forms.TextInput(attrs={'class': 'form-control'}),
            'montant' : forms.TextInput(attrs={'class': 'form-control'}),
            'marque': forms.TextInput(attrs={'class': 'form-control'}),
        }
        fields = [
        'matricule',
        'couleur',
        'modele',
        'montant',
        'marque',
        ] 

class loginForm(forms.ModelForm):
    class Meta:
        model = Vehicule
        widgets = {
            'login': forms.TextInput(attrs={'class': 'form-control'}),
            'password' : forms.TextInput(attrs={'class': 'form-control'}),
        }
        fields = [
        
        ]   