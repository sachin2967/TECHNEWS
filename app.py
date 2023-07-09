from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
load_dotenv()
import os
unsplash_api_key = os.getenv('unsplash_api_key')




app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    url = 'https://www.ndtv.com/'
    response = requests.get(url)
    header_tags=["LATEST","INDIA","CITIES","WORLD-NEWS","EDUCATION","SCIENCE","PEOPLE"]
    num=0
    if request.method == 'POST': 
     num = int(request.form["section_number"])
    
    selected_section = header_tags[num]
    #url
    section_url = url+header_tags[num]
        
    # Send a GET request to the section URL
    response = requests.get(section_url)

    # Create a BeautifulSoup object to parse the HTML content of the section
    section_soup = BeautifulSoup(response.content, 'html.parser')
    
    
    # Find the div tag that represents the different news articles
    articles = section_soup.find_all('div', class_='news_Itm', limit=8)
    finalNews = ""
    for article in articles:
        news_itm_cont_div = article.find('div', class_='news_Itm-cont')
        if news_itm_cont_div is not None:
            dec = news_itm_cont_div.find('p')
            if dec is not None:
                finalNews += dec.text + "\n"
    # Fetch the image URL from the Unsplash API
    unsplash_url = f'https://api.unsplash.com/photos/random?client_id={unsplash_api_key}'
    unsplash_response = requests.get(unsplash_url)
    if unsplash_response.status_code == 200:
        random_image = unsplash_response.json()
        image_url = random_image['urls']['regular']
    else:
        image_url = 'https://img.freepik.com/free-vector/instagram-background-gradient-colors_23-2147821882.jpg?w=740&t=st=1688179543~exp=1688180143~hmac=e070dcbbe1a862354d21b00c5bb742929ba55f887008e255aeefa9db8328b5bd'
    
    return render_template('index.html', News=finalNews, header=selected_section, image_url=image_url)



    if __name__ == '__main__':
     app.run()

      











