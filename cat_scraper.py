import sys
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


# funnycatpix.com
# catoftheday.com
# unsplash.com

# selenium, nginx, cdn
def main():

    # Where we put the stored data
    # DIR_PATH = sys.argv[1]
    
    src = "https://www.funnycatpix.com"
    url = src + '/page/'
    max_idx = 1519

    # prevent duplicates by tracking most recent post
    # most recent entry, 
    
    with open("urls.txt", "a") as f:
        for idx in tqdm(range(1, max_idx +1)):

            # Remake every url header and request the page
            new_url = url + str(idx)
            response = requests.get(new_url)
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

                    complete_url = src + image_url
                    f.write(complete_url + "\n")
                    # print(image_name, image_url, DIR_PATH + image_url.split("/")[-1])

            except AttributeError:
                print(url)
                print("Last Page Reached. Page " + str(idx - 1))

        

if __name__ == "__main__":
    main()


