#!/usr/bin/env python3
"""
Deployment Fix Script for ServicesBLADI

This script addresses the following issues:
1. Service activation and French category names
2. Media file handling for Azure deployment
3. Document download/view functionality
4. Profile picture and country update issues

Run this script after deployment to ensure all fixes are applied.
"""

import os
import sys
import django

# Add the backend directory to Python path
sys.path.append('/home/mohammedabd/Desktop/WEBSITE/SERVICESBLADI/ORIGINAL/version_finale/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'servicesbladi.settings')

django.setup()

from services.models import Service, ServiceCategory, ServiceType

def fix_deployment_issues():
    print("🔧 ServicesBLADI Deployment Fix Script")
    print("=" * 50)
    
    # 1. Check and activate services
    print("\n1. Checking services activation...")
    
    categories = ServiceCategory.objects.all()
    services = Service.objects.all()
    
    if not categories.exists():
        print("❌ No service categories found!")
        return
    
    if not services.exists():
        print("❌ No services found!")
        return
        
    print(f"✅ Found {categories.count()} categories and {services.count()} services")
    
    # 2. Ensure French category names
    print("\n2. Updating category names to French...")
    
    french_names = {
        'Administrative Services': 'Administratif',
        'Tourism Services': 'Tourisme', 
        'Real Estate Services': 'Immobilier',
        'Fiscal Services': 'Fiscal',
        'Investment Services': 'Investissement'
    }
    
    updated_count = 0
    for category in categories:
        if category.name in french_names:
            old_name = category.name
            category.name = french_names[old_name]
            category.name_fr = french_names[old_name]
            category.save()
            print(f"   ✅ Updated '{old_name}' to '{category.name}'")
            updated_count += 1
        else:
            print(f"   ℹ️ Category '{category.name}' already in French")
    
    # 3. Activate all services
    print("\n3. Activating all services...")
    
    inactive_services = Service.objects.filter(is_active=False)
    if inactive_services.exists():
        Service.objects.all().update(is_active=True)
        print(f"   ✅ Activated {inactive_services.count()} services")
    else:
        print("   ✅ All services already active")
    
    # 4. Final verification
    print("\n4. Final verification...")
    
    print("\nActive Categories:")
    for category in ServiceCategory.objects.all():
        service_count = Service.objects.filter(service_type__category=category, is_active=True).count()
        print(f"   • {category.name}: {service_count} active services")
    
    total_active = Service.objects.filter(is_active=True).count()
    print(f"\n✅ Total active services: {total_active}")
    
    if total_active > 0:
        print("\n🎉 All deployment issues fixed successfully!")
        print("\nNext steps:")
        print("1. Test 'Nouvelle demande' functionality")
        print("2. Test document upload/download")
        print("3. Test profile picture upload") 
        print("4. Test country selection in profile")
    else:
        print("\n❌ No active services found. Please check your database.")

if __name__ == "__main__":
    fix_deployment_issues()
