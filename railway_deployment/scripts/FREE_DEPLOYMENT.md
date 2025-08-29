# 🆓 75Flow - Free Deployment Guide

## 🎯 **Railway (Recommended - Completely Free)**

### Step 1: Prepare Your Repository
```bash
# Make sure your code is on GitHub
git add .
git commit -m "Ready for deployment"
git push origin main
```

### Step 2: Deploy to Railway
1. **Go to** [railway.app](https://railway.app)
2. **Sign up** with GitHub (no credit card needed)
3. **Click "New Project"**
4. **Select "Deploy from GitHub repo"**
5. **Choose your 75Flow repository**
6. **Railway will auto-detect Django and deploy!**

### Step 3: Configure Environment Variables
In Railway dashboard, go to your project → Variables tab and add:
```
SECRET_KEY=your-secret-key-here
DEBUG=False
ENVIRONMENT=production
ALLOWED_HOSTS=*.railway.app
```

### Step 4: Run Migrations
In Railway dashboard → Deployments → View Logs → Terminal:
```bash
python manage.py migrate
python manage.py createsuperuser
```

### Step 5: Share with Team
Your app will be live at: `https://your-app-name.railway.app`

---

## 🎯 **Render (Alternative - Completely Free)**

### Step 1: Deploy to Render
1. **Go to** [render.com](https://render.com)
2. **Sign up** with GitHub (no credit card needed)
3. **Click "New +" → "Web Service"**
4. **Connect your GitHub repository**
5. **Configure settings**:
   - **Name**: `75flow`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn flow75.wsgi:application`
6. **Click "Create Web Service"**

### Step 2: Add Environment Variables
In Render dashboard → Environment → Environment Variables:
```
SECRET_KEY=your-secret-key-here
DEBUG=False
ENVIRONMENT=production
ALLOWED_HOSTS=*.onrender.com
```

### Step 3: Run Migrations
In Render dashboard → Shell:
```bash
python manage.py migrate
python manage.py createsuperuser
```

---

## 🔑 **Generate Secret Key**
```bash
python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## 👥 **User Credentials**
Once deployed, these users will be available:
- **Shruti**: Username: `Shruti`, Password: `Shruti123`
- **Sid**: Username: `Sid`, Password: `Sid123`
- **Sanju**: Username: `Sanju`, Password: `Sanju123`

## 📱 **Mobile Ready**
- ✅ Works perfectly on iPhone, Android, tablets
- ✅ Responsive design for all screen sizes
- ✅ Touch-friendly interface

## 🎯 **Post-Deployment**
1. ✅ Test login with all users
2. ✅ Verify mobile responsiveness
3. ✅ Share URL with Sid and Sanju
4. ✅ Start your 75-day challenge!

---

## 🆘 **Need Help?**
- **Railway Docs**: https://docs.railway.app
- **Render Docs**: https://render.com/docs
- **Both platforms offer free support**

---

**🚀 Your 75Flow app will be live in minutes - completely free!** 