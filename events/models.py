from django.db import models
from accounts.models import Users

# Create your models here.


class Event(models.Model):

    CATEGORY_CHOICES = (
        ("technical", "Technical"),
        ("sports", "Sports"),
        ("cultural", "Cultural"),
        ("speech", "Speech"),
        ("workshop", "Workshop"),
    )

    MODE_CHOICES = (
        ("online", "Online"),
        ("offline", "Offline"),
        ("hybrid", "Hybrid"),
    )

    organizer = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="organized_events")

    title = models.CharField(max_length=255)

    slug = models.SlugField(unique=True)

    description = models.TextField()

    ai_knowledge = models.TextField(blank=True)

    event_logo = models.ImageField(upload_to="event_logos/",blank=True,null=True)

    banner_image = models.ImageField(upload_to="event_banners/",blank=True,null=True)

    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES)

    mode = models.CharField(max_length=20,choices=MODE_CHOICES)

    venue = models.CharField(max_length=255,blank=True)

    city = models.CharField(max_length=100,blank=True)

    start_date = models.DateField()

    end_date = models.DateField()

    start_time = models.TimeField()

    end_time = models.TimeField()

    chief_guest = models.CharField(max_length=255,blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class TicketTier(models.Model):

    TICKET_TYPE_CHOICES = (
        ("free", "Free"),
        ("paid", "Paid"),
    )

    event = models.ForeignKey(Event,on_delete=models.CASCADE,related_name="ticket_tiers")

    name = models.CharField(max_length=100)

    ticket_type = models.CharField(max_length=20,choices=TICKET_TYPE_CHOICES,default="free")

    price = models.DecimalField(max_digits=10,decimal_places=2,default=0)

    capacity = models.PositiveIntegerField()

    sold_count = models.PositiveIntegerField(default=0)

    description = models.TextField(blank=True)

    early_bird_price = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)

    early_bird_end_date = models.DateTimeField(blank=True,null=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event.title} - {self.name}"
    
class Registration(models.Model):

    STATUS_CHOICES = (
        ("registered", "Registered"),
        ("checked_in", "Checked In"),
        ("cancelled", "Cancelled"),
    )

    attendee = models.ForeignKey(Users,on_delete=models.CASCADE,related_name="registrations")

    event = models.ForeignKey(Event,on_delete=models.CASCADE)

    ticket_tier = models.ForeignKey(TicketTier,on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)

    total_price = models.DecimalField(max_digits=10,decimal_places=2)

    qr_code = models.ImageField(upload_to="qr_codes/",blank=True,null=True)

    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="registered")

    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.attendee.username} - {self.event.title}"

class Wishlist(models.Model):

    user = models.ForeignKey(Users,on_delete=models.CASCADE)

    event = models.ForeignKey(Event,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    
class Review(models.Model):

    user = models.ForeignKey(Users,on_delete=models.CASCADE)

    event = models.ForeignKey(Event,on_delete=models.CASCADE)

    rating = models.IntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )