# Health Check Scripts

This directory contains health check and monitoring scripts for the 75Flow application.

## Scripts

### Health Checks
- `healthcheck.py` - Main health check script for application monitoring
- `test_health.py` - Health test script for development testing
- `test_port.py` - Port testing utility to verify application binding

## Usage

### Health Check
```bash
# Run health check
python scripts/health/healthcheck.py

# Test health endpoint
python scripts/health/test_health.py
```

### Port Testing
```bash
# Test if application is binding to correct port
python scripts/health/test_port.py
```

## Integration

These scripts can be used for:
- Monitoring application health in production
- Testing deployment configurations
- Verifying port binding before deployment
- CI/CD pipeline health checks 