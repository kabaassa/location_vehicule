import datetime
from django.db import models


# Create your models here.


class Utilisateur(models.Model):

     #class Meta:
      #   pass
    S = 'secretaire'
    G = 'gerant'
    CAT = {
        S : 'secretaire',
        G : 'gerant'
    }

    M = 'm'
    F = 'f'
    SEXE = {
        M : 'homme',
        F : 'femme'
    }

    nom = models.CharField(max_length=100, null=False)
    prenom = models.CharField(max_length=100, null=False)
    sexe = models.CharField(choices=SEXE.items(), max_length=100,null=False)
    categorie = models.CharField(choices=CAT.items(), max_length=100, null=False, blank=False)
    num_tel = models.IntegerField()
    adresse = models.CharField(max_length=150, null=False, blank=False)
    login = models.CharField(max_length=100,null=False, blank=False)
    password = models.CharField(max_length=100, null=False, blank=False)
    email=models.EmailField(max_length=150,null=False, blank=False)
    desactiver=models.BooleanField(default=False)
    datecreat=models.DateField(default=datetime.date.today)

    def __str__(self):
        return '{} {} {} {} {}'.format(
            self.nom, self.prenom,self.sexe,self.categorie,self.adresse)



class Client(models.Model):
     # class Meta:
    #     pass
    nom=models.CharField(null=False, blank=False,max_length=100)
    prenom=models.CharField(null=False, blank=False,max_length=100)
    num_tel=models.IntegerField(null=False, blank=False)
    adresse=models.CharField(null=False, blank=False,max_length=100)
    num_permis=models.CharField(null=False, blank=False,max_length=100)
    ville=models.CharField(null=False,blank=False, max_length=120)
    date_enreg=models.DateField(default=datetime.date.today)


    def __str__(self):
        return '{} {} {} {} {} {}'.format(
            self.nom, self.prenom, self.num_tel, self.adresse, self.num_permis, self.date_enreg) 


class Vehicule(models.Model):
    # class Meta:
     #     pass
    matricule=models.CharField(max_length=100,null=False, blank=False)
    couleur=models.CharField(max_length=100,null=False, blank=False)
    modele=models.CharField(max_length=100,null=False, blank=False)
    date_enr=models.DateField(default=datetime.date.today)
    montant=models.CharField(max_length=100,null=False, blank=False)
    marque=models.CharField (max_length=100,null=False, blank=False)

    def __str__(self):
       return '{} {} {} {} {} '.format(self.matricule,self.couleur,self.modele,self.montant,self.date_enr)
