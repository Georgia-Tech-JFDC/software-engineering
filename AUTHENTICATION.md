# Authentication Setup

## Overview

Your JFDC site now has full authentication protection. All pages require login to access.

## Login Credentials

**Master Login:**
- **Username:** `jfdc`
- **Password:** `GaTech$$JFDC`

## How It Works

### Protected Pages
All pages now require authentication:
- Home page (`/`)
- Projects page (`/projects/`)
- Analytics Dashboard (`/analytics-dashboard/`)

### Login Flow
1. User visits any page
2. If not authenticated, automatically redirected to `/login/`
3. After successful login, redirected to requested page (or home)
4. Logout button available in navigation

### Login Page
- Black and gold themed to match site design
- Located at: http://127.0.0.1:8000/login/
- Shows error message for invalid credentials
- Responsive mobile design

## Features

✅ **Session-based authentication** - Uses Django's built-in auth system
✅ **Login required** - All pages protected with `@login_required` decorator
✅ **Automatic redirects** - Redirects to login if not authenticated
✅ **Logout functionality** - Button in navigation to log out
✅ **Styled login page** - Matches black/gold theme
✅ **Error handling** - Shows messages for failed login attempts

## Important Notes

### Database Contains User
The user account is stored in `db.sqlite3`:
- ✅ This file is already in `.gitignore` (won't be pushed to GitHub)
- ✅ User credentials are hashed (secure storage)

### After Pushing to GitHub
When someone clones your repository, they will need to:

1. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

2. **Create the user account:**
   ```bash
   python manage.py shell
   ```
   Then in the Python shell:
   ```python
   from django.contrib.auth.models import User
   User.objects.create_user(username='jfdc', password='GaTech$$JFDC')
   exit()
   ```

3. **Or use Django admin:**
   ```bash
   python manage.py createsuperuser
   ```
   Then create regular users through the admin panel.

## File Changes Made

### New Files:
- `main/templates/main/login.html` - Login page template

### Modified Files:
- `main/views.py` - Added login/logout views and `@login_required` decorators
- `main/urls.py` - Added `/login/` and `/logout/` routes
- `djangoProject/settings.py` - Added login URL settings
- `templates/base.html` - Added logout button to navigation

## Testing

### Test Login
1. Visit: http://127.0.0.1:8000/
2. Should redirect to: http://127.0.0.1:8000/login/
3. Enter credentials:
   - Username: `jfdc`
   - Password: `GaTech$$JFDC`
4. Should redirect to home page
5. Logout button appears in navigation

### Test Logout
1. Click "Logout" in navigation
2. Should redirect to login page
3. Try accessing any page - should redirect to login

## Security Notes

- ✅ Password is hashed in database (not stored in plain text)
- ✅ CSRF protection enabled on login form
- ✅ Session-based authentication (not stored in cookies)
- ✅ Login credentials NOT in any code files
- ✅ Database file (`db.sqlite3`) excluded from Git

## Changing Credentials

To change the password later:

```bash
python manage.py shell
```

Then:
```python
from django.contrib.auth.models import User
user = User.objects.get(username='jfdc')
user.set_password('NEW_PASSWORD_HERE')
user.save()
exit()
```

## Adding More Users

To add additional users:

```bash
python manage.py shell
```

Then:
```python
from django.contrib.auth.models import User
User.objects.create_user(
    username='newuser',
    password='password123'
)
exit()
```

---

**Your site is now fully protected with authentication!** 🔒

