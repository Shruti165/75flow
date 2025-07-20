# Scripts Directory

This directory contains all helper scripts and utilities for the 75Flow Django application, organized by purpose.

## Directory Structure

### `/deployment/`
Contains all deployment-related scripts and configuration files:
- `deploy.sh` - Main deployment script
- `deploy_railway.sh` - Railway-specific deployment
- `deploy_one_line.sh` - One-line deployment command
- `deploy_free.sh` - Free tier deployment
- `build.sh` - Build script
- `start.sh` - Application startup script
- `set_railway_env.sh` - Railway environment setup
- `nginx.conf` - Nginx configuration
- `75flow.service` - Systemd service file

### `/health/`
Contains health check and monitoring scripts:
- `healthcheck.py` - Health check script
- `test_health.py` - Health test script
- `test_port.py` - Port testing utility

### `/railway/`
Contains Railway-specific scripts:
- `railway_start.py` - Railway startup script (referenced by Procfile)
- `railway_health.py` - Railway health check

### `/docs/`
Contains deployment documentation:
- Various deployment guides and troubleshooting docs

## Usage

Most scripts can be run directly from their respective directories. The main Railway startup script is referenced by the root `Procfile` for deployment. 