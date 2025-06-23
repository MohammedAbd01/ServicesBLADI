# 🚀 AZURE APP SERVICE UPDATE INSTRUCTIONS

## STEP 1: Update Environment Variables in Azure Portal

1. Go to **Azure Portal** → **Your App Service** → **Configuration** → **Application Settings**
2. Add/Update these environment variables:

```
DJANGO_SETTINGS_MODULE=servicesbladi.settings
DJANGO_ENV=production
SECRET_KEY=<generate-new-32-char-secret-key>
AZURE_MYSQL_HOST=<your-mysql-server>.mysql.database.azure.com
AZURE_MYSQL_NAME=servicesbladi
AZURE_MYSQL_USER=<your-mysql-username>
AZURE_MYSQL_PASSWORD=<your-mysql-password>
AZURE_MYSQL_PORT=3306
PYTHONPATH=/home/site/wwwroot
SCM_DO_BUILD_DURING_DEPLOYMENT=true
ENABLE_ORYX_BUILD=true
PRE_BUILD_SCRIPT_PATH=startup.txt
```

3. Click **Save** to apply the changes

## STEP 2: Update GitHub Repository Connection

### Option A: Via Azure Portal (Recommended)
1. Go to **Azure Portal** → **Your App Service** → **Deployment Center**
2. **Disconnect** current repository if connected
3. Click **GitHub** → **Authorize** → **Continue**
4. Select:
   - **Organization**: MohammedAbd01
   - **Repository**: ServicesBLADI
   - **Branch**: main (or master)
5. Click **Save**

### Option B: Via GitHub Actions (If you prefer)
1. The repository already has `.github/workflows/azure-deploy.yml`
2. Update the workflow file with your App Service name
3. Add Azure credentials as GitHub secrets

## STEP 3: Verify Deployment Settings

1. **App Service Plan**: Ensure it's Linux with Python 3.10+
2. **Startup Command**: Should be empty (we use startup.txt)
3. **Always On**: Enable for production
4. **ARR Affinity**: Disable for better performance

## STEP 4: Deploy

1. After connecting GitHub, Azure will automatically trigger deployment
2. Monitor deployment in **Azure Portal** → **Deployment Center** → **Logs**
3. Watch for any errors during build/deployment

## STEP 5: Post-Deployment Verification

1. Check **App Service** → **Log stream** for any runtime errors
2. Test your website URL
3. Verify all Django apps are working:
   - accounts (user management)
   - chatbot (AI functionality)
   - custom_requests (request handling)
   - messaging (real-time chat)
   - resources (resource management)
   - services (core services)

## 🚨 IMPORTANT NOTES:

- **Database**: Make sure your Azure MySQL database is configured and accessible
- **Static Files**: Will be served by WhiteNoise (already configured)
- **SSL**: HTTPS is enforced in production settings
- **Logging**: Check `/home/site/wwwroot/logs/` for detailed logs

## 🛟 TROUBLESHOOTING:

If deployment fails:
1. Check **Deployment Center** → **Logs** for build errors
2. Check **Log stream** for runtime errors
3. Verify all environment variables are set correctly
4. Ensure database connection string is correct

## ✅ SUCCESS INDICATORS:

- Deployment shows "Success" in Deployment Center
- Website loads without 500 errors
- All Django apps are accessible
- Static files (CSS/JS) load correctly
- Database operations work
