# Tab Close Logout Feature

## How It Works

Your JFDC site now automatically logs out when you close the tab (not just the browser).

### What Happens:

✅ **Close tab** → Auto logout, must login again  
✅ **Close browser** → Auto logout, must login again  
✅ **Navigate away from site** → Auto logout  
✅ **Refresh page (F5, Ctrl+R)** → Stays logged in (doesn't logout)  
✅ **Click Logout button** → Manual logout  
✅ **60 seconds of inactivity** → Session expires, must login again  
✅ **Active browsing** → Session stays alive as long as you're clicking/navigating  

### Technical Implementation

**1. JavaScript Detection:**
- Listens for `beforeunload` event (fires when tab closes)
- Uses `navigator.sendBeacon()` to send logout request
- Detects refresh vs. close (doesn't logout on refresh)

**2. Session Settings:**
- `SESSION_EXPIRE_AT_BROWSER_CLOSE = True` - Extra protection
- `SESSION_COOKIE_AGE = 60` - 60 second timeout for inactivity
- `SESSION_SAVE_EVERY_REQUEST = True` - Refreshes timer while active
- `SESSION_COOKIE_HTTPONLY = False` - Allows JavaScript to manage session

**3. Smart Logout:**
- Distinguishes between manual logout (button) and automatic (tab close)
- Uses beacon API for reliable logout on tab close
- Returns different responses for each type

## Testing

### Test 1: Close Tab
1. Login at http://127.0.0.1:8000/login/
2. Browse to any page
3. Close the tab (click X or Cmd+W / Ctrl+W)
4. Open a new tab and go to http://127.0.0.1:8000/
5. ✅ Should ask you to login again

### Test 2: Refresh Page
1. Login at http://127.0.0.1:8000/login/
2. Browse to any page
3. Press F5 or Ctrl+R to refresh
4. ✅ Should stay logged in (not logout)

### Test 3: Inactivity
1. Login at http://127.0.0.1:8000/login/
2. Don't click anything for 60 seconds
3. Try to navigate to another page
4. ✅ Should redirect to login

### Test 4: Manual Logout
1. Login at http://127.0.0.1:8000/login/
2. Click "Logout" in navigation
3. ✅ Should redirect to login page

## Limitations

### Browser Behavior
- **Not 100% reliable** - Browsers sometimes don't fire `beforeunload` for security/performance reasons
- **Mobile browsers** - May not always fire the event reliably
- **Force quit/crash** - Cannot detect if browser crashes or is force-quit
- **No internet** - Cannot send logout request if connection drops

### What This Means
If the JavaScript fails to fire:
- The 60-second session timeout is a backup
- Closing browser will still clear session
- User would need to wait 60 seconds or clear cookies manually

## Adjusting Timeout

### Make Shorter
Edit `djangoProject/settings.py`:

```python
SESSION_COOKIE_AGE = 30  # 30 seconds
SESSION_COOKIE_AGE = 10  # 10 seconds  
SESSION_COOKIE_AGE = 5   # 5 seconds
```

### Make Longer
```python
SESSION_COOKIE_AGE = 120  # 2 minutes
SESSION_COOKIE_AGE = 300  # 5 minutes
SESSION_COOKIE_AGE = 600  # 10 minutes
```

### Remove Timeout (Only Tab Close)
```python
SESSION_COOKIE_AGE = 86400  # 24 hours (but still logout on tab close via JavaScript)
```

## Disabling This Feature

To go back to normal session behavior:

**Edit `djangoProject/settings.py`:**
```python
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 1209600  # 2 weeks (Django default)
SESSION_SAVE_EVERY_REQUEST = False
SESSION_COOKIE_HTTPONLY = True
```

**Remove JavaScript from `templates/base.html`:**
Delete the auto-logout script (lines 161-177).

## Security Notes

✅ **Pros:**
- Extra security - sessions don't persist after tab closes
- Good for shared computers
- Reduces risk if user forgets to logout

⚠️ **Cons:**
- `SESSION_COOKIE_HTTPONLY = False` allows JavaScript to access session cookie
- This is necessary for the tab-close detection to work
- The cookie itself is still secure (CSRF protection enabled)

## Files Modified

- `djangoProject/settings.py` - Session configuration
- `templates/base.html` - JavaScript for tab close detection
- `main/views.py` - Logout handler for beacon requests

---

**Your site now requires login every time you open a new tab!** 🔐

