# Adding Your Tableau Dashboard

## Quick Setup Guide

Your Analytics Dashboard page is ready! Here's how to add your Tableau dashboard:

### Step 1: Get Your Tableau Embed Code

**From Tableau Public:**
1. Go to your dashboard on Tableau Public
2. Click the "Share" button
3. Copy the embed code

**From Tableau Server:**
1. Open your dashboard
2. Click "Share" → "Embed Code"
3. Copy the provided code

### Step 2: Add the Code to Your Page

1. Open the file: `main/templates/main/analytics_dashboard.html`
2. Find this section (around line 60-85):
   ```html
   <!-- Dashboard Container -->
   <div class="bg-gray-900 border border-yellow-600 rounded-xl p-8">
       <div class="text-center py-20">
           <!-- PLACEHOLDER CONTENT HERE -->
       </div>
   </div>
   ```
3. Replace the inner `<div class="text-center py-20">` content with your Tableau embed code

### Step 3: Example Tableau Embed

Your Tableau embed code will look something like this:

```html
<div class="bg-gray-900 border border-yellow-600 rounded-xl p-8">
    <!-- Paste your Tableau embed code here -->
    <div class='tableauPlaceholder' id='viz1234567890' style='position: relative'>
        <noscript>
            <a href='#'>
                <img alt='Dashboard' src='https://public.tableau.com/...' style='border: none' />
            </a>
        </noscript>
        <object class='tableauViz' style='display:none;'>
            <param name='host_url' value='https://public.tableau.com/' />
            <param name='embed_code_version' value='3' />
            <param name='site_root' value='' />
            <param name='name' value='YourDashboard/Dashboard1' />
            <param name='tabs' value='no' />
            <param name='toolbar' value='yes' />
            <param name='static_image' value='https://public.tableau.com/...' />
            <param name='animate_transition' value='yes' />
            <param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' />
            <param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' />
            <param name='language' value='en-US' />
        </object>
    </div>
    <script type='text/javascript'>
        var divElement = document.getElementById('viz1234567890');
        var vizElement = divElement.getElementsByTagName('object')[0];
        if (divElement.offsetWidth > 800) {
            vizElement.style.width='100%';
            vizElement.style.height=(divElement.offsetWidth*0.75)+'px';
        } else if (divElement.offsetWidth > 500) {
            vizElement.style.width='100%';
            vizElement.style.height=(divElement.offsetWidth*0.75)+'px';
        } else {
            vizElement.style.width='100%';
            vizElement.style.height='727px';
        }
        var scriptElement = document.createElement('script');
        scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
        vizElement.parentNode.insertBefore(scriptElement, vizElement);
    </script>
</div>
```

### Step 4: Customize Styling (Optional)

To make the dashboard fit better with the black and gold theme, you can adjust:

```html
<!-- Add custom styling -->
<style>
    .tableauViz {
        border-radius: 8px;
        overflow: hidden;
    }
</style>
```

### Step 5: Test Your Dashboard

1. Save the file
2. The Django server should auto-reload
3. Visit: http://127.0.0.1:8000/analytics-dashboard/
4. Your Tableau dashboard should now be embedded!

## Tips for Best Results

### Responsive Design
- Set width to '100%' for mobile-friendly display
- Use relative height calculations
- Test on different screen sizes

### Performance
- Consider using Tableau's "static_image" parameter for faster loading
- Enable caching if using Tableau Server

### Styling
- The dashboard container has the black/gold theme applied
- You can modify the border colors in the HTML
- Adjust padding in the parent div as needed

## Current Page Structure

```
Analytics Dashboard Page
├── Header (Black bg, gold title)
├── Dashboard Container (Gray bg, gold border)
│   └── [Your Tableau embed goes here]
├── Quick Stats (3 cards - optional, can remove)
└── About Section (Gray bg - optional, can remove)
```

## Troubleshooting

**Dashboard not showing?**
- Check browser console for errors
- Verify the Tableau embed URL is correct
- Ensure JavaScript is enabled
- Check if your Tableau dashboard is public

**Responsive issues?**
- Adjust the width/height calculations in the script
- Test with Tableau's responsive settings
- Use `device='desktop'` or `device='phone'` parameters

## Quick Access

- **Dashboard URL**: http://127.0.0.1:8000/analytics-dashboard/
- **Template File**: `main/templates/main/analytics_dashboard.html`
- **View File**: `main/views.py` (line 14)

---

Need help? The placeholder page includes instructions and is ready for your Tableau dashboard!

