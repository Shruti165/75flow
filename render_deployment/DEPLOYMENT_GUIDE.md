# 🚀 Render Deployment Guide with Local Data

This guide explains how to deploy your 75Flow application to Render with all your local data and users, including configurable challenge settings.

## 📋 Prerequisites

- Local Django application running with data
- GitHub repository connected to Render
- Render account

## 🔄 Step-by-Step Process

### **Step 1: Export Local Data**

Run the export script from your local project:

```bash
cd /path/to/your/75Flow
python scripts/export_local_data.py
```

This will create:
- `local_data_export.json` - Raw data export
- `import_local_data.py` - Import script for Render
- `reset_passwords.py` - Password reset script

### **Step 2: Commit and Push**

```bash
git add .
git commit -m "Add local data export for Render deployment"
git push origin main
```

### **Step 3: Deploy on Render**

1. **Go to [Render Dashboard](https://render.com)**
2. **Create New Web Service**
3. **Connect your GitHub repository**
4. **Render will automatically detect the configuration**

### **Step 4: Monitor Deployment**

The build process will:
1. Install dependencies
2. Run migrations
3. **Import your local data automatically**
4. Create all users, categories, and habits

### **Step 5: Configure Challenge Settings (Optional)**

Customize your challenge parameters in Render:

1. **Go to your Render service dashboard**
2. **Navigate to Environment tab**
3. **Add these environment variables:**
   ```bash
   CHALLENGE_START_DATE=2025-07-15
   CHALLENGE_DURATION_DAYS=75
   CHALLENGE_NAME=75Flow Challenge
   ```
4. **Redeploy if you made changes**

### **Step 6: Login with Your Local Credentials**

After deployment, you can login with:
- **Your existing usernames**
- **Passwords reset to usernames** (e.g., username: `Shruti`, password: `Shruti`)

## 🔧 Manual Data Import (If Needed)

If automatic import fails, you can manually import data:

### **Option A: Render Shell**

1. Go to your service in Render Dashboard
2. Click "Shell" tab
3. Run:

```bash
python import_local_data.py
python reset_passwords.py
```

### **Option B: Management Commands**

```bash
# Reset passwords to usernames
python manage.py reset_participant_passwords

# Or create specific users
python manage.py shell
```

In the shell:
```python
from django.contrib.auth.models import User
user = User.objects.get(username='Shruti')
user.set_password('Shruti')
user.save()
exit()
```

## 📊 What Gets Exported/Imported

### **✅ Users & Profiles**
- Username, email, names
- Profile information (bio, images)
- Staff/superuser status

### **✅ Categories**
- Category names and descriptions
- Colors and icons
- Creation dates

### **✅ Habits**
- Habit names and descriptions
- Category associations
- User assignments

### **✅ Habit Completion Records**
- Daily completion status
- Dates and timestamps
- All historical data

## 🚨 Important Notes

1. **Passwords are reset** to usernames for easy access
2. **Profile images** are exported as file paths (not actual files)
3. **All relationships** are preserved
4. **Data integrity** is maintained

## 🔍 Troubleshooting

### **Import Fails**
- Check if all models exist
- Verify database migrations
- Check Render shell logs

### **Users Can't Login**
- Run `python reset_passwords.py`
- Verify user creation in admin panel
- Check password reset logs

### **Missing Data**
- Verify export script ran successfully
- Check import script logs
- Manually run import commands

## 🎯 Success Indicators

After successful deployment:
- ✅ All users can login
- ✅ Categories are visible
- ✅ Habits are displayed
- ✅ Progress tracking works
- ✅ Admin panel accessible

## 📞 Support

If you encounter issues:
1. Check Render build logs
2. Verify data export was successful
3. Check import script output
4. Use Render shell for debugging

---

**Happy Deploying! 🚀**
