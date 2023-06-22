import os
from bs4 import BeautifulSoup
import requests

# Googleimage = "https://www.google.com/search?" normal search
Googleimage = "https://www.google.com/search?tbm=isch&"  # image search

headers_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

save_folder = "images"

def main():
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    download_images()

def download_images():
    data = input("What are you looking for? ")
    no_of_images = int(input("How many images do you want? "))
    print("Searching...")

    search_url = Googleimage + "q=" + data
    print(search_url)
    response = requests.get(search_url, headers=headers_agent)
    soup = BeautifulSoup(response.content, 'html.parser')
    images = soup.find_all('img')

    count = 0
    for img in images:
        link = img.get("data-src")
        if link:
            try:
                image_response = requests.get(link)
                image_content = image_response.content
                file_name = os.path.join(save_folder, f"image_{count}.jpg")
                with open(file_name, 'wb') as f:
                    f.write(image_content)
                print(f"Downloaded image_{count}.jpg")
                count += 1
                if count == no_of_images:
                    break
            except requests.exceptions.RequestException as e:
                print(f"Error downloading image: {e}")
    
    print(f"Total images downloaded: {count}")


if __name__ == '__main__':
    main()
