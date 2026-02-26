"""
Main entry point for NewsAggregator
"""

import argparse
from scraper import run_scraper
from api import app
from database import init_database

def main():
    parser = argparse.ArgumentParser(description='NewsAggregator: Scrape and aggregate news')
    parser.add_argument('--scrape', action='store_true', help='Run the scraper')
    parser.add_argument('--api', action='store_true', help='Start the API server')
    parser.add_argument('--all', action='store_true', help='Run scraper then start API')
    
    args = parser.parse_args()
    
    # Initialize database
    init_database()
    
    if args.scrape:
        print("Running scraper...")
        run_scraper()
    
    elif args.api:
        print("Starting API server on http://localhost:5000")
        app.run(debug=True, port=5000)
    
    elif args.all:
        print("Running scraper...")
        run_scraper()
        print("\nStarting API server...")
        app.run(debug=True, port=5000)
    
    else:
        print("Usage: python main.py --scrape | --api | --all")
        print("  --scrape : Run the news scraper")
        print("  --api    : Start the Flask API server")
        print("  --all    : Run scraper then start API")

if __name__ == '__main__':
    main()
