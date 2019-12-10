from datetime import datetime, date
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UtilisateurManager(BaseUserManager):
    def create_user(self, username, password=None):
        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Utilisateur(AbstractBaseUser):

    A = 'admin'
    S = 'secretaire'
    G = 'gerant'
    CAT = {
        S: 'secretaire',
        G: 'gerant',
        A: 'Administrateur'
    }

    M = 'm'
    F = 'f'
    SEXE = {
        M: 'homme',
        F: 'femme'
    }

    username = models.SlugField(
        "Nom d'utilisateur", max_length=100, null=False, unique=True)
    nom = models.CharField(max_length=100, null=True, blank=True)
    prenom = models.CharField("Prénoms", max_length=100, null=True, blank=True)
    sexe = models.CharField("Sexe", choices=SEXE.items(), max_length=10)

    categorie = models.CharField(
        "Catégorie", choices=CAT.items(), max_length=100)
    num_tel = models.IntegerField("Téléphone")
    adresse = models.CharField(
        "Adresse", max_length=200, null=True, blank=True)
    datecreat = models.DateTimeField(default=datetime.now, null=True)
    email = models.EmailField(
        "E-mail", max_length=255, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UtilisateurManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

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

    def del_url(self):
        return reverse("del_path", args=[self.username])

    def edit_url(self):
        return reverse("edit_path", args=[self.username])

    def active_url(self):
       return reverse("active_path", args=[self.username])


class Client(models.Model):

    class Meta:
        pass

    user = models.ForeignKey(
        "Utilisateur", blank=True, null=True, verbose_name="Utilisateur",
        on_delete=models.CASCADE)
    nom = models.CharField(null=False, blank=False, max_length=100)
    prenom = models.CharField(null=False, blank=False, max_length=100)
    num_tel = models.IntegerField(null=False, blank=False)
    adresse = models.CharField(null=False, blank=False, max_length=100)
    num_docu = models.CharField(null=False, blank=False, max_length=100)
    localite = models.CharField(null=False, blank=False, max_length=120)
    date_enr = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return '{} {} {} {} {} {}'.format(
            self.nom, self.prenom, self.num_tel, self.adresse, self.num_docu,
            self.date_enr)


class Vehicule(models.Model):

    D = 'disponible'
    E = 'en_location'
    EM = "en_maintenance"
    H = "hors_service"
    STATUS = {
        D: 'Disponible',
        E: 'En Location',
        EM: "En Maintenance",
        H: "En Hors Service"
    }
    matricule = models.CharField("Matricule", max_length=100, unique=False)
    marque = models.CharField("Marque", max_length=100, null=False, blank=False)
    modele = models.CharField("Modele", max_length=100, null=False, blank=False)
    couleur = models.CharField("Couleur", max_length=100, null=False, blank=False)
    date_enr = models.DateField(default=date.today)
    update_date = models.DateTimeField(default=datetime.now)
    status = models.CharField(
        "Statut", choices=STATUS.items(), default=D, max_length=80)

    def label_status(self):
        return self.STATUS.get(self.status)

    def display(self):
        return '{}-{}'.format(self.marque, self.modele)

    # Recuperation de la date de retour du vehicule s'il est en location
    def date_de_retour(self):
        try:
            last_location = LocationItem.objects.filter(
                vehicule=self).latest('location__date_locat')
            return last_location.date_retour
        except Exception as e:
            return None

    def __str__(self):
        return '{} {} {} {}'.format(
            self.modele, self.marque, self.couleur, self.matricule)


class Location(models.Model):
    client = models.ForeignKey(
        "Client", blank=True, null=True, verbose_name="Client",
        on_delete=models.CASCADE)
    date_locat = models.DateField("Date de location")
    localite = models.CharField(null=False, blank=False, max_length=100)

    def __str__(self):
        return'{} {} {}'.format(
            self.date_locat, self.localite, self.client)


class LocationItem(models.Model):
    vehicule = models.ForeignKey(
        "Vehicule", blank=True, null=True, verbose_name="Vehicule",
        on_delete=models.CASCADE)
    location = models.ForeignKey(
        "Location", blank=True, null=True, verbose_name="Locations",
        on_delete=models.CASCADE)
    date_retour = models.DateField()
    montant = models.IntegerField()

    def __str__(self):
        return'{} {} {}'.format(
            self.location, self.date_retour, self.vehicule)


class Facture(models.Model):

    # class Meta:
    #     pass
    location = models.ForeignKey(
        "Location", blank=True, null=True, verbose_name="Location",
        on_delete=models.CASCADE)
    client = models.ForeignKey(
        "Client", blank=True, null=True, verbose_name="Client",
        on_delete=models.CASCADE)
    date_edit = models.DateField()

    def __str__(self):
        return'{} {} {} '.format(self.date_edit, self.location, self.client)
