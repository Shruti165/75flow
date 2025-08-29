# 🔄 Automatic Data Refresh on Render

## **Overview**
Every time you **deploy** or **restart** your Render service, all your local data is automatically loaded fresh. This ensures your deployed application always has the latest data structure and habits.

## **How It Works**

### **1. Automatic Execution**
- **On Deploy**: When you push code changes to Git and Render rebuilds
- **On Restart**: When you manually restart the service from Render dashboard
- **On Manual Deploy**: When you trigger a new deployment

### **2. Data Refresh Process**
The `refresh_data.py` script automatically:
1. 🧹 **Clears existing data** (habits, profiles, categories, completion records)
2. 👑 **Ensures admin user exists**
3. 📥 **Imports fresh categories** (Reading, Fitness, Nutrition, Wealth, Spiritual, Fun)
4. 👥 **Imports all users** (Sid, Shruti, Sanju, admin, Sachin, Defni, Pooja)
5. 🎯 **Imports ALL 187+ habits** distributed across users
6. 🔐 **Resets passwords** to usernames for easy access

### **3. Script Priority Order**
1. **`refresh_data.py`** (Recommended - Complete refresh)
2. **`import_local_data.py`** (Fallback - Import from local export)
3. **`import_all_local_data.py`** (Fallback - Hardcoded data)
4. **`create_default_users`** (Last resort - Basic users only)

## **Benefits**

✅ **Always Fresh Data**: No stale data on deployments
✅ **Consistent State**: Every restart gives you the same clean data
✅ **No Manual Work**: Automatic execution on every deploy/restart
✅ **Complete Reset**: Clears old data and imports fresh data
✅ **Easy Access**: All users can login with username=password

## **What Gets Refreshed**

### **Users & Profiles**
- All 7 users with their profiles
- Admin user with full permissions
- All passwords reset to usernames

### **Categories**
- 6 categories with colors
- Reading, Fitness, Nutrition, Wealth, Spiritual, Fun

### **Habits**
- **Shruti**: 40+ comprehensive habits
- **Admin**: Same habits as Shruti
- **Other users**: 20+ habits each
- **Total**: 187+ habits across all users

## **Usage**

### **Automatic (Recommended)**
Just deploy or restart your service - data refresh happens automatically!

### **Manual Execution**
```bash
cd render_deployment
python refresh_data.py
```

### **Force Refresh**
If you need to refresh data without deploying:
1. Go to Render dashboard
2. Click "Restart" on your service
3. Data will refresh automatically

## **Login Credentials After Refresh**

| Username | Password | Role |
|----------|----------|------|
| `admin` | `admin` | Superuser/Admin |
| `Shruti` | `Shruti` | Participant |
| `Sid` | `Sid` | Participant |
| `Sanju` | `Sanju` | Participant |
| `Sachin` | `Sachin` | Participant |
| `Defni` | `Defni` | Participant |
| `Pooja` | `Pooja` | Participant |

## **Monitoring**

### **Build Logs**
Check Render build logs to see the refresh process:
```
🔄 Running data refresh on every deploy/restart...
🧹 Clearing existing data...
📥 Importing categories...
📥 Importing users and profiles...
📥 Importing ALL habits...
🔐 Resetting user passwords...
🎉 Data refresh completed successfully!
```

### **Verification**
After refresh, verify:
1. All users can login
2. All categories are present
3. All habits are loaded
4. Passwords work correctly

## **Troubleshooting**

### **If Refresh Fails**
1. Check build logs for errors
2. Ensure all required files are in `render_deployment/`
3. Verify Python dependencies are installed
4. Check database connectivity

### **Manual Recovery**
If automatic refresh fails:
```bash
cd render_deployment
python import_all_local_data.py  # Fallback script
```

## **File Structure**
```
render_deployment/
├── build.sh                    # Build script (runs refresh automatically)
├── refresh_data.py            # Main refresh script (recommended)
├── import_local_data.py       # Fallback import script
├── import_all_local_data.py   # Fallback hardcoded data
└── AUTO_DATA_REFRESH.md       # This documentation
```

## **Best Practices**

1. **Always use `refresh_data.py`** for consistent deployments
2. **Test locally** before deploying to production
3. **Monitor build logs** to ensure refresh completes successfully
4. **Keep backup** of your local data export
5. **Use Git** to track changes to refresh scripts

---

**🎉 Result**: Every deploy/restart gives you a fresh, clean application with all your data loaded automatically!
