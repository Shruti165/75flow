# Railway Deployment Troubleshooting Guide

## Common Railway Deployment Errors

### 1. "There was an error deploying from source"

**Possible Causes:**
- Missing dependencies
- Python version incompatibility
- Build script errors
- Static files collection issues

**Solutions:**

#### A. Check Railway Logs
```bash
railway logs
```

#### B. Verify Environment Variables
Make sure these are set in Railway:
```
ENVIRONMENT=production
DEBUG=False
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=*.railway.app
CSRF_TRUSTED_ORIGINS=https://*.railway.app
```

#### C. Check Build Process
1. **Static Files**: Ensure `python manage.py collectstatic --noinput` runs
2. **Migrations**: Ensure `python manage.py migrate` runs
3. **Dependencies**: Check if all packages install correctly

### 2. Database Connection Issues

**Symptoms:**
- App starts but shows database errors
- Migration failures

**Solutions:**
```bash
# Check if PostgreSQL is connected
railway run python manage.py dbshell

# Run migrations manually
railway run python manage.py migrate

# Check database status
railway run python manage.py check --database default
```

### 3. Static Files Not Loading

**Symptoms:**
- CSS/JS not loading
- 404 errors for static files

**Solutions:**
1. **Check WhiteNoise**: Ensure whitenoise is installed
2. **Collect Static**: Run `python manage.py collectstatic --noinput`
3. **Check STATIC_ROOT**: Verify static files are in the correct directory

### 4. Port Binding Issues

**Symptoms:**
- App won't start
- Port already in use errors

**Solutions:**
1. **Check Procfile**: Ensure it uses `$PORT` environment variable
2. **Verify Gunicorn**: Check gunicorn configuration

## Manual Deployment Steps

### Step 1: Prepare Your Code
```bash
# Ensure all changes are committed
git add .
git commit -m "Fix deployment issues"
git push
```

### Step 2: Railway Dashboard Setup
1. Go to Railway dashboard
2. Create new project
3. Connect your GitHub repository
4. Add PostgreSQL service
5. Set environment variables

### Step 3: Environment Variables
Set these in Railway dashboard:
```
ENVIRONMENT=production
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=*.railway.app
CSRF_TRUSTED_ORIGINS=https://*.railway.app
```

### Step 4: Deploy
1. Railway will automatically detect Django
2. It will run the build process
3. Check logs for any errors

## Debugging Commands

### Check Railway Status
```bash
railway status
```

### View Logs
```bash
railway logs
```

### Connect to Database
```bash
railway connect
```

### Run Commands
```bash
railway run python manage.py migrate
railway run python manage.py createsuperuser
railway run python manage.py collectstatic --noinput
```

### Check App Health
```bash
curl https://your-app.railway.app/health/
```

## Common Fixes

### 1. Update Requirements.txt
If you get dependency errors, update requirements.txt:
```
Django==5.1.0
Pillow==10.1.0
python-decouple==3.8
gunicorn==21.2.0
whitenoise==6.6.0
psycopg2-binary==2.9.9
dj-database-url==2.1.0
```

### 2. Fix Procfile
Ensure Procfile contains:
```
web: gunicorn flow75.wsgi:application --bind 0.0.0.0:$PORT --workers 2 --timeout 120 --log-file -
```

### 3. Add Runtime.txt
Create runtime.txt with:
```
python-3.10.10
```

### 4. Check Settings
Ensure settings.py handles:
- Environment variables properly
- Database configuration
- Static files configuration
- Security settings

## Still Having Issues?

1. **Check Railway Status**: Visit https://status.railway.app/
2. **Review Logs**: Look for specific error messages
3. **Test Locally**: Ensure app works locally first
4. **Contact Support**: Use Railway's support if needed

## Success Checklist

- [ ] App deploys without errors
- [ ] Health check endpoint responds
- [ ] Database migrations run successfully
- [ ] Static files load properly
- [ ] Admin panel accessible
- [ ] All features working
- [ ] HTTPS enabled
- [ ] Environment variables set correctly 