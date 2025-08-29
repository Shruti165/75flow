# PostgreSQL Setup on Railway - 75Flow

This guide will help you set up PostgreSQL on Railway for production while keeping SQLite for local development.

## Current Setup

Your Django app is already configured to:
- Use SQLite for local development (default)
- Use PostgreSQL for production (when `DATABASE_URL` is provided)
- Handle environment-specific settings automatically

## Step 1: Add PostgreSQL Service on Railway

1. **Go to your Railway project dashboard**
2. **Click "New Service"**
3. **Select "Database" → "PostgreSQL"**
4. **Give it a name like "75flow-db"**
5. **Click "Deploy"**

## Step 2: Railway Environment Variables

Once PostgreSQL is added, Railway will automatically provide these variables to your Django app:

### Auto-Provided by Railway:
- `DATABASE_URL` - PostgreSQL connection string
- `PORT` - Application port
- `RAILWAY_STATIC_URL` - Static files URL

### Manual Variables to Set:
```
ENVIRONMENT=production
DEBUG=False
SECRET_KEY=your-super-secret-key-here
ALLOWED_HOSTS=*.railway.app
CSRF_TRUSTED_ORIGINS=https://*.railway.app
```

## Step 3: Database Migration Process

### Option A: Using the Management Command (Recommended)
```bash
# This will run automatically during deployment
railway run python manage.py migrate_to_postgres
```

### Option B: Manual Migration
```bash
# Run migrations
railway run python manage.py migrate

# Create superuser
railway run python manage.py createsuperuser

# Load dummy data
railway run python manage.py populate_dummy_data
```

## Step 4: Verify Database Connection

### Check Database Status:
```bash
railway run python manage.py dbshell
```

### View Database Logs:
```bash
railway logs
```

## Step 5: Local Development (SQLite)

For local development, continue using SQLite:

```bash
# Local development server
python3 manage.py runserver

# Local database operations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py populate_dummy_data
```

## Environment Variables Summary

### Local Development (.env file - optional):
```
ENVIRONMENT=development
DEBUG=True
SECRET_KEY=dev-secret-key
DATABASE_URL=sqlite:///db.sqlite3
```

### Production (Railway Variables):
```
ENVIRONMENT=production
DEBUG=False
SECRET_KEY=your-production-secret-key
DATABASE_URL=postgresql://... (auto-provided by Railway)
ALLOWED_HOSTS=*.railway.app
CSRF_TRUSTED_ORIGINS=https://*.railway.app
```

## Database Backup and Restore

### Backup PostgreSQL (Production):
```bash
railway run python manage.py dumpdata --exclude auth.permission --exclude contenttypes > backup.json
```

### Restore to Local SQLite:
```bash
python3 manage.py loaddata backup.json
```

## Troubleshooting

### Common Issues:

1. **Connection Refused**: Check if PostgreSQL service is running
2. **Migration Errors**: Run `railway run python manage.py migrate --fake-initial`
3. **Static Files**: Railway handles this automatically with WhiteNoise

### Useful Commands:
```bash
# Check Railway status
railway status

# View logs
railway logs

# Connect to database
railway connect

# Open app
railway open
```

## Security Notes

1. **Never commit sensitive data** to Git
2. **Use strong SECRET_KEY** in production
3. **Enable HTTPS** (Railway handles this)
4. **Regular backups** of PostgreSQL data

## Next Steps

1. Deploy your app to Railway
2. Add PostgreSQL service
3. Set environment variables
4. Run migrations
5. Test the application
6. Share the URL with Sid and Sanju!

Your Django app is already configured to handle this setup automatically! 🚀 