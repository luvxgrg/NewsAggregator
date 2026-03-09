# NewsAggregator 📰

> A Python web scraping application that aggregates news from multiple sources, stores articles in a database, and provides a REST API for searching and filtering news.

## ✨ Features

- **Multi-Source Scraping**: Scrapes news from multiple sources using BeautifulSoup
- **Smart Database Storage**: Stores articles in SQLite for easy access
- **REST API**: Built with Flask/FastAPI for searching and filtering news
- **CLI Support**: Command-line interface for manual scraping operations
- **Configurable**: Easy-to-configure settings for news sources and filters
- **Search & Filter**: Query articles by topic, date, source, and keywords

## 🛠️ Tech Stack

- **Backend**: Python 3.8+
- **Scraping**: BeautifulSoup, Requests
- **Database**: SQLite (articles.db)
- **API**: Flask/Express (if extended)
- **Configuration**: Python config file

## 📦 Installation

### Prerequisites

- Python 3.8+
- pip or conda

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/luvxgrg/NewsAggregator.git
   cd NewsAggregator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure (Optional)**
   Edit `config.py` to customize:
   - News sources
   - Scraping frequency
   - Database location
   - API settings

## 🚀 Usage

### Run the Scraper

```bash
python main.py
```

This will:
- Scrape all configured news sources
- Store articles in `articles.db`
- Start the API server (if configured)

### Query the API

```bash
# Search news by keyword
curl "http://localhost:5000/api/articles?q=technology"

# Filter by source
curl "http://localhost:5000/api/articles?source=bbc"

# Get latest 10 articles
curl "http://localhost:5000/api/articles?limit=10"
```

### Use as a Module

```python
from scraper import scrape_news
from database import get_articles

# Scrape news
articles = scrape_news(source="bbc")

# Query articles
results = get_articles(keyword="python", limit=5)
for article in results:
    print(article['title'])
```

## 📋 Project Structure

```
NewsAggregator/
├── main.py              # Entry point for the application
├── scraper.py           # Web scraping logic
├── api.py              # REST API endpoints
├── database.py         # Database operations
├── config.py           # Configuration settings
├── articles.db         # SQLite database (auto-created)
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## 📄 Configuration

Edit `config.py` to customize:

```python
# News sources to scrape
SOURCES = ['bbc', 'cnn', 'techcrunch']

# Database location
DB_PATH = './articles.db'

# API settings
API_HOST = 'localhost'
API_PORT = 5000
```

## 🔄 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/articles` | Fetch articles with filters |
| GET | `/api/articles/<id>` | Get single article |
| POST | `/api/scrape` | Trigger manual scrape |
| GET | `/api/sources` | List available sources |

## 🧪 Testing

```bash
# Run tests (if available)
python -m pytest tests/
```

## 🐛 Troubleshooting

### Database locked error
- Close any other instances of the app
- Delete `articles.db` and restart

### Scraping fails
- Check internet connection
- Verify source URLs are accessible
- Check `config.py` for correct source settings

### API not responding
- Verify API service is running
- Check port 5000 is not in use
- View logs for error messages

## 📈 Future Enhancements

- [ ] Sentiment analysis for articles
- [ ] Category-based filtering
- [ ] User authentication for saved preferences
- [ ] Web dashboard UI
- [ ] Real-time push notifications
- [ ] Docker containerization

## 📄 License

MIT License - feel free to use this project for personal and commercial purposes.

## 👤 Author

**Lovish** ([@luvxgrg](https://github.com/luvxgrg))

Find me on:
- GitHub: [@luvxgrg](https://github.com/luvxgrg)
- LinkedIn: [Lovish](https://linkedin.com)

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## ⭐ Show your support

If you found this project helpful, please star it on GitHub!

---

**Last Updated**: March 2026
