from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class Users(AbstractUser):
    ROLE_CHOICES = (
        ("attendee","Attendee"),
        ("organizer","Organizer"),
    )
    
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20,default="attendee",choices=ROLE_CHOICES)
    
    def __str__(self):
        return self.username

class Profile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    profile_image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )

    bio = models.TextField(
        blank=True
    )

    phone_number = models.CharField(
        max_length=15,
        blank=True
    )

    city = models.CharField(
        max_length=100,
        blank=True
    )

    country = models.CharField(
        max_length=100,
        blank=True
    )

    linkedin_url = models.URLField(
        blank=True
    )

    facebook_url = models.URLField(
        blank=True
    )

    instagram_url = models.URLField(
        blank=True
    )

    allow_networking = models.BooleanField(
        default=False
    )

    preferred_categories = models.JSONField(
        default=list,
        blank=True
    )

    organisation_name = models.CharField(
        max_length=255,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.user.username} Profile"