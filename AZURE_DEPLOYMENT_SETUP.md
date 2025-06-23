# Azure Deployment Setup for ServicesBladi version_finale

## 🚀 Overview
This document guides you through setting up Azure deployment for the ServicesBladi Django project. All necessary Azure configuration files have been transferred from the hosting version.

## 📁 Transferred Azure Configuration Files

### Root Level Configuration
- `azure_app_settings.json` - Azure App Service application settings
- `AZURE_DEPLOYMENT_GUIDE.md` - Detailed deployment documentation
- `startup.txt` - Azure startup commands for the Django application
- `web.config` - IIS/Azure web server configuration
- `.azureignore` - Files to ignore during Azure deployment

### Backend Configuration
- `backend/azure_config.py` - Azure-specific Django configurations
- `backend/BaltimoreCyberTrustRoot.crt.pem` - SSL certificate for Azure MySQL
- `backend/gunicorn.conf.py` - Production server configuration
- `backend/requirements.txt` - Updated with Azure-specific packages
- `backend/servicesbladi/settings_azure.py` - Azure-configured Django settings reference

### CI/CD Configuration
- `.github/workflows/azure-deploy.yml` - Azure deployment workflow
- `.github/workflows/main_servicesbladi.yml` - Main deployment workflow

## 🔧 Next Steps to Complete Azure Setup

### 1. Update Django Settings
Replace or merge your current `backend/servicesbladi/settings.py` with the Azure configuration:

```bash
# Option 1: Use the Azure-configured settings directly
cp backend/servicesbladi/settings_azure.py backend/servicesbladi/settings.py

# Option 2: Manually merge Azure configurations into your existing settings
# Review and integrate the Azure-specific configurations from settings_azure.py
```

### 2. Update Requirements
The requirements.txt has been updated with Azure-specific packages. Install them:

```bash
cd backend
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Set up the following environment variables in your Azure App Service:

**In Azure Portal → App Service → Configuration → Application Settings:**
- `DJANGO_SETTINGS_MODULE` = `servicesbladi.settings`
- `PYTHONPATH` = `/home/site/wwwroot`
- `WEBSITE_HTTPLOGGING_RETENTION_DAYS` = `3`

### 4. Database Configuration
Update your database settings to use Azure Database for MySQL:
- Host: `servicesbladi.mysql.database.azure.com`
- Database: `servicesbladi`
- User: `servicesbladiadmin`
- SSL: Uses BaltimoreCyberTrustRoot.crt.pem

### 5. Static Files Configuration
Ensure WhiteNoise is configured for serving static files in Azure:
- Static files will be collected to `staticfiles/`
- Media files will be served from `media/`

### 6. GitHub Actions Setup
Update the GitHub Actions workflow files with your specific:
- Azure subscription ID
- Resource group name
- App service name
- Any repository-specific settings

## 🔍 Azure-Specific Configurations Included

### Security Settings
- SSL redirect disabled (Azure handles SSL termination)
- Secure cookies enabled for HTTPS
- XSS protection enabled
- Content type sniffing disabled

### Performance Settings
- WhiteNoise for static file serving
- Gunicorn with optimized worker configuration
- Database connection optimizations for Azure MySQL

### Logging Configuration
- Console logging for Azure App Service logs
- Error logging to Azure Application Insights
- Custom log rotation settings

## 📊 Deployment Architecture

```
GitHub Repository
    ↓ (GitHub Actions)
Azure App Service
    ├── Static Files (via WhiteNoise)
    ├── Media Files
    └── Database (Azure MySQL)
```

## 🚨 Important Notes

1. **Secret Key**: Update the SECRET_KEY in production settings
2. **Debug Mode**: Ensure DEBUG=False in production
3. **Allowed Hosts**: Update ALLOWED_HOSTS with your Azure URL
4. **Database Credentials**: Secure your database credentials
5. **SSL Certificate**: The Baltimore certificate is included for Azure MySQL

## 🔄 Manual Steps Required

1. Review and merge `settings_azure.py` with your current settings
2. Update any project-specific configurations
3. Test the deployment in a staging environment first
4. Configure Azure App Service settings via Azure Portal
5. Set up monitoring and logging in Azure

## 📞 Support
Refer to `AZURE_DEPLOYMENT_GUIDE.md` for detailed deployment instructions and troubleshooting.
