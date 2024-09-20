from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book
import requests
from django.conf import settings

@receiver(post_save, sender=Book)
def update_frontend(sender, instance, created, **kwargs):
       if created: 
        frontend_url = settings.FRONTEND_API_URL + '/books/'
        book_data = {
               'title': instance.title,
               'author': instance.author,
               'publisher': instance.publisher,
               'category': instance.category,
               'available': instance.available,
               'return_date': instance.return_date
           }
           
        try:
               # Make a POST request to the frontend API to create the book
               response = requests.post(frontend_url, json=book_data)
               response.raise_for_status()  # Raise an error if the request fails
               print(f"Book '{instance.title}' successfully synced with frontend.")
        except requests.exceptions.RequestException as e:
               print(f"Failed to sync book '{instance.title}' with frontend: {e}")