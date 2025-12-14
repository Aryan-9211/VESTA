# VESTA - AI-Powered Outfit Analyzer

An intelligent web application that uses AI to analyze outfit photos and provide personalized fashion recommendations.

## Features

- 📸 **Photo Upload**: Upload outfit images for analysis
- 🤖 **AI-Powered Analysis**: Uses OpenAI GPT-4 Vision to rate outfits (1-10)
- 💡 **Smart Suggestions**: Get detailed improvement recommendations
- 🎯 **Context-Aware**: Takes into account occasion, gender, and age
- 🎨 **Beautiful UI**: Modern, responsive design with Bootstrap 5

## Tech Stack

- **Backend**: Django 4.2
- **AI**: OpenAI GPT-4 Vision API
- **Frontend**: Bootstrap 5, vanilla JavaScript
- **Database**: SQLite (development)

## Project Structure

```
VESTA/
├── vesta/                      # Django project settings
│   ├── __init__.py
│   ├── settings.py            # Main configuration
│   ├── urls.py                # Root URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── outfit_analyzer/           # Main Django app
│   ├── services/              # Business logic layer
│   │   ├── __init__.py
│   │   └── ai_analyzer.py     # AI analysis service
│   ├── __init__.py
│   ├── admin.py               # Admin interface
│   ├── apps.py
│   ├── forms.py               # Form definitions
│   ├── models.py              # Database models
│   ├── urls.py                # App URL routing
│   └── views.py               # View controllers
├── templates/                 # HTML templates
│   ├── base.html              # Base template
│   └── outfit_analyzer/
│       ├── home.html          # Upload page
│       └── result.html        # Results page
├── static/                    # Static files (CSS, JS, images)
├── media/                     # User uploads (auto-created)
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
├── .env.example               # Environment variables template
├── .gitignore
└── README.md
```

## Setup Instructions

### 1. Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### 2. Installation

```bash
# Clone or navigate to the project directory
cd VESTA

# Create a virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=sk-your-actual-api-key-here
```

### 4. Database Setup

```bash
# Run migrations to create database tables
python manage.py makemigrations
python manage.py migrate

# Create a superuser (optional, for admin access)
python manage.py createsuperuser
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your browser!

## Usage

1. **Upload a Photo**: Click to upload an outfit image
2. **Provide Context**: Select occasion, gender, and enter age
3. **Analyze**: Click "Analyze My Outfit"
4. **View Results**: See your rating and personalized suggestions

## API Costs

This application uses OpenAI's GPT-4 Vision API. Approximate costs:
- ~$0.01-0.05 per image analysis
- Monitor usage at [OpenAI Dashboard](https://platform.openai.com/usage)

## Future Enhancements (V2+)

- User authentication and history
- Wardrobe management
- Shopping recommendations
- Social sharing features
- Mobile app
- Custom ML model training

## Development

### Running Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Accessing Admin Panel

```bash
# Create superuser if not done
python manage.py createsuperuser

# Visit http://localhost:8000/admin
```

### Adding New Features

The project structure is designed for easy extension:
- Add new services in `outfit_analyzer/services/`
- Add new models in `outfit_analyzer/models.py`
- Add new views in `outfit_analyzer/views.py`
- Add new templates in `templates/outfit_analyzer/`

## License

This project is for educational purposes.

## Support

For issues or questions, please create an issue in the repository.

---

Built with ❤️ by Aryan M.
