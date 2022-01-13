import requests
import urllib.request
from PIL import Image

print('What is your name?: ', end='\t')
name = input()
r1 = requests.get('https://api.agify.io?name='+name)
age = r1.json()['age']
count = r1.json()['count']
r2 = requests.get('https://api.genderize.io?name='+name)
gender = r2.json()['gender']
gender_probability = r2.json()['probability']
print(gender_probability)

print('I predict you age is', age, 'and your gender is', gender)
print('Count =', count)

dog_pic = requests.get('https://random.dog/woof.json').json()['url']
urllib.request.urlretrieve(dog_pic, 'dog')
print('Here is a picture of a dog.')
img = Image.open("dog")
img.show()

