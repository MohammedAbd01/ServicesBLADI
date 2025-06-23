# 🔧 AZURE ENVIRONMENT VARIABLES SETUP

## REQUIRED ENVIRONMENT VARIABLES FOR YOUR APP SERVICE:

### Core Django Settings:
```bash
DJANGO_SETTINGS_MODULE=servicesbladi.settings
DJANGO_ENV=production
```

### Security:
```bash
SECRET_KEY=<GENERATE_NEW_SECRET_KEY>
# Generate a new secret key: https://djecrety.ir/
```

### Database Configuration:
```bash
AZURE_MYSQL_HOST=<your-mysql-server>.mysql.database.azure.com
AZURE_MYSQL_NAME=servicesbladi
AZURE_MYSQL_USER=<your-mysql-username>
AZURE_MYSQL_PASSWORD=<your-mysql-password>
AZURE_MYSQL_PORT=3306
```

### Azure App Service Settings:
```bash
WEBSITE_HTTPLOGGING_RETENTION_DAYS=3
SCM_DO_BUILD_DURING_DEPLOYMENT=true
ENABLE_ORYX_BUILD=true
PRE_BUILD_SCRIPT_PATH=startup.txt
PYTHONPATH=/home/site/wwwroot
```

---

## 📝 HOW TO SET THESE IN AZURE PORTAL:

1. **Go to Azure Portal**
2. **Navigate to your App Service**
3. **Go to Configuration → Application Settings**
4. **Click "New application setting" for each variable**
5. **Save all changes**

---

## 🔍 FIND YOUR CURRENT DATABASE SETTINGS:

Your current database settings should be in your existing App Service under:
- **Configuration → Application Settings**
- Look for variables like:
  - `DATABASE_URL`
  - `MYSQL_HOST`
  - `AZURE_MYSQL_*`
  - `DB_*`

---

## ⚡ QUICK SETUP CHECKLIST:

### Before Updating Repository:
- [ ] Copy current database settings from Azure Portal
- [ ] Generate new SECRET_KEY
- [ ] Prepare all environment variables

### Update Repository:
- [ ] Go to Deployment Center
- [ ] Disconnect old repository
- [ ] Connect new repository: `version_finale`
- [ ] Set branch to deploy from

### Set Environment Variables:
- [ ] Add all required variables
- [ ] Save configuration
- [ ] Restart App Service

### Deploy & Test:
- [ ] Trigger deployment
- [ ] Monitor logs
- [ ] Test website functionality

---

**NEXT STEP: Tell me your current App Service name and I'll help you with the specific update process!**
