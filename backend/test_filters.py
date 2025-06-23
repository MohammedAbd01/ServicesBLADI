#!/usr/bin/env python3
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'servicesbladi.settings')
django.setup()

from services.templatetags.service_filters import translate_service_name, should_display_service
from services.models import Service

print("Testing template filters...")

# Test services (simulating what might be in database)
test_services = [
    "Test Service",
    "Administrative Basic Service", 
    "Tourism Basic Service",
    "Real Estate Basic Service",
    "Investment Basic Service",
    "Fiscal Basic Service",
    "Administratif",
    "Tourisme",
    "Immobilier",
    "Investissement",
    "Fiscal"
]

print("\nTranslation tests:")
for service_name in test_services:
    translated = translate_service_name(service_name)
    should_display = should_display_service(service_name)
    print(f"  '{service_name}' -> '{translated}' (display: {should_display})")

print("\nActual services in database:")
try:
    services = Service.objects.all()
    for service in services:
        translated = translate_service_name(service.title)
        should_display = should_display_service(service.title)
        print(f"  ID {service.id}: '{service.title}' -> '{translated}' (display: {should_display}, active: {service.is_active})")
except Exception as e:
    print(f"  Error accessing database: {e}")
