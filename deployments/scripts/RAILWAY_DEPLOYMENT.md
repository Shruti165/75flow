# Railway Deployment Guide for 75Flow

## Environment Variables to Set in Railway

Set these environment variables in your Railway project dashboard:

### Required Variables

```
ENVIRONMENT=production
DEBUG=False
```

### Database (Railway will auto-provide this)
```
DATABASE_URL=postgresql://postgres:password@localhost:5432/75flow
```
*Note: Railway automatically provides this when you add a PostgreSQL service*

### Security
```
SECRET_KEY=your-secret-key-here
```
*Generate a secure secret key using: `python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`*

### Allowed Hosts
```
ALLOWED_HOSTS=localhost,127.0.0.1,healthcheck.railway.app,.railway.app,.up.railway.app,*.railway.app
```

### CSRF Trusted Origins
```
CSRF_TRUSTED_ORIGINS=https://*.railway.app,https://*.up.railway.app
```

### Static Files
```
STATIC_URL=/static/
STATIC_ROOT=/app/staticfiles
```

### Media Files
```
MEDIA_URL=/media/
MEDIA_ROOT=/app/media
```

### Security Headers (Railway handles SSL)
```
SECURE_PROXY_SSL_HEADER=('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST=True
USE_X_FORWARDED_PORT=True
```

### Optional: Email Configuration
```
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=noreply@75flow.com
```

## Step-by-Step Deployment

1. **Connect to Railway**
   - Go to [railway.app](https://railway.app)
   - Sign in with GitHub
   - Click "New Project" → "Deploy from GitHub repo"

2. **Select Repository**
   - Choose your 75Flow repository
   - Railway will auto-detect it's a Python project

3. **Add PostgreSQL Database**
   - In your project dashboard, click "New"
   - Select "Database" → "PostgreSQL"
   - Railway will automatically set the `DATABASE_URL` environment variable

4. **Set Environment Variables**
   - Go to your project's "Variables" tab
   - Add all the environment variables listed above
   - Make sure to replace placeholder values with actual values

5. **Deploy**
   - Railway will automatically deploy when you push to your main branch
   - Or click "Deploy" in the dashboard

6. **Health Check**
   - Railway will automatically test the `/health/` endpoint
   - Make sure it returns "OK"

## Important Notes

- **Secret Key**: Generate a new secret key for production. Never use the development one.
- **Database**: Railway will automatically migrate your database on first deploy
- **Static Files**: WhiteNoise will serve static files automatically
- **Health Check**: The `/health/` endpoint is configured to respond to Railway's health checks
- **SSL**: Railway handles SSL certificates automatically

## Troubleshooting

### Health Check Fails
- Make sure the `/health/` endpoint is accessible
- Check that `healthcheck.railway.app` is in `ALLOWED_HOSTS`

### Static Files Not Loading
- Ensure `whitenoise` is in `requirements.txt`
- Check that `STATIC_ROOT` is set correctly

### Database Connection Issues
- Verify `DATABASE_URL` is set correctly
- Check that PostgreSQL service is running

### 500 Errors
- Check Railway logs for detailed error messages
- Ensure all required environment variables are set
- Verify that `DEBUG=False` in production 