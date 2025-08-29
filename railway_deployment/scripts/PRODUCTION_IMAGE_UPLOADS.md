# Production Image Uploads Guide for 75Flow

## Overview
This guide addresses image upload issues in production on Railway and provides solutions to ensure profile images work correctly.

## Current Issues
- Images upload successfully locally but fail in production
- Profile images may not persist after Railway deployments
- File permissions and storage issues in Railway's ephemeral filesystem

## Root Causes

### 1. **Railway's Ephemeral Filesystem**
- Railway uses ephemeral containers that don't persist files between deployments
- Uploaded images are lost when the container restarts or redeploys
- The `media/` directory is recreated on each deployment

### 2. **File Permissions**
- Railway containers may have restricted file permissions
- Media directories might not be writable by the Django application

### 3. **Path Configuration**
- File paths may not be correctly configured for production environment
- URL routing might not work properly in production

## Solutions Implemented

### 1. **Enhanced Media Configuration**
Updated `flow75/settings.py`:
```python
# Configure media files for production
if ENVIRONMENT == 'production':
    MEDIA_ROOT = BASE_DIR / 'media'
    MEDIA_URL = '/media/'
    
    # Ensure media directory exists with proper permissions
    MEDIA_ROOT.mkdir(exist_ok=True)
    
    # Set proper permissions for media directory
    import stat
    MEDIA_ROOT.chmod(stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 777 permissions
    
    # Create profile_images subdirectory with proper permissions
    profile_images_dir = MEDIA_ROOT / 'profile_images'
    profile_images_dir.mkdir(exist_ok=True)
    profile_images_dir.chmod(stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 777 permissions
    
    # File upload settings for production
    FILE_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024  # 10MB
    DATA_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024  # 10MB
    FILE_UPLOAD_PERMISSIONS = 0o666  # Read/write for all
    FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o777  # Full permissions for directories
```

### 2. **Improved Profile Model**
Updated `habits/models.py`:
```python
def profile_image_path(instance, filename):
    """Generate file path for profile images"""
    ext = filename.split('.')[-1]
    filename = f"{instance.user.username}_{instance.user.id}.{ext}"
    return os.path.join('profile_images', filename)

class Profile(models.Model):
    profile_image = models.ImageField(
        upload_to=profile_image_path, 
        null=True, 
        blank=True,
        help_text="Upload a profile picture (JPG, PNG, GIF up to 5MB)"
    )
    
    def save(self, *args, **kwargs):
        # Ensure media directory exists before saving
        if settings.ENVIRONMENT == 'production':
            media_root = settings.MEDIA_ROOT
            profile_images_dir = media_root / 'profile_images'
            profile_images_dir.mkdir(parents=True, exist_ok=True)
            
            # Set proper permissions
            import stat
            profile_images_dir.chmod(stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
        
        super().save(*args, **kwargs)
```

### 3. **Enhanced Form Validation**
Updated `habits/forms.py`:
```python
def clean_profile_image(self):
    """Validate profile image upload"""
    image = self.cleaned_data.get('profile_image')
    
    if image:
        # Check file size (5MB limit)
        if image.size > 5 * 1024 * 1024:
            raise ValidationError("Image file size must be under 5MB.")
        
        # Check file extension
        allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif']
        file_extension = os.path.splitext(image.name)[1].lower()
        
        if file_extension not in allowed_extensions:
            raise ValidationError("Please upload a valid image file (JPG, PNG, or GIF).")
        
        # Check if it's actually an image
        try:
            from PIL import Image
            img = Image.open(image)
            img.verify()
        except Exception:
            raise ValidationError("Please upload a valid image file.")
    
    return image
```

## Testing Image Uploads

### 1. **Run the Test Script**
```bash
python3 test_image_uploads.py
```

This script will:
- Test media directory setup and permissions
- Test image upload functionality
- Check existing profile images
- Validate form handling

### 2. **Manual Testing**
1. Start the development server: `python3 manage.py runserver 8000`
2. Log in and go to profile page
3. Try uploading a profile image
4. Check if the image displays correctly

## Production Deployment Steps

### 1. **Deploy to Railway**
```bash
git add .
git commit -m "Fix image uploads for production"
git push origin main
```

### 2. **Set Environment Variables**
Ensure these are set in Railway:
```
ENVIRONMENT=production
DEBUG=False
DATABASE_URL=your_postgresql_url
```

### 3. **Monitor Deployment**
- Check Railway deployment logs
- Verify the app starts successfully
- Test image uploads after deployment

## Troubleshooting

### **If Images Still Don't Work:**

1. **Check Railway Logs**
   ```bash
   # View Railway logs
   railway logs
   ```

2. **Test File Permissions**
   ```bash
   # Run the test script in production
   python3 test_image_uploads.py
   ```

3. **Verify Media URLs**
   - Try accessing: `your-app.railway.app/media/profile_images/filename.png`
   - Check if the file exists in the container

### **Common Issues and Solutions:**

1. **"Permission Denied" Errors**
   - The media directory doesn't have proper permissions
   - Solution: The updated settings automatically set 777 permissions

2. **"File Not Found" Errors**
   - Images are uploaded but not accessible via URL
   - Solution: Ensure media URLs are properly configured

3. **Images Disappear After Deployment**
   - Railway's ephemeral filesystem deletes files
   - Solution: Consider implementing cloud storage

## Long-term Solutions

### 1. **Cloud Storage (Recommended)**
For production, consider using:
- **AWS S3**: Most popular and reliable
- **Google Cloud Storage**: Good integration with Railway
- **Cloudinary**: Specialized for image management

### 2. **Database Storage**
Store images as base64 strings in the database:
- Pros: Images persist across deployments
- Cons: Increases database size significantly

### 3. **CDN Integration**
Use a CDN for serving images:
- Better performance
- Reduced server load
- Global distribution

## Monitoring and Maintenance

### 1. **Regular Testing**
- Test image uploads after each deployment
- Monitor file storage usage
- Check for broken image links

### 2. **Backup Strategy**
- Regularly backup profile images
- Consider automated backups to cloud storage
- Test restore procedures

### 3. **Performance Monitoring**
- Monitor image loading times
- Track storage usage
- Optimize image sizes if needed

## Next Steps

1. **Deploy the current fixes** and test image uploads
2. **Monitor the application** for any issues
3. **Consider implementing cloud storage** for better reliability
4. **Set up automated testing** for image uploads
5. **Create backup procedures** for profile images

## Support

If you continue to experience issues:
1. Check Railway deployment logs
2. Run the test script to diagnose problems
3. Verify environment variables are set correctly
4. Consider implementing cloud storage solution 