#!/bin/bash

# 🔍 Project Analysis Script for Azure Deployment
# Run this script to understand the current project state

echo "🔍 ANALYZING PROJECT STATE FOR AZURE DEPLOYMENT"
echo "================================================"

echo ""
echo "📁 PROJECT STRUCTURE:"
echo "Current directory: $(pwd)"
echo "Main directories:"
ls -la | grep -E "^d" | awk '{print "  - " $9}'

echo ""
echo "📋 AZURE CONFIGURATION FILES STATUS:"
files=("azure_app_settings.json" "startup.txt" "web.config" ".azureignore" "AZURE_DEPLOYMENT_GUIDE.md")
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "  ✅ $file - EXISTS ($(wc -l < "$file") lines)"
    else
        echo "  ❌ $file - MISSING"
    fi
done

echo ""
echo "🐍 BACKEND CONFIGURATION:"
if [ -f "backend/requirements.txt" ]; then
    echo "  ✅ requirements.txt - EXISTS ($(wc -l < backend/requirements.txt) packages)"
    echo "    Key packages:"
    grep -E "(django|gunicorn|whitenoise|mysql)" backend/requirements.txt | head -5 | sed 's/^/      /'
else
    echo "  ❌ requirements.txt - MISSING"
fi

if [ -f "backend/servicesbladi/settings.py" ]; then
    echo "  ✅ settings.py - EXISTS ($(wc -l < backend/servicesbladi/settings.py) lines)"
    echo "    Azure references:"
    grep -i azure backend/servicesbladi/settings.py | wc -l | awk '{print "      " $1 " Azure references found"}'
else
    echo "  ❌ settings.py - MISSING"
fi

if [ -f "backend/azure_config.py" ]; then
    echo "  ✅ azure_config.py - EXISTS ($(wc -l < backend/azure_config.py) lines)"
else
    echo "  ❌ azure_config.py - MISSING"
fi

if [ -f "backend/BaltimoreCyberTrustRoot.crt.pem" ]; then
    echo "  ✅ SSL Certificate - EXISTS"
else
    echo "  ❌ SSL Certificate - MISSING"
fi

if [ -f "backend/gunicorn.conf.py" ]; then
    echo "  ✅ gunicorn.conf.py - EXISTS"
else
    echo "  ❌ gunicorn.conf.py - MISSING"
fi

echo ""
echo "📱 DJANGO APPS DETECTED:"
if [ -d "backend" ]; then
    for app in backend/*/; do
        if [ -f "$app/apps.py" ] || [ -f "$app/models.py" ]; then
            app_name=$(basename "$app")
            if [ "$app_name" != "__pycache__" ] && [ "$app_name" != "staticfiles" ] && [ "$app_name" != "media" ] && [ "$app_name" != "templates" ]; then
                echo "  📱 $app_name"
            fi
        fi
    done
else
    echo "  ❌ Backend directory not found"
fi

echo ""
echo "🔧 GITHUB ACTIONS:"
if [ -d ".github/workflows" ]; then
    echo "  ✅ GitHub Actions directory exists"
    for workflow in .github/workflows/*.yml; do
        if [ -f "$workflow" ]; then
            echo "    - $(basename "$workflow")"
        fi
    done
else
    echo "  ❌ No GitHub Actions found"
fi

echo ""
echo "📊 PROJECT SIZE ANALYSIS:"
echo "  Total files: $(find . -type f | wc -l)"
echo "  Python files: $(find . -name "*.py" | wc -l)"
echo "  Template files: $(find . -name "*.html" | wc -l)"
echo "  Static files: $(find . -name "*.css" -o -name "*.js" | wc -l)"

echo ""
echo "🎯 IMMEDIATE ACTIONS REQUIRED:"
echo "  1. ⚠️  CRITICAL: Merge azure_config.py into settings.py"
echo "  2. 📝 Update requirements.txt with Azure packages"
echo "  3. 🔍 Validate all Azure configuration files"
echo "  4. 🚀 Choose Azure App Service deployment strategy"
echo "  5. 🔐 Set up environment variables"
echo "  6. 🧪 Test before deployment"

echo ""
echo "📞 NEXT STEPS:"
echo "  📖 Read: AI_DEPLOYMENT_PROMPT.md for detailed instructions"
echo "  📋 Use: DEPLOYMENT_CHECKLIST.md to track progress"
echo "  🔧 Start with: Merging Django settings for Azure"

echo ""
echo "================================================"
echo "🤖 Ready for AI assistant to continue deployment!"
echo "================================================"
