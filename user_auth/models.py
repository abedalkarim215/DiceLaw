from django.db import models

# Model for Attorneys
class Attorney(models.Model):
    name = models.CharField(max_length=100)  # Name of the attorney
    email = models.EmailField(unique=True)  # Email address of the attorney (unique)
    about = models.TextField()  # Information about the attorney
    image = models.ImageField(upload_to='attorney_images/')  # Image of the attorney
    practice_area = models.ForeignKey('web.PracticeArea', on_delete=models.CASCADE)  # Practice area associated with the attorney
