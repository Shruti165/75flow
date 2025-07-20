# Railway Scripts

This directory contains Railway-specific scripts for the 75Flow application.

## Scripts

### Core Railway Scripts
- `railway_start.py` - Main Railway startup script (referenced by root Procfile)
- `railway_health.py` - Railway-specific health check

## Railway Startup Script

The `railway_start.py` script is the main entry point for Railway deployment. It:

1. Sets up Django environment
2. Configures Gunicorn with Railway-specific settings
3. Binds to `0.0.0.0:$PORT` (Railway provides the PORT environment variable)
4. Handles graceful shutdown
5. Provides detailed logging for debugging

### Configuration
- Binds to host: `0.0.0.0`
- Port: Uses `$PORT` environment variable (Railway provides this)
- Workers: 1 (optimized for Railway)
- Timeout: 120 seconds
- Preload: Enabled for better performance

## Usage

The startup script is automatically called by Railway via the Procfile:
```
web: python scripts/railway/railway_start.py
```

For manual testing:
```bash
python scripts/railway/railway_start.py
```

## Health Check

The `railway_health.py` script provides a simple health check for Railway:
```bash
python scripts/railway/railway_health.py
``` 