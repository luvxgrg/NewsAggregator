# Configuration settings for NewsAggregator

NEWS_SOURCES = {
    'bbc': {
        'url': 'https://www.bbc.com/news',
        'article_selector': 'article h2 a::text',
        'link_selector': 'article h2 a::attr(href)',
    },
    'techcrunch': {
        'url': 'https://techcrunch.com',
        'article_selector': 'h2.post-block__title a::text',
        'link_selector': 'h2.post-block__title a::attr(href)',
    },
    'hackernews': {
        'url': 'https://news.ycombinator.com',
        'article_selector': 'span.titleline a::text',
        'link_selector': 'span.titleline a::attr(href)',
    }
}

DATABASE_PATH = 'articles.db'
MAX_ARTICLES_PER_SOURCE = 50
FLASK_PORT = 5000
FLASK_DEBUG = True
