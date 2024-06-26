from bs4 import BeautifulSoup
import requests

def get_recent_articles():
    url = "https://www.bleepingcomputer.com/news/security/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 403:
        print("Access forbidden: 403 error")
        return []

    if response.status_code != 200:
        print(f"Request failed with status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')

    articles = []

    # Find all articles in the news listing
    article_list = soup.find_all('div', class_='bc_latest_news_text')
    for article in article_list:
        title_tag = article.find('h4')
        summary_tag = article.find('p')
        author_tag = article.find('li', class_='bc_news_author')
        date_tag = article.find('li', class_='bc_news_date')

        if title_tag and summary_tag and author_tag and date_tag:
            title = title_tag.text.strip()
            link = title_tag.find('a')['href']
            summary = summary_tag.text.strip()
            author = author_tag.text.strip()
            date = date_tag.text.strip()
            articles.append({'title': title, 'link': link, 'summary': summary, 'author': author, 'date': date})
    
    return articles

def main():
    articles = get_recent_articles()
    
    if articles:
        for idx, article in enumerate(articles, start=1):
            print(f"Article {idx}:")
            print(f"Title: {article['title']}")
            print(f"Link: {article['link']}")
            print(f"Summary: {article['summary']}")
            print(f"Author: {article['author']}")
            print(f"Date: {article['date']}\n")
    else:
        print("No news articles found or failed to fetch news")

if __name__ == "__main__":
    main()
