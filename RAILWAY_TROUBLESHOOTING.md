# Railway Deployment Troubleshooting Guide

## Common Issues and Solutions

### 1. Bad Request (400) Error

**Symptoms:** Getting "Bad Request" when accessing the app URL

**Solutions:**
- Check CSRF_TRUSTED_ORIGINS in Railway environment variables
- Ensure ALLOWED_HOSTS includes your Railway domain
- Verify SSL settings are properly configured

**Quick Fix:**
```bash
# Set these environment variables in Railway dashboard
ALLOWED_HOSTS=flow75.up.railway.app,*.railway.app
CSRF_TRUSTED_ORIGINS=https://flow75.up.railway.app,https://*.railway.app
```

### 2. Database Connection Issues

**Symptoms:** Database errors or migration failures

**Solutions:**
- Ensure PostgreSQL is added to your Railway project
- Check DATABASE_URL environment variable
- Run migrations: `railway run python manage.py migrate`

### 3. Static Files Not Loading

**Symptoms:** CSS/JS files not loading, broken styling

**Solutions:**
- Ensure WhiteNoise is in requirements.txt
- Check STATIC_ROOT and STATIC_URL settings
- Run: `railway run python manage.py collectstatic --noinput`

### 4. Environment Variables

**Required Railway Environment Variables:**
```
ENVIRONMENT=production
DEBUG=False
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://... (auto-provided by Railway)
ALLOWED_HOSTS=flow75.up.railway.app,*.railway.app
CSRF_TRUSTED_ORIGINS=https://flow75.up.railway.app,https://*.railway.app
```

### 5. Health Check Endpoint

**Test the deployment:**
```bash
curl https://flow75.up.railway.app/health/
```

**Expected response:** `{"status": "healthy", "timestamp": "..."}`

### 6. Common Commands

**View logs:**
```bash
railway logs
```

**Check status:**
```bash
railway status
```

**Run Django commands:**
```bash
railway run python manage.py migrate
railway run python manage.py createsuperuser
railway run python manage.py collectstatic
```

**Connect to database:**
```bash
railway connect
```

### 7. Deployment Process

**Manual deployment:**
```bash
# 1. Commit changes
git add .
git commit -m "Deploy update"
git push origin main

# 2. Deploy to Railway
railway up

# 3. Run migrations
railway run python manage.py migrate

# 4. Collect static files
railway run python manage.py collectstatic --noinput
```

**Using the deployment script:**
```bash
./deploy_railway.sh
```

### 8. Performance Issues

**Symptoms:** Slow loading times

**Solutions:**
- Check Railway plan (free tier has limitations)
- Optimize database queries
- Use caching where appropriate
- Monitor Railway metrics

### 9. SSL/HTTPS Issues

**Symptoms:** Mixed content warnings or SSL errors

**Solutions:**
- Ensure all external resources use HTTPS
- Check SECURE_SSL_REDIRECT setting
- Verify Railway's automatic SSL configuration

### 10. Memory Issues

**Symptoms:** App crashes or timeouts

**Solutions:**
- Check Railway logs for memory usage
- Optimize Django settings for production
- Consider upgrading Railway plan if needed

## Getting Help

1. **Check Railway logs:** `railway logs`
2. **Test locally:** Ensure app works locally first
3. **Railway documentation:** https://docs.railway.app/
4. **Django deployment guide:** https://docs.djangoproject.com/en/5.1/howto/deployment/

## Quick Health Check

Run this to verify everything is working:

```bash
# Test health endpoint
curl -s https://flow75.up.railway.app/health/

# Test main page (should redirect to login)
curl -s -o /dev/null -w "%{http_code}" https://flow75.up.railway.app/

# Check Railway status
railway status
```

Expected results:
- Health endpoint: `{"status": "healthy", "timestamp": "..."}`
- Main page: `302` (redirect to login)
- Railway status: `Deployed` or `Building` 