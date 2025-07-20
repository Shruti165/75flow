from django.core.management.base import BaseCommand
from django.test import Client
from django.urls import reverse

class Command(BaseCommand):
    help = 'Test the health check endpoint'

    def handle(self, *args, **options):
        client = Client()
        
        # Test health endpoint
        response = client.get('/health/')
        self.stdout.write(f'Health endpoint status: {response.status_code}')
        self.stdout.write(f'Health endpoint content: {response.content.decode()}')
        
        # Test test endpoint
        response = client.get('/test/')
        self.stdout.write(f'Test endpoint status: {response.status_code}')
        self.stdout.write(f'Test endpoint content: {response.content.decode()}')
        
        # Test root endpoint
        response = client.get('/')
        self.stdout.write(f'Root endpoint status: {response.status_code}') 