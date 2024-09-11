import sys
import requests
from bs4 import BeautifulSoup

# funnycatpix.com
# catoftheday.com
# unsplash.com

# selenium, nginx, cdn
def main():

    # Where we put the stored data
    DIR_PATH = sys.argv[1]
    
    src = "https://www.funnycatpix.com"
    url = src + '/page/'
    max_idx = 1519

    # prevent duplicates by tracking most recent post
    # most recent entry, 
    

    for idx in range(max_idx, max_idx + 2):

        # Remake every url header and request the page
        url = url + str(idx)
        response = requests.get(url)
        html_content = response.content

        # make soup object
        soup = BeautifulSoup(html_content, 'html.parser')

        # try to scrape for images, if we cannot, return
        try:
            posts = soup.find("section",id="posts")
            image_tags = posts.find_all('img')
            for image_tag in image_tags:
                image_url = image_tag['src']
                image_name = image_tag['alt']
                
                print(image_name, image_url, DIR_PATH + image_url.split("/")[-1])

        except AttributeError:
            print("Last Page Reached. Page " + str(idx - 1))
        

if __name__ == "__main__":
    main()


