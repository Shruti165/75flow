# 75Flow - 75-Day Habit Tracking Challenge

A comprehensive Django web application for tracking habits over a 75-day challenge period. Built with modern UI/UX design and gamification elements to keep users motivated and engaged.

## 🌟 Features

### Core Functionality
- **75-Day Challenge Tracking**: Complete habit tracking system for a 75-day transformation journey
- **Multi-Category Habits**: Support for Reading, Fitness, Nutrition, Wealth, Spiritual, and Fun categories
- **Daily Progress Tracking**: Check off completed habits daily with visual progress indicators
- **Real-time Scoreboard**: Live leaderboard with daily, weekly, and overall rankings
- **User Profiles**: Personalized profiles with avatar uploads and progress statistics

### Advanced Features
- **Category Performance Analysis**: Detailed breakdown of performance across all categories
- **Streak Tracking**: Monitor current and best streaks for motivation
- **Achievement System**: Badges and rewards for consistent performance
- **Responsive Design**: Mobile-friendly interface with modern UI/UX
- **Social Features**: Compare progress with other participants

### Technical Features
- **Django Backend**: Robust Python web framework
- **Bootstrap Frontend**: Modern, responsive design
- **Remix Icons**: Beautiful flat icon system
- **Real-time Updates**: Dynamic progress bars and statistics
- **Media Upload**: Profile image uploads with automatic resizing

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/75flow.git
   cd 75flow
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Visit the application**
   Open your browser and go to `http://127.0.0.1:8000`

## 📁 Project Structure

```
75Flow/
├── 75flow/                 # Main Django project
│   ├── settings.py        # Project settings
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py           # WSGI configuration
├── habits/               # Main app
│   ├── models.py         # Database models
│   ├── views.py          # View logic
│   ├── forms.py          # Form definitions
│   ├── urls.py           # App URL patterns
│   └── management/       # Custom management commands
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── registration/     # Authentication templates
│   └── habits/          # App-specific templates
├── static/              # Static files (CSS, JS, images)
├── media/               # User-uploaded files
├── requirements.txt     # Python dependencies
└── manage.py           # Django management script
```

## 🎯 Usage

### For Users
1. **Register/Login**: Create an account or log in
2. **Set Up Profile**: Upload a profile picture and customize your profile
3. **Add Habits**: Create habits in different categories
4. **Daily Tracking**: Check off completed habits each day
5. **Monitor Progress**: View your progress on the scoreboard and dashboard
6. **Stay Motivated**: Track streaks and achievements

### For Administrators
1. **User Management**: Monitor user activity and progress
2. **Category Management**: Add or modify habit categories
3. **System Monitoring**: Track overall challenge statistics
4. **Data Export**: Export user data and progress reports

## 🛠️ Configuration

### Environment Variables
Create a `.env` file in the project root:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
MEDIA_URL=/media/
STATIC_URL=/static/
```

### Database Configuration
The application uses SQLite by default. For production, configure PostgreSQL or MySQL in settings.py.

## 🚀 Deployment

### Production Deployment
1. **Set DEBUG=False** in settings.py
2. **Configure your database** (PostgreSQL recommended)
3. **Set up static file serving** (nginx + gunicorn)
4. **Configure environment variables**
5. **Run migrations**
6. **Collect static files**: `python manage.py collectstatic`

### Docker Deployment
```bash
docker build -t 75flow .
docker run -p 8000:8000 75flow
```

## 📊 API Endpoints

- `GET /` - Home page
- `GET /scoreboard/` - Leaderboard and rankings
- `GET /daily-tracking/` - Daily habit tracking
- `GET /profile/` - User profile management
- `POST /habits/add/` - Add new habits
- `POST /habits/track/` - Track daily progress

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Django community for the excellent web framework
- Bootstrap team for the responsive CSS framework
- Remix Icon team for the beautiful icon set
- All contributors and users of 75Flow

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Email: support@75flow.com
- Documentation: [docs.75flow.com](https://docs.75flow.com)

---

**Made with ❤️ for habit tracking and personal development** 