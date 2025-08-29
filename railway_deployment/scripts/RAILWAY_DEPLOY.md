# 🚂 75Flow - Railway Deployment Guide

## 🎯 **Step-by-Step Railway Deployment**

### Step 1: Go to Railway
1. **Visit** [railway.app](https://railway.app)
2. **Sign up** with your GitHub account (no credit card required)
3. **Click "New Project"**

### Step 2: Connect Your Repository
1. **Select "Deploy from GitHub repo"**
2. **Choose your repository**: `Shruti165/75flow`
3. **Railway will auto-detect Django** and start deploying

### Step 3: Configure Environment Variables
In Railway dashboard, go to your project → **Variables** tab and add:

```
SECRET_KEY=atc5s6uveg37ghg3t5#giuvviglu$gj8(b-ig2o6!im36q0_ll
DEBUG=False
ENVIRONMENT=production
ALLOWED_HOSTS=*.railway.app
```

### Step 4: Wait for Deployment
- Railway will automatically:
  - Install dependencies from `requirements.txt`
  - Run the build process
  - Deploy your app

### Step 5: Run Migrations
Once deployed, in Railway dashboard:
1. Go to **Deployments** tab
2. Click on your latest deployment
3. Click **View Logs** → **Terminal**
4. Run these commands:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

### Step 6: Access Your App
Your app will be live at: `https://your-app-name.railway.app`

## 👥 **User Credentials**
Once deployed, these users will be available:
- **Shruti**: Username: `Shruti`, Password: `Shruti123`
- **Sid**: Username: `Sid`, Password: `Sid123`
- **Sanju**: Username: `Sanju`, Password: `Sanju123`

## 📱 **Mobile Features**
- ✅ Responsive design for all devices
- ✅ Touch-friendly interface
- ✅ Fast loading on mobile
- ✅ Works on iPhone, Android, tablets

## 🎯 **What Happens After Deployment**
1. ✅ Your app will be live and accessible
2. ✅ All three users can log in immediately
3. ✅ Mobile-responsive design works perfectly
4. ✅ Share the URL with Sid and Sanju
5. ✅ Start your 75-day challenge!

## 🆘 **Troubleshooting**
- **If deployment fails**: Check the logs in Railway dashboard
- **If migrations fail**: Run them manually in the terminal
- **If static files don't load**: WhiteNoise is configured for production

## 🎉 **You're Ready!**
Your 75Flow app will be live in minutes on Railway - completely free!

---
**Good luck with your 75-day challenge! 🚀** 