import requests
from bs4 import BeautifulSoup

def get_book_cover_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        soup = BeautifulSoup(response.content, "html.parser")
        img_tag = soup.find("img", class_="ResponsiveImage")

        if img_tag and 'src' in img_tag.attrs:
          return img_tag['src']
        else:
          print("Image element not found or has no 'src' attribute.")
          return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None