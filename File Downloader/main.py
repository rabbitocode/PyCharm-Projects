import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse, urljoin, unquote

# Directory where you want to save the files
directory = r'D:\Downloaded Course'
if not os.path.exists(directory):
    os.makedirs(directory)


# Function to download files
def download_file(url):
    print(f"Downloading file from URL: {url}")
    response = requests.get(url, stream=True)
    response.raise_for_status()

    filename = unquote(os.path.basename(urlparse(url).path))
    file_path = os.path.join(directory, filename)

    with open(file_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)

    print(f"Downloaded file saved to {file_path}")


# URL of the webpage containing links
webpage_url = 'https://romhub.io/COURSE/server1/UDEMY%20COURSES/Complete%20Blender%20Creator:%20Learn%203D%20Modelling%20for%20Beginners/01%20-%20Introduction%20&%20Setup%20-%20New%20Blender%203.2%20Content'

# Get the HTML content of the webpage
print(f"Fetching webpage content from: {webpage_url}")
response = requests.get(webpage_url)
response.raise_for_status()

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all links with the class 'list-item'
links_found = False
for link in soup.find_all('a', class_='list-item'):
    href = link.get('href')
    if href:
        # Construct the full URL
        file_url = urljoin(webpage_url, href)
        print(f"Found URL: {file_url}")
        # Check if it's a file URL (you can add more checks if needed)
        if any(file_url.lower().endswith(ext) for ext in ['.mp4', '.srt', '.blend', '.url']):
            download_file(file_url)
            links_found = True

if not links_found:
    print("No downloadable files found.")
