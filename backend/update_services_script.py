#!/usr/bin/env python
"""
Script to update service names in the database
"""
import os
import sys
import django

print("Starting script...")

try:
    # Add the project directory to Python path
    sys.path.append('c:/Users/Airzo/Desktop/SERVICESBLADI/version_finale/backend')
    print("Added path to sys.path")

    # Set Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'servicesbladi.settings')
    print("Set Django settings module")

    # Setup Django
    django.setup()
    print("Django setup completed")

    from services.models import Service
    print("Imported Service model")

    print("Starting service updates...")
    
    # First, let's see what services currently exist
    print("\nCurrent services in database:")
    try:
        services = Service.objects.all()
        for service in services:
            print(f'  - {service.title}')
    except Exception as e:
        print(f"Error fetching services: {e}")
        sys.exit(1)

    # Remove Test Service
    try:
        test_service = Service.objects.filter(title='Test Service').first()
        if test_service:
            test_service.delete()
            print('✓ Removed "Test Service"')
        else:
            print('✗ "Test Service" not found')
    except Exception as e:
        print(f"Error removing Test Service: {e}")

    # Update service titles to proper French names (consistent without "Services" prefix)
    service_updates = {
        'Administrative Basic Service': 'Administratif',
        'Services Administratifs': 'Administratif',  # In case it exists in database
        'Tourism Basic Service': 'Tourisme', 
        'Real Estate Basic Service': 'Immobilier',
        'Investment Basic Service': 'Investissement',
        'Fiscal Basic Service': 'Fiscal'
    }

    for old_title, new_title in service_updates.items():
        try:
            service = Service.objects.filter(title=old_title).first()
            if service:
                service.title = new_title
                service.save()
                print(f'✓ Updated "{old_title}" to "{new_title}"')
            else:
                print(f'✗ Service "{old_title}" not found')
        except Exception as e:
            print(f"Error updating {old_title}: {e}")

    # Display final results
    print('\nFinal services in database:')
    try:
        services = Service.objects.all()
        for service in services:
            print(f'  - {service.title}')
    except Exception as e:
        print(f"Error fetching final services: {e}")
    
    print('\nService updates completed successfully!')

except Exception as e:
    print(f"Error in script: {e}")
    import traceback
    traceback.print_exc()
