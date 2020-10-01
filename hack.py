import os
import random

for i in range(20):
    with open('data.txt', 'a') as f:
        f.write(f'{i}')
        x = 365 + random.randint(0, i)
        date = f'{x} days ago'
        os.system('git add .')
        os.system(f'git commit --date="{date}" -m "E"')
os.system('git push')
