from datetime import datetime, date
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)

# Create your models here.
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UtilisateurManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username, date of
        birth and password.
        """
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Utilisateur(AbstractBaseUser):

    S = 'secretaire'
    G = 'gerant'
    CAT = {
        S: 'secretaire',
        G: 'gerant'
    }

    M = 'm'
    F = 'f'
    SEXE = {
        M: 'homme',
        F: 'femme'
    }

    username = models.SlugField("Nom d'utilisateur", max_length=100, null=False, unique=True)
    nom = models.CharField(max_length=100, null=True, blank=True)
    prenom = models.CharField("Prénoms", max_length=100, null=True, blank=True)
    sexe = models.CharField("Sexe", choices=SEXE.items(), max_length=10)
    categorie = models.CharField("Catégorie", choices=CAT.items(), max_length=100)
    num_tel = models.IntegerField("Téléphone")
    adresse = models.CharField("Adresse", max_length=150, null=True, blank=True)
    datecreat = models.DateTimeField(default=datetime.now)
    email = models.EmailField("E-mail", max_length=255, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UtilisateurManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Client(models.Model):

    class Meta:
        pass

    nom=models.CharField(null=False, blank=False,max_length=100)
    prenom=models.CharField(null=False, blank=False,max_length=100)
    num_tel=models.IntegerField(null=False, blank=False)
    adresse=models.CharField(null=False, blank=False,max_length=100)
    num_permis=models.CharField(null=False, blank=False,max_length=100)
    ville=models.CharField(null=False,blank=False, max_length=120)
    date_enreg=models.DateField(default=date.today)

    def __str__(self):
        return '{} {} {} {} {} {}'.format(
            self.nom, self.prenom, self.num_tel, self.adresse, self.num_permis,
            self.date_enreg)


class Vehicule(models.Model):
    # class Meta:
     #     pass
    matricule=models.CharField(max_length=100,null=False, blank=False)
    couleur=models.CharField(max_length=100,null=False, blank=False)
    modele=models.CharField(max_length=100,null=False, blank=False)
    date_enr=models.DateField(default=date.today)
    montant=models.CharField(max_length=100,null=False, blank=False)
    marque=models.CharField(max_length=100,null=False, blank=False)

    def __str__(self):
        return '{} {} {} {} {} '.format(
            self.matricule,self.couleur,self.modele,self.montant,self.date_enr)