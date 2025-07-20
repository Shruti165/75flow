# Data Migration Guide: SQLite to Railway PostgreSQL

## Overview
This guide will help you migrate your 75Flow data from the local SQLite database to Railway PostgreSQL for production use.

## Current Status
✅ **Backup Completed**: Your SQLite data has been successfully backed up to the `migration_backup/` directory:
- `auth_user.json` - User accounts
- `habits_category.json` - Habit categories
- `habits_habit.json` - All habits
- `habits_habitday.json` - Habit completion records
- `habits_profile.json` - User profiles

## Step-by-Step Migration Process

### Step 1: Get Railway Database URL
1. Go to your Railway dashboard: https://railway.app/dashboard
2. Select your 75Flow project
3. Go to the "Variables" tab
4. Copy the `DATABASE_URL` value
5. The URL should look like:
   ```
   postgresql://postgres:YOUR_PASSWORD@mainline.proxy.rlwy.net:22310/railway
   ```

### Step 2: Set Environment Variable
Set the DATABASE_URL as an environment variable:
```bash
export DATABASE_URL='your_railway_database_url_here'
```

### Step 3: Run Migration
Execute the migration script:
```bash
python3 migrate_to_railway.py
```

## What the Migration Does

1. **Connects to Railway PostgreSQL** using your DATABASE_URL
2. **Runs Django migrations** to create all necessary tables
3. **Loads your data** in the correct order:
   - Users first (for foreign key relationships)
   - Categories
   - Profiles
   - Habits
   - Habit completion records
4. **Verifies the migration** by counting records

## Expected Results

After successful migration, you should see:
- All 3 users migrated
- All 6 categories migrated
- All 190 habits migrated
- All 109 habit completion records migrated
- All 3 profiles migrated

## Troubleshooting

### Connection Issues
If you get connection errors:
1. Verify your DATABASE_URL is correct
2. Check that your Railway PostgreSQL service is running
3. Ensure the password in the URL is correct

### Migration Errors
If migrations fail:
1. Check that all required packages are installed:
   ```bash
   pip3 install psycopg2-binary dj-database-url
   ```
2. Verify your Django settings are configured for PostgreSQL

### Data Loading Errors
If data loading fails:
1. Check that the backup files exist in `migration_backup/`
2. Ensure the Railway database is empty (or use `--flush` option)
3. Verify foreign key relationships are correct

## Verification

After migration, you can verify the data by:
1. Checking the migration script output
2. Connecting to your Railway app and testing functionality
3. Comparing record counts with your local database

## Backup Safety

Your original SQLite database (`db.sqlite3`) remains unchanged. The backup files in `migration_backup/` contain all your data in JSON format for safekeeping.

## Next Steps

After successful migration:
1. Deploy your app to Railway
2. Test all functionality with the new PostgreSQL database
3. Keep the backup files for future reference
4. Consider setting up automated backups for the production database

## Files Created

- `migration_backup/` - Directory containing all backup files
- `migrate_to_railway.py` - Migration script
- `MIGRATION_INSTRUCTIONS.md` - This guide

## Support

If you encounter any issues during migration, check:
1. Railway documentation: https://docs.railway.app/
2. Django database migration docs: https://docs.djangoproject.com/en/5.1/topics/migrations/
3. Your Railway project logs for any error messages 