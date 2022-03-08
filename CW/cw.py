from time import time, sleep
import os
i = 0
a_directory = "images/images/"
for filename in os.listdir(a_directory):
    filepath = os.path.join(a_directory, filename)
    print(filepath)
    sleep(10)
