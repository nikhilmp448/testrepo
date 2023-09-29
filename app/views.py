from django.shortcuts import render
import imdb
import requests
from bs4 import BeautifulSoup


def get_images():


# URL of the website with HD wallpapers
    url = "https://www.hdwallpapers.in/cars-desktop-wallpapers.html"

    # Define a user-agent to mimic a web browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    # Send a GET request to the website with the custom headers
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all image tags with the "src" attribute
        img_tags = soup.find_all("img", src=True)

        # Extract the URLs from the "src" attribute of the image tags
        image_urls = [img["src"] for img in img_tags]

        # Filter the image URLs to include only those ending with ".jpg" (you can adjust this filter as needed)
        hd_image_urls = [img_url for img_url in image_urls if img_url.endswith(".jpg")]

        # Print the list of HD image URLs
    #     for idx, img_url in enumerate(hd_image_urls, start=1):
    #         print(f"HD Wallpaper {idx}: {img_url}")
        return hd_image_urls
    else:
        return response.status_code



def home(request):
    images = get_images()
    context = {'images':images}
    return render(request,'ads.html',context)