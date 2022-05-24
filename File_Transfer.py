import os
import time
import shutil
SRC_PATH = "."
TARGET_PATH = "../"
for filename in os.listdir(SRC_PATH):
    if os.path.getmtime(filename) >= (time.time() - 24*60*60): 
        shutil.move(os.path.join(SRC_PATH, filename), TARGET_PATH)  
