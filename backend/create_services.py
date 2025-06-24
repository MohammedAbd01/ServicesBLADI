#!/usr/bin/env python
import os
import sys
import django

# Add the parent directory to the path to import Django settings
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'servicesbladi.settings')

django.setup()

from services.models import ServiceCategory, Service

def create_french_services():
    """Create only the 5 French services as shown in the screenshot"""
    
    # Create service categories in French
    categories_data = [
        {
            'name': 'Administratif',
            'description': 'Services administratifs et juridiques',
            'icon': 'fas fa-file-alt'
        },
        {
            'name': 'Tourisme', 
            'description': 'Services liés au tourisme et voyages',
            'icon': 'fas fa-plane'
        },
        {
            'name': 'Immobilier',
            'description': 'Services immobiliers et propriétés',
            'icon': 'fas fa-home'
        },
        {
            'name': 'Fiscal',
            'description': 'Services fiscaux et comptables',
            'icon': 'fas fa-calculator'
        },
        {
            'name': 'Investissement',
            'description': 'Services d\'investissement et financiers',
            'icon': 'fas fa-chart-line'
        }
    ]
    
    print("Creating French service categories...")
    
    # Clear existing categories and services
    ServiceCategory.objects.all().delete()
    Service.objects.all().delete()
    
    created_categories = []
    
    for cat_data in categories_data:
        category, created = ServiceCategory.objects.get_or_create(
            name=cat_data['name'],
            defaults={
                'description': cat_data['description'],
                'icon': cat_data['icon'],
                'is_active': True
            }
        )
        created_categories.append(category)
        print(f"✓ Catégorie créée: {category.name}")
    
    # Create services for each category
    services_data = {
        'Administratif': [
            {
                'name': 'Demande de passeport',
                'description': 'Assistance pour les demandes de passeport',
                'price': 150.00,
                'duration': '2-3 jours ouvrables'
            },
            {
                'name': 'Demande de visa',
                'description': 'Aide pour les demandes de visa',
                'price': 200.00,
                'duration': '5-10 jours ouvrables'
            },
            {
                'name': 'Documents légaux',
                'description': 'Préparation de documents légaux',
                'price': 100.00,
                'duration': '1-2 jours ouvrables'
            }
        ],
        'Tourisme': [
            {
                'name': 'Réservation d\'hôtel',
                'description': 'Réservation d\'hébergements',
                'price': 50.00,
                'duration': 'Immédiat'
            },
            {
                'name': 'Circuit touristique',
                'description': 'Organisation de circuits touristiques',
                'price': 300.00,
                'duration': '1-2 semaines'
            },
            {
                'name': 'Guide touristique',
                'description': 'Services de guide touristique',
                'price': 80.00,
                'duration': 'Par jour'
            }
        ],
        'Immobilier': [
            {
                'name': 'Recherche de propriété',
                'description': 'Aide à la recherche de biens immobiliers',
                'price': 500.00,
                'duration': '1-4 semaines'
            },
            {
                'name': 'Évaluation immobilière',
                'description': 'Évaluation de la valeur immobilière',
                'price': 200.00,
                'duration': '3-5 jours ouvrables'
            },
            {
                'name': 'Contrat de location',
                'description': 'Préparation de contrats de location',
                'price': 150.00,
                'duration': '1-2 jours ouvrables'
            }
        ],
        'Fiscal': [
            {
                'name': 'Déclaration d\'impôts',
                'description': 'Aide pour la déclaration d\'impôts',
                'price': 120.00,
                'duration': '2-3 jours ouvrables'
            },
            {
                'name': 'Consultation fiscale',
                'description': 'Conseils en matière fiscale',
                'price': 80.00,
                'duration': '1 heure'
            },
            {
                'name': 'Comptabilité',
                'description': 'Services de comptabilité',
                'price': 250.00,
                'duration': 'Mensuel'
            }
        ],
        'Investissement': [
            {
                'name': 'Conseil en investissement',
                'description': 'Conseils pour investissements',
                'price': 300.00,
                'duration': '1-2 heures'
            },
            {
                'name': 'Analyse de marché',
                'description': 'Analyse des opportunités de marché',
                'price': 400.00,
                'duration': '1 semaine'
            },
            {
                'name': 'Gestion de portefeuille',
                'description': 'Gestion de portefeuille d\'investissement',
                'price': 500.00,
                'duration': 'Mensuel'
            }
        ]
    }
    
    print("\nCreating services...")
    
    for category in created_categories:
        if category.name in services_data:
            for service_data in services_data[category.name]:
                service, created = Service.objects.get_or_create(
                    name=service_data['name'],
                    category=category,
                    defaults={
                        'description': service_data['description'],
                        'price': service_data['price'],
                        'duration': service_data['duration'],
                        'is_active': True
                    }
                )
                if created:
                    print(f"  ✓ Service créé: {service.name} - {service.price}€")
                else:
                    print(f"  → Service existe déjà: {service.name}")
    
    print(f"\n✅ Terminé! {ServiceCategory.objects.count()} catégories et {Service.objects.count()} services créés.")
    
    # Display summary
    print("\n=== RÉSUMÉ ===")
    for category in ServiceCategory.objects.all():
        print(f"\n📁 {category.name} ({category.services.count()} services)")
        for service in category.services.all():
            print(f"   • {service.name} - {service.price}€")

if __name__ == '__main__':
    create_french_services()
