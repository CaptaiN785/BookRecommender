import requests
from PIL import Image

HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

def getImage(img_url):
    data = requests.get(img_url, headers=HEADERS)
    with open("temp/img.jpg", 'wb') as file:
            file.write(data.content)
    image = Image.open("temp/img.jpg")
    if image.height < 400 and image.width < 150:
        return Image.open("missing.jpg")
    image = image.resize((300, 500))
    return image

if __name__ == '__main__':
    getImage("http://images.amazon.com/images/P/0061087017.01.LZZZZZZZ.jpg")