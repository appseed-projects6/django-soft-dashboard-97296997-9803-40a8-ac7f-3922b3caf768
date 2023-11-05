# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Etudiant(models.Model):

    #__Etudiant_FIELDS__
    nom_prenom = models.CharField(max_length=255, null=True, blank=True)
    num_inscription = models.CharField(max_length=255, null=True, blank=True)

    #__Etudiant_FIELDS__END

    class Meta:
        verbose_name        = _("Etudiant")
        verbose_name_plural = _("Etudiant")


class Mention(models.Model):

    #__Mention_FIELDS__
    nom_mention = models.CharField(max_length=255, null=True, blank=True)

    #__Mention_FIELDS__END

    class Meta:
        verbose_name        = _("Mention")
        verbose_name_plural = _("Mention")


class Option(models.Model):

    #__Option_FIELDS__
    nom_option = models.CharField(max_length=255, null=True, blank=True)

    #__Option_FIELDS__END

    class Meta:
        verbose_name        = _("Option")
        verbose_name_plural = _("Option")



#__MODELS__END
