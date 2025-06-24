#!/usr/bin/env python3
import os
import sys
import django

# Add the backend directory to Python path
sys.path.append('/home/mohammedabd/Desktop/WEBSITE/SERVICESBLADI/ORIGINAL/version_finale/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'servicesbladi.settings')

django.setup()

from services.models import Service, ServiceCategory

def check_and_activate_services():
    print("Current Services:")
    services = Service.objects.all()
    if not services.exists():
        print("No services found in database!")
        print("Let's check categories...")
    else:
        for service in services:
            print(f"- {service.title} (Active: {service.is_active}) - Category: {service.service_type.category.name}")
    
    print("\nCurrent Categories:")
    categories = ServiceCategory.objects.all()
    if not categories.exists():
        print("No categories found in database!")
        return
    
    for category in categories:
        print(f"- {category.name} (Active: True)")
        # Check service types in this category
        for service_type in category.service_types.all():
            print(f"  └─ {service_type.name}")
    
    # Check if we need to create services or just activate them
    if services.exists():
        print("\nActivating all services...")
        Service.objects.all().update(is_active=True)
        print("✅ All services activated!")
        
        print("\nUpdated Services:")
        for service in Service.objects.all():
            print(f"- {service.title} (Active: {service.is_active})")
    else:
        print("\n⚠️ No services found. You may need to create them first.")

if __name__ == "__main__":
    check_and_activate_services()
