import requests
from bs4 import BeautifulSoup

# Function to fetch and parse search results from Google
def fetch_and_parse_google_results(search_query, page_num):
    search_url = f"https://www.google.com/search?q={search_query}&start={page_num * 10}"
    response = requests.get(search_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        search_results = soup.find_all("a")
        return [link.get("href") for link in search_results if link.get("href")]
    else:
        print("Failed to retrieve search results for page", page_num)
        return []

# Number of pages to search
num_pages = 10
results_per_page = 10  # Google typically shows 10 results per page

# Search query
#search_query = input("Enter the domain to search")
#search_query = "site:" + search_query
search_query = "site:azurewebsites.net"

# Iterate through multiple pages of search results to collect the top 100 websites
top_websites = []
for page_num in range(num_pages):
    page_results = fetch_and_parse_google_results(search_query, page_num)
    domain = search_query.split(":")[1]
    top_websites.extend([url for url in page_results if ".{}".format(domain) in url])

    # Stop if we have collected 100 websites
    if len(top_websites) >= 100:
        break

# Print the top 100 websites
for idx, website in enumerate(top_websites[:100], start=1):
    print(f"{idx}. {website}")

# Ensure that we have collected at least 100 websites
if len(top_websites) < 100:
    print("Note: Less than 100 websites found with the '.{}' suffix.".format(search_query.split(":")[1]))
