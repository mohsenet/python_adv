from tqdm import tqdm
import time


# Simulate a time-consuming loop
for i in tqdm(range(100)):
    time.sleep(0.1)
