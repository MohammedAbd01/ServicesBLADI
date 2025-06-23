# ⚠️  GITHUB SECRET UPDATE REQUIRED

The 401 Unauthorized error indicates that the GitHub secret `AZURE_WEBAPP_PUBLISH_PROFILE` 
needs to be updated with a fresh publish profile.

## 🔄 STEPS TO FIX:

### 1. GET FRESH PUBLISH PROFILE

Go to Azure Portal:
1. Navigate to: App Services → servicesbladi
2. Click "Get publish profile" (in the top toolbar)
3. Download the .publishsettings file
4. Open the file and copy ALL the XML content

### 2. UPDATE GITHUB SECRET

Go to GitHub:
1. Navigate to: https://github.com/MohammedAbd01/ServicesBLADI/settings/secrets/actions
2. Find the secret: AZURE_WEBAPP_PUBLISH_PROFILE
3. Click "Update" (pencil icon)
4. Replace the value with the fresh XML content from Azure Portal
5. Click "Update secret"

### 3. TRIGGER NEW DEPLOYMENT

After updating the secret:
- Push any small change to trigger a new deployment, OR
- Go to Actions tab and manually run the workflow

## 🚨 COMMON ISSUES:

- Make sure to copy the ENTIRE XML content (including <?xml> declaration)
- Don't add any extra spaces or line breaks
- The XML should start with <?xml and end with </publishData>

## ✅ ALTERNATIVE: Use Azure CLI Method

If the publish profile continues to have issues, I can help you set up 
GitHub deployment using Azure CLI authentication instead.

## 📋 FRESH PUBLISH PROFILE CONTENT:

Copy this from Azure Portal instead for the most current credentials:
```
The content from the .publishsettings file you download from Azure Portal
```
