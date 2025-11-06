# JFDC Project Showcase

A sleek, modern Django web application with a black and gold theme, designed to showcase JFDC projects.

## Features

- 🎨 Elegant black and gold color scheme
- 📱 Fully responsive design
- 🚀 Fast and optimized
- 🎯 Clean, minimalist layout
- 💫 Smooth animations and transitions

## Pages

1. **Home** - Landing page explaining JFDC's project showcase
2. **Projects** - Gallery view of completed and upcoming projects

## Tech Stack

- **Backend**: Django 4.2.26
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Database**: SQLite (development)
- **Icons**: Font Awesome 6
- **Fonts**: Google Fonts (Inter)

## Color Scheme

- **Primary**: Black (#000000)
- **Accent**: Gold (#d4af37)
- **Text**: White (#ffffff)
- **Secondary**: Gray shades

## Quick Start

### Prerequisites
- Python 3.8 or higher

### Steps

1. **Navigate to project directory**
   ```bash
   cd /Users/arnavmohnalkar/Desktop/JFDC_APP
   ```

2. **Activate virtual environment**
   ```bash
   source venv/bin/activate
   ```

3. **Run the server**
   ```bash
   python manage.py runserver
   ```

4. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Projects: http://127.0.0.1:8000/projects/

## Project Structure

```
JFDC_APP/
├── djangoProject/          # Project settings
│   ├── settings.py        # Django settings
│   └── urls.py            # Main URL configuration
├── main/                   # Main application
│   ├── templates/         # HTML templates
│   │   └── main/
│   │       ├── home.html       # Landing page
│   │       └── projects.html   # Projects showcase
│   ├── views.py           # View functions
│   └── urls.py            # App URL configuration
├── templates/             # Base templates
│   └── base.html          # Base template with nav/footer
├── static/                # Static files (CSS, JS, images)
├── venv/                  # Virtual environment
└── manage.py              # Django management script
```

## Customization

### Colors
The app uses a black and gold theme. To change colors, modify these classes in templates:
- `gold-bg` → Gold gradient background
- `gradient-text` → Gold gradient text
- `border-yellow-600` → Gold border
- `text-yellow-500` → Gold text

### Content
Update the content in the templates:
- `templates/base.html` - Navigation and footer
- `main/templates/main/home.html` - Landing page
- `main/templates/main/projects.html` - Projects gallery

### Adding Projects
To add real projects, edit `main/templates/main/projects.html` and replace the placeholder cards with actual project information.

## Available URLs

- `/` - Home page (landing)
- `/projects/` - Projects showcase page

## Development

### Running Tests
```bash
python manage.py test
```

### Making Changes
The development server automatically reloads when you make changes to the code.

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Purpose

This application serves as a digital showcase for projects created by JFDC. It provides a clean, professional platform to display completed work and upcoming projects.

---

Built with Django and Tailwind CSS
