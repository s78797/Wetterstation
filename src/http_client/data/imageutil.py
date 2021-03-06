import datetime
import random
from io import BytesIO
from time import time

import requests
from PIL import Image

url = 'http://placeimg.com/1280/720/'
for i in range(140, 165, 1):
    response = requests.get(url + str(i))
    img = Image.open(BytesIO(response.content))
    filename = str(int((time() - 48*60*60)) + random.randrange(1, 200)) + '.jpeg'
    img = img.convert('RGB')
    img.save('mock/' + filename)
    print('saved ' + str(i) + '.' + 'image: ' + filename)
