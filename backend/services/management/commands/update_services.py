from django.core.management.base import BaseCommand
from services.models import Service


class Command(BaseCommand):
    help = 'Update services to have proper French names and remove Test Service'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting service updates...'))
        
        # Remove Test Service
        test_service = Service.objects.filter(title='Test Service').first()
        if test_service:
            test_service.delete()
            self.stdout.write(self.style.SUCCESS('✓ Removed "Test Service"'))
        else:
            self.stdout.write(self.style.WARNING('✗ "Test Service" not found'))

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
            service = Service.objects.filter(title=old_title).first()
            if service:
                service.title = new_title
                service.save()
                self.stdout.write(self.style.SUCCESS(f'✓ Updated "{old_title}" to "{new_title}"'))
            else:
                self.stdout.write(self.style.WARNING(f'✗ Service "{old_title}" not found'))

        # Display final results
        self.stdout.write(self.style.SUCCESS('\nFinal services in database:'))
        services = Service.objects.all()
        for service in services:
            self.stdout.write(f'  - {service.title}')
        
        self.stdout.write(self.style.SUCCESS('\nService updates completed successfully!'))
