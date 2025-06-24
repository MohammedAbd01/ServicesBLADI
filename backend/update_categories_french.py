#!/usr/bin/env python3
import os
import sys
import django

# Add the backend directory to Python path
sys.path.append('/home/mohammedabd/Desktop/WEBSITE/SERVICESBLADI/ORIGINAL/version_finale/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'servicesbladi.settings')

django.setup()

from services.models import ServiceCategory

def update_categories_to_french():
    print("Updating categories to French...")
    
    # Mapping of English to French names
    french_names = {
        'Administrative Services': 'Administratif',
        'Tourism Services': 'Tourisme',
        'Real Estate Services': 'Immobilier', 
        'Fiscal Services': 'Fiscal',
        'Investment Services': 'Investissement'
    }
    
    for category in ServiceCategory.objects.all():
        if category.name in french_names:
            old_name = category.name
            category.name = french_names[old_name]
            category.name_fr = french_names[old_name]
            category.save()
            print(f"✅ Updated '{old_name}' to '{category.name}'")
        else:
            print(f"⚠️ Category '{category.name}' not found in mapping")
    
    print("\nUpdated Categories:")
    for category in ServiceCategory.objects.all():
        print(f"- {category.name}")

if __name__ == "__main__":
    update_categories_to_french()
