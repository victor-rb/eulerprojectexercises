import requests
from bs4 import BeautifulSoup as bs

def scrap_problem (_url) :
    try:
        response = requests.get(_url)

        if response.status_code == 200 :
            soup = bs( response.content, 'html.parser')

            name_div = soup.find('h2').get_text()
            problem_div = format_text(soup.find('div', class_='problem_content').get_text())

            return name_div, problem_div
    
        else:
            print(f"Failed to scrape {_url}. Status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        
        print(f"Error scraping {_url}: {e}")

        return None
    
def format_text( text ): 

    if '$' in text :
        text = text.replace('$', '')
    if '\\times' in text:
        text = text.replace('\\times', 'X')
    if '\\dots' in text:
        text = text.replace('\\dots', '...')
    
    return text


