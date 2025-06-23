# 📋 Azure Deployment Checklist

## Pre-Deployment Tasks
- [x] **Settings Configuration** ✅ COMPLETED
  - [x] Read current `backend/servicesbladi/settings.py`
  - [x] Read `backend/azure_config.py`
  - [x] Merge Azure configurations into main settings.py
  - [x] Add Azure environment detection
  - [x] Configure Azure database with SSL
  - [x] Set up static files for Azure (WhiteNoise)
  - [x] Configure security settings for Azure
  - [x] Add logging configuration for Azure
  - [x] Update ALLOWED_HOSTS for Azure domain

- [x] **Requirements.txt Validation** ✅ COMPLETED
  - [x] Check current requirements.txt
  - [x] Add gunicorn>=20.1.0
  - [x] Add whitenoise>=6.5.0
  - [x] Add mysqlclient>=2.2.7
  - [x] Add django-environ
  - [ ] Verify all app dependencies

- [ ] **Azure Configuration Files**
  - [ ] Validate azure_app_settings.json
  - [ ] Check startup.txt commands
  - [ ] Verify web.config paths
  - [ ] Update GitHub Actions workflows
  - [ ] Ensure SSL certificate is in place

- [ ] **Azure App Service Strategy**
  - [ ] **Option A: Create New App Service**
    - [ ] Create new Azure App Service
    - [ ] Create new Azure MySQL database
    - [ ] Set up GitHub repository connection
    - [ ] Configure environment variables
  - [ ] **Option B: Reuse Existing**
    - [ ] Disconnect old repository
    - [ ] Connect new repository
    - [ ] Update environment variables

- [ ] **Environment Variables Setup**
  - [ ] DJANGO_SETTINGS_MODULE=servicesbladi.settings
  - [ ] PYTHONPATH=/home/site/wwwroot
  - [ ] WEBSITE_HTTPLOGGING_RETENTION_DAYS=3
  - [ ] SCM_DO_BUILD_DURING_DEPLOYMENT=true
  - [ ] ENABLE_ORYX_BUILD=true
  - [ ] PRE_BUILD_SCRIPT_PATH=startup.txt
  - [ ] Database connection variables
  - [ ] Email configuration variables
  - [ ] SECRET_KEY (new generation)
  - [ ] DEBUG=False

- [ ] **GitHub Repository**
  - [ ] Git repository initialized
  - [ ] All files committed
  - [ ] GitHub repository created
  - [ ] Azure App Service connected
  - [ ] GitHub Actions secrets configured
    - [ ] AZURE_CLIENT_ID
    - [ ] AZURE_TENANT_ID
    - [ ] AZURE_SUBSCRIPTION_ID

- [ ] **Database Strategy**
  - [ ] Choose migration approach
  - [ ] Plan data migration (if needed)
  - [ ] Test database connectivity

## Testing Before Deployment
- [ ] **Local Testing with Azure Settings**
  - [ ] Test with Azure database settings
  - [ ] Verify static files collection
  - [ ] Check all Django apps work
  - [ ] Test admin panel access
  - [ ] Validate user authentication
  - [ ] Test core functionalities

- [ ] **File Validation**
  - [ ] All required files present
  - [ ] No missing dependencies
  - [ ] Correct file permissions
  - [ ] Valid configuration syntax

## Deployment Process
- [ ] **Initial Deployment**
  - [ ] GitHub Actions trigger
  - [ ] Build process completes
  - [ ] Deployment package created
  - [ ] Application deployed to Azure

- [ ] **Post-Deployment Validation**
  - [ ] Application starts successfully
  - [ ] Database migrations run
  - [ ] Static files serve correctly
  - [ ] Admin panel accessible at /admin/
  - [ ] User registration/login works
  - [ ] All Django apps functional:
    - [ ] Accounts app
    - [ ] Chatbot app
    - [ ] Custom requests app
    - [ ] Messaging app
    - [ ] Resources app
    - [ ] Services app

## Post-Deployment Testing
- [ ] **Core Functionality**
  - [ ] Homepage loads
  - [ ] User registration works
  - [ ] User login/logout works
  - [ ] Profile management works
  - [ ] Service requests can be created
  - [ ] Messaging system works
  - [ ] Document upload works
  - [ ] Chatbot responds
  - [ ] Admin panel fully functional

- [ ] **Performance & Security**
  - [ ] SSL certificate valid
  - [ ] Page load times acceptable
  - [ ] Database queries optimized
  - [ ] Static files cached properly
  - [ ] Error pages display correctly

## Troubleshooting Checklist
- [ ] **If Deployment Fails**
  - [ ] Check GitHub Actions logs
  - [ ] Verify environment variables
  - [ ] Check startup.txt execution
  - [ ] Validate requirements.txt
  - [ ] Check file permissions

- [ ] **If Application Won't Start**
  - [ ] Check Azure App Service logs
  - [ ] Verify database connectivity
  - [ ] Check secret key configuration
  - [ ] Validate ALLOWED_HOSTS
  - [ ] Check Python path settings

- [ ] **If Database Issues**
  - [ ] Verify connection string
  - [ ] Check SSL certificate
  - [ ] Test database credentials
  - [ ] Check firewall rules
  - [ ] Validate migration status

## Success Criteria ✅
Application is successfully deployed when:
- [ ] Application loads without errors
- [ ] All pages accessible
- [ ] User authentication functional
- [ ] Database operations work
- [ ] File uploads work
- [ ] Static files serve correctly
- [ ] Admin interface accessible
- [ ] All Django apps operational
- [ ] Performance is acceptable
- [ ] Security configurations active

## Emergency Procedures
- [ ] **Rollback Plan Ready**
  - [ ] Old version still accessible
  - [ ] Database backup available
  - [ ] Quick rollback procedure documented
  - [ ] Contact information ready

---
**Date Started:** ___________  
**Completed By:** ___________  
**Deployment Status:** [ ] In Progress [ ] Completed [ ] Failed  
**Notes:** ________________________________
