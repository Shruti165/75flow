# Deployment Scripts

This directory contains all deployment-related scripts and configuration files for the 75Flow application.

## Scripts

### Core Deployment
- `deploy.sh` - Main deployment script for general deployment
- `deploy_railway.sh` - Railway-specific deployment with environment setup
- `deploy_one_line.sh` - One-line deployment command for quick deployment
- `deploy_free.sh` - Deployment script optimized for free tier services

### Build and Start
- `build.sh` - Application build script
- `start.sh` - Application startup script for local development
- `set_railway_env.sh` - Railway environment variable setup

### Configuration Files
- `nginx.conf` - Nginx web server configuration
- `75flow.service` - Systemd service file for Linux deployment

## Usage

Run any script from this directory or from the project root:

```bash
# From project root
./scripts/deployment/deploy_railway.sh

# From this directory
./deploy_railway.sh
```

## Railway Deployment

For Railway deployment, the main startup script is located in `../railway/railway_start.py` and is referenced by the root `Procfile`. 