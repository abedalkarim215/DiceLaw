from django.db import models
from django.contrib.auth.models import User

# Model for Practice Areas
class PracticeArea(models.Model):
    name = models.CharField(max_length=100)  # Name of the practice area
    logo = models.ImageField(upload_to='practice_area_logos/')  # Logo associated with the practice area
    description = models.TextField()  # Description of the practice area
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time of creation

# Model for Free Consultations
class FreeConsultation(models.Model):
    client = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)  # Client associated with the consultation
    subject = models.CharField(max_length=200)  # Subject of the consultation
    message = models.TextField()  # Message of the consultation
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time of creation

# Model for Clients' Reviews
class ClientsReview(models.Model):
    client = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)  # Client who provided the review
    message = models.TextField()  # The review message
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time of creation

# Model for Newsletter Subscriptions
class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)  # Email address for subscription (unique)
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time of subscription



# Model for Contact Us Requests
class ContactUs(models.Model):
    client = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)  # Client who sent the request
    subject = models.CharField(max_length=200)  # Subject of the request
    message = models.TextField()  # Message of the request
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time of creation


# Model for General Information
class GeneralInfo(models.Model):
    logo = models.ImageField(upload_to='general_info_logos/')  # Logo for general information
    bio = models.TextField()  # Biographical information
    facebook_url = models.URLField()  # Facebook profile URL
    instagram_url = models.URLField()  # Instagram profile URL
    twitter_url = models.URLField()  # Twitter profile URL
    location = models.CharField(max_length=100)  # Location information
    phone = models.CharField(max_length=15)  # Phone number
    mobile = models.CharField(max_length=15)  # Mobile number
    email = models.EmailField()  # Email address
    honors_and_awards_count = models.PositiveIntegerField()  # Count of honors and awards
    successful_cases_count = models.PositiveIntegerField()  # Count of successful cases
    trusted_clients_count = models.PositiveIntegerField()  # Count of trusted clients