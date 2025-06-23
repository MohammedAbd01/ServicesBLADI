#!/usr/bin/env python3
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from services.models import Service

print("Current services in database:")
services = Service.objects.all()
for service in services:
    print(f"  - ID: {service.id}, Title: \"{service.title}\", Active: {service.is_active}")

print(f"\nTotal services: {services.count()}")
print(f"Active services: {Service.objects.filter(is_active=True).count()}")
