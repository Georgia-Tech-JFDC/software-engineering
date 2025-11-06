# Quick Start Guide - JFDC Showcase

Your Django app is already set up and running!

## 🚀 View Your App

The server is currently running at:
- **Main site**: http://127.0.0.1:8000/
- **Projects**: http://127.0.0.1:8000/projects/

## 🎨 What You'll See

- **Black & Gold Theme** - Elegant, professional design
- **Landing Page** - Explains JFDC project showcase
- **Projects Page** - Gallery for your completed work
- **Fully Responsive** - Works on all devices

## 📝 Quick Edits

### Update Landing Page Content
Edit: `main/templates/main/home.html`

### Add Real Projects
Edit: `main/templates/main/projects.html`
Replace the placeholder cards with your actual projects.

### Change Colors
Edit: `templates/base.html`
Modify the CSS classes with gold/yellow and black colors.

## 🛑 Stop the Server

The server is running in the background. To stop it:
1. Check running processes: `ps aux | grep runserver`
2. Kill the process: `kill [PID]`

Or restart it:
```bash
cd /Users/arnavmohnalkar/Desktop/JFDC_APP
source venv/bin/activate
python manage.py runserver
```

## 📂 Key Files

- `main/templates/main/home.html` - Landing page
- `main/templates/main/projects.html` - Projects gallery
- `templates/base.html` - Navigation & footer
- `main/views.py` - Page logic
- `main/urls.py` - URL routing

## 🎯 Next Steps

1. **Add Your Projects** - Update the projects page with real content
2. **Customize Text** - Edit the landing page copy
3. **Add Images** - Upload project screenshots to `/static/images/`
4. **Create Models** - Add database models for dynamic projects

---

Simple, clean, and ready to showcase your work! 🎊
