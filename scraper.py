"""
Simplified Web scraper for news articles using requests and BeautifulSoup
"""

import requests
from bs4 import BeautifulSoup
from config import NEWS_SOURCES, MAX_ARTICLES_PER_SOURCE
from database import save_article
import time

class NewsScrapler:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.articles_count = 0
    
    def scrape_all_sources(self):
        """Scrape news from all configured sources"""
        print("🕷️ Starting news scraping...")
        
        for source_name, source_config in NEWS_SOURCES.items():
            print(f"\n📰 Scraping {source_name.upper()}...")
            self.scrape_source(source_name, source_config)
            time.sleep(2)  # Be respectful to servers
        
        print(f"\n✅ Scraping completed! Total articles saved: {self.articles_count}")
    
    def scrape_source(self, source_name: str, source_config: dict):
        """Scrape a specific news source"""
        try:
            # Fetch the webpage
            response = requests.get(source_config['url'], headers=self.headers, timeout=10)
            response.raise_for_status()
            
            # Parse HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract articles based on source
            articles = []
            
            if source_name == 'bbc':
                # BBC specific extraction
                for article in soup.find_all('article'):
                    try:
                        title = article.find('h2')
                        link = article.find('a')
                        if title and link:
                            title_text = title.get_text(strip=True)
                            href = link.get('href', '')
                            if href and title_text:
                                articles.append({'title': title_text, 'link': href})
                    except:
                        continue
            
            elif source_name == 'techcrunch':
                # TechCrunch specific extraction
                for item in soup.find_all('a', class_='post-block__title__link'):
                    try:
                        title = item.get_text(strip=True)
                        link = item.get('href', '')
                        if title and link:
                            articles.append({'title': title, 'link': link})
                    except:
                        continue
            
            elif source_name == 'hackernews':
                # HackerNews specific extraction
                for tr in soup.find_all('tr', class_='athing'):
                    try:
                        title_cell = tr.find('span', class_='titleline')
                        if title_cell:
                            link = title_cell.find('a')
                            if link:
                                title = link.get_text(strip=True)
                                href = link.get('href', '')
                                if title and href:
                                    articles.append({'title': title, 'link': href})
                    except:
                        continue
            
            # Save articles to database
            for i, article in enumerate(articles):
                if i >= MAX_ARTICLES_PER_SOURCE:
                    break
                
                # Ensure link is complete
                link = article['link']
                if not link.startswith('http'):
                    if source_name == 'hackernews':
                        link = 'https://news.ycombinator.com/' + link
                    else:
                        link = source_config['url'] + link
                
                # Save to database
                if save_article(article['title'], link, source_name):
                    self.articles_count += 1
                    print(f"  ✓ Saved: {article['title'][:60]}...")
        
        except Exception as e:
            print(f"  ❌ Error scraping {source_name}: {str(e)}")

def run_scraper():
    """Run the scraper"""
    scraper = NewsScrapler()
    scraper.scrape_all_sources()

if __name__ == "__main__":
    run_scraper()
