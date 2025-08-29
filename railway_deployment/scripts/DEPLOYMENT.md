# 75Flow - Production Deployment Guide

## 🚀 Quick Deploy Options

### Option 1: Railway (Recommended - Free & Easy)
1. **Sign up** at [railway.app](https://railway.app)
2. **Connect your GitHub** repository
3. **Deploy automatically** - Railway will detect Django and deploy

### Option 2: Render (Free Tier Available)
1. **Sign up** at [render.com](https://render.com)
2. **Create a new Web Service**
3. **Connect your GitHub** repository
4. **Configure build settings**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn flow75.wsgi:application`

### Option 3: Heroku (Paid)
1. **Sign up** at [heroku.com](https://heroku.com)
2. **Install Heroku CLI**
3. **Deploy using CLI** or connect GitHub

## 📋 Pre-Deployment Checklist

### ✅ Environment Variables
Set these environment variables in your hosting platform:

```bash
# Required
SECRET_KEY=your-secret-key-here
DEBUG=False
ENVIRONMENT=production
ALLOWED_HOSTS=your-domain.com,www.your-domain.com

# Database (if using external DB)
DATABASE_URL=postgresql://user:password@host:port/dbname

# Optional - Email settings
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=noreply@75flow.com
```

### ✅ Static Files
The project is configured to serve static files using WhiteNoise.

### ✅ Database Migration
Run migrations after deployment:
```bash
python manage.py migrate
```

### ✅ Create Superuser
Create admin user after deployment:
```bash
python manage.py createsuperuser
```

## 🔧 Platform-Specific Instructions

### Railway Deployment
1. **Fork/Clone** this repository to your GitHub
2. **Connect** Railway to your GitHub repo
3. **Add environment variables** in Railway dashboard
4. **Deploy** - Railway will auto-detect Django
5. **Run migrations** in Railway console:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

### Render Deployment
1. **Create new Web Service**
2. **Connect GitHub repository**
3. **Configure settings**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn flow75.wsgi:application`
4. **Add environment variables**
5. **Deploy**

### Heroku Deployment
1. **Install Heroku CLI**
2. **Login**: `heroku login`
3. **Create app**: `heroku create your-app-name`
4. **Set config vars**:
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   heroku config:set ENVIRONMENT=production
   ```
5. **Deploy**: `git push heroku main`
6. **Run migrations**: `heroku run python manage.py migrate`

## 🔐 Security Checklist

- [ ] `DEBUG=False` in production
- [ ] Strong `SECRET_KEY` set
- [ ] `ALLOWED_HOSTS` configured
- [ ] HTTPS enabled
- [ ] Database credentials secured
- [ ] Static files served properly

## 📱 Mobile Optimization

The app is fully mobile-responsive and includes:
- ✅ Bootstrap 5 responsive design
- ✅ Mobile-first CSS
- ✅ Touch-friendly interface
- ✅ Optimized for all screen sizes

## 👥 User Management

### Default Users (for testing)
- **Shruti**: Username: `Shruti`, Password: `Shruti123`
- **Sid**: Username: `Sid`, Password: `Sid123`
- **Sanju**: Username: `Sanju`, Password: `Sanju123`

### Creating New Users
1. **Via Admin Panel**: `/admin/` (requires superuser)
2. **Via Django Shell**:
   ```bash
   python manage.py shell
   from django.contrib.auth.models import User
   User.objects.create_user('username', 'email@example.com', 'password')
   ```

## 🐛 Troubleshooting

### Common Issues
1. **Static files not loading**: Ensure WhiteNoise is configured
2. **Database connection**: Check DATABASE_URL format
3. **Migration errors**: Run `python manage.py migrate --run-syncdb`
4. **Permission errors**: Check file permissions on server

### Logs
- Check platform-specific logs (Railway/Render/Heroku dashboards)
- Django logs are configured in `settings.py`

## 📞 Support

For deployment issues:
1. Check platform documentation
2. Review Django deployment docs
3. Check logs for specific error messages

## 🎯 Post-Deployment

After successful deployment:
1. ✅ Test all features (login, habits, scoreboard)
2. ✅ Verify mobile responsiveness
3. ✅ Check email functionality (if configured)
4. ✅ Monitor performance and logs
5. ✅ Share the URL with Sid and Sanju!

---

**Happy Deploying! 🚀** 