# 🚀 Render Deployment Configuration

This folder contains all the necessary files for deploying the 75Flow Django application to Render.

## 📁 Files Overview

### **Core Deployment Files**
- **`Procfile`** - Specifies the web process command for Render
- **`render.yaml`** - Render service configuration and environment variables
- **`build.sh`** - Build script executed during deployment
- **`runtime.txt`** - Python version specification (3.11.0)

### **System Dependencies**
- **`packages.txt`** - System-level packages required for Pillow and other dependencies
- **`.python-version`** - Python version for development tools

### **Requirements Files**
- **`requirements.txt`** - Main Python dependencies
- **`requirements-dev.txt`** - Development dependencies (without Pillow)
- **`requirements-py313.txt`** - Python 3.13 optimized dependencies

## 🔧 Deployment Process

1. **Connect Repository**: Link your GitHub repo to Render
2. **Auto-Detection**: Render will automatically detect the configuration
3. **Build Process**: 
   - Installs system dependencies from `packages.txt`
   - Detects Python version and chooses appropriate requirements
   - Installs Python dependencies
   - Collects static files
   - Runs database migrations

## 🌐 Environment Variables

The following environment variables are configured in `render.yaml`:
- `PYTHON_VERSION`: 3.11.0
- `DEBUG`: false
- `ALLOWED_HOSTS`: .onrender.com
- `ENVIRONMENT`: production
- `PORT`: 10000

## 📦 System Dependencies

Essential system packages for Pillow and other libraries:
- Image processing libraries (libjpeg, libpng, libfreetype)
- Build tools (build-essential, python3.11-dev)
- Security libraries (libffi-dev, libssl-dev)

## 🚀 Quick Deploy

1. Push your code to GitHub
2. Create new Web Service on Render
3. Connect your repository
4. Render will automatically use these configuration files
5. Deploy and enjoy! 🎉

## 🔍 Troubleshooting

If you encounter build issues:
- Check the build logs in Render dashboard
- Verify Python version compatibility
- Ensure all system dependencies are listed in `packages.txt`
- The build script includes fallback options for Pillow installation
