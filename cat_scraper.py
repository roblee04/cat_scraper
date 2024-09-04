import requests
from bs4 import BeautifulSoup

# funnycatpix.com
# catoftheday.com
# unsplash.com

def main():

    print("hello")
    url = 'https://funnycatpix.com'
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')

    image_tags = soup.find_all('img')

    for image_tag in image_tags:
        image_url = image_tag['src']
        image_name = image_url.split('/')[-1]
        image_data = requests.get(image_url).content
        with open(image_name, 'wb') as handler:
            handler.write(image_data)

    # reduce duplicate entries, hash url

if __name__ == "__main__":
    main()


