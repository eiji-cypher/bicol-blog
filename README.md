# Bicol Region Blog

A travel blog celebrating the culture, food, and legends of Bicol, Philippines.

**🚀 The system is fully deployed! View the live site here: [Insert Live Site URL]**

## Features
- **3 destinations**: Legazpi City, Naga City, Sorsogon City
- **Top Attractions**, **Local Delicacies**, **Festivals**, and **Myths & Legends** for each
- Editorial magazine aesthetic with responsive design
- Flask backend, pure HTML/CSS/JS frontend

## Local Development

```bash
pip install -r requirements.txt
python app.py
```
Open http://localhost:5000

## Deployment Reference

This project is fully deployed and hosted on Vercel. To deploy updates or launch your own instance:

### Option 1: Vercel CLI
```bash
npm i -g vercel
vercel login
vercel --prod
```

### Option 2: Vercel Dashboard
1. Push this project to GitHub
2. Go to https://vercel.com/new
3. Import your GitHub repository
4. Vercel auto-detects Python — click **Deploy**

That's it! Vercel handles everything.

## Project Structure
```
bicol-blog/
├── app.py              # Flask app + all data
├── vercel.json         # Vercel deployment config
├── requirements.txt
├── templates/
│   ├── base.html       # Shared layout
│   ├── index.html      # Homepage
│   └── place.html      # Individual place page
└── static/
    ├── css/style.css
    └── js/main.js
```

## Adding More Places
In `app.py`, add a new entry to the `places` dict with the same structure as existing entries. The site auto-generates pages and navigation.
