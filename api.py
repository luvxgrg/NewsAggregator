"""
Flask API for NewsAggregator
"""

from flask import Flask, jsonify, request
from database import init_database, get_all_articles, search_articles, get_articles_by_source

app = Flask(__name__)

# Initialize database on startup
init_database()

@app.route('/api/articles', methods=['GET'])
def get_articles():
    """Get all articles"""
    articles = get_all_articles()
    return jsonify({
        'success': True,
        'count': len(articles),
        'articles': articles
    })

@app.route('/api/articles/search', methods=['GET'])
def search():
    """Search articles by query"""
    query = request.args.get('q', '')
    
    if not query:
        return jsonify({
            'success': False,
            'message': 'Search query required'
        }), 400
    
    articles = search_articles(query)
    return jsonify({
        'success': True,
        'query': query,
        'count': len(articles),
        'articles': articles
    })

@app.route('/api/articles/source/<source>', methods=['GET'])
def get_by_source(source):
    """Get articles from specific source"""
    articles = get_articles_by_source(source)
    return jsonify({
        'success': True,
        'source': source,
        'count': len(articles),
        'articles': articles
    })

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get statistics about articles"""
    articles = get_all_articles()
    
    sources = {}
    for article in articles:
        source = article['source']
        sources[source] = sources.get(source, 0) + 1
    
    return jsonify({
        'success': True,
        'total_articles': len(articles),
        'sources': sources
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'service': 'NewsAggregator API'})

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'message': 'Endpoint not found',
        'available_endpoints': [
            '/api/articles',
            '/api/articles/search?q=query',
            '/api/articles/source/<source>',
            '/api/stats',
            '/health'
        ]
    }), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
