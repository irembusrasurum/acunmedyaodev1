# import specialMath as math
from matematik import topla as toplamaIslemi
from ders3 import sayHello,Human
from human import Human
import random
from selenium import webdriver

print(toplamaIslemi(10, 20))
print(random.randint(0, 100))

human1 = Human("Irem")
human1.talk("Merhaba")

chromeDriver = webdriver.Chrome()