# 🚀 75Flow - Quick Deployment Guide

## Deploy to Railway (Recommended - Free & Easy)

### Option 1: Automatic Deployment Script
```bash
# Make sure you're in the project directory
./deploy_railway.sh
```

### Option 2: Manual Railway Deployment
1. **Sign up** at [railway.app](https://railway.app)
2. **Connect your GitHub** repository
3. **Railway will auto-detect Django** and deploy
4. **Set environment variables** in Railway dashboard:
   - `SECRET_KEY` (generate one)
   - `DEBUG=False`
   - `ENVIRONMENT=production`
   - `ALLOWED_HOSTS=*.railway.app`

### Option 3: Railway CLI
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway init
railway up
```

## 🔧 Post-Deployment Steps

1. **Run migrations**:
   ```bash
   railway run python manage.py migrate
   ```

2. **Create superuser**:
   ```bash
   railway run python manage.py createsuperuser
   ```

3. **Test the app**:
   - Visit your Railway URL
   - Test login with existing users:
     - Shruti / Shruti123
     - Sid / Sid123
     - Sanju / Sanju123

## 📱 Mobile Ready

The app is fully mobile-responsive and works perfectly on:
- ✅ iPhone/iPad
- ✅ Android phones/tablets
- ✅ All modern browsers

## 👥 Share with Team

Once deployed, share the Railway URL with:
- **Sid** - Username: `Sid`, Password: `Sid123`
- **Sanju** - Username: `Sanju`, Password: `Sanju123`

## 🆘 Need Help?

- Check the full deployment guide: `DEPLOYMENT.md`
- Railway documentation: https://docs.railway.app
- Django deployment docs: https://docs.djangoproject.com/en/5.1/howto/deployment/

---

**Happy Deploying! 🎉** 