"""
Database management for storing articles
"""

import sqlite3
from datetime import datetime
from typing import List, Dict
import os

DATABASE_PATH = 'articles.db'

def init_database():
    """Initialize SQLite database with articles table"""
    if not os.path.exists(DATABASE_PATH):
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                link TEXT UNIQUE NOT NULL,
                source TEXT NOT NULL,
                published_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                content TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
        print("✅ Database initialized successfully")

def save_article(title: str, link: str, source: str, content: str = None):
    """Save an article to the database"""
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO articles (title, link, source, content)
            VALUES (?, ?, ?, ?)
        ''', (title, link, source, content))
        
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False

def get_all_articles() -> List[Dict]:
    """Get all articles from database"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT id, title, link, source, published_date
        FROM articles
        ORDER BY published_date DESC
    ''')
    
    articles = []
    for row in cursor.fetchall():
        articles.append({
            'id': row[0],
            'title': row[1],
            'link': row[2],
            'source': row[3],
            'published_date': row[4]
        })
    
    conn.close()
    return articles

def search_articles(query: str) -> List[Dict]:
    """Search articles by title"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    search_query = f"%{query}%"
    cursor.execute('''
        SELECT id, title, link, source, published_date
        FROM articles
        WHERE title LIKE ?
        ORDER BY published_date DESC
    ''', (search_query,))
    
    articles = []
    for row in cursor.fetchall():
        articles.append({
            'id': row[0],
            'title': row[1],
            'link': row[2],
            'source': row[3],
            'published_date': row[4]
        })
    
    conn.close()
    return articles

def get_articles_by_source(source: str) -> List[Dict]:
    """Get articles from specific source"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT id, title, link, source, published_date
        FROM articles
        WHERE source = ?
        ORDER BY published_date DESC
    ''', (source,))
    
    articles = []
    for row in cursor.fetchall():
        articles.append({
            'id': row[0],
            'title': row[1],
            'link': row[2],
            'source': row[3],
            'published_date': row[4]
        })
    
    conn.close()
    return articles

def delete_old_articles(days: int = 7):
    """Delete articles older than specified days"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        DELETE FROM articles
        WHERE published_date < datetime('now', '-' || ? || ' days')
    ''', (days,))
    
    deleted = cursor.rowcount
    conn.commit()
    conn.close()
    
    return deleted
