import re

import requests
from bs4 import BeautifulSoup
from googlesearch import search


# 구글검색
def get_search_results(query, num_results=100):
    urls = []
    for url in search(query, num_results=num_results):
        urls.append(url)
    return urls

# url에서 긁어오기
def scrape_text_from_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text from the HTML
        paragraphs = soup.find_all('p')
        text = ' '.join([p.get_text() for p in paragraphs])

        # Basic cleanup
        text = re.sub(r'\s+', ' ', text)
        return text
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve {url}: {e}")
        return None

# Function to retrieve and scrape text from Google search results
def retrieve_and_scrape(query, num_results=100):
    urls = get_search_results(query, num_results)
    documents = []
    
    for url in urls:
        text = scrape_text_from_url(url)
        if text:
            documents.append(text)
    
    return documents

# Example usage
postgresql_query = "Postgresql performance tuning hints"
mysql_query = "MySQL performance tuning hints"

postgresql_docs = retrieve_and_scrape(postgresql_query)
mysql_docs = retrieve_and_scrape(mysql_query)

# Save the documents to a file (optional)
with open("postgresql_docs.txt", "w") as f:
    for doc in postgresql_docs:
        f.write(doc + "\n\n")

with open("mysql_docs.txt", "w") as f:
    for doc in mysql_docs:
        f.write(doc + "\n\n")

print("Documents retrieved and saved.")
