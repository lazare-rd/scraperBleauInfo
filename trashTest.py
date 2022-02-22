from decimal import Rounded
import requests
import time

t1 = time.time()
response = requests.get("https://Bleau.info/95.2ouest/304549.html")
t2 = time.time()
print(response.elapsed)
print(round(t2-t1, 4))