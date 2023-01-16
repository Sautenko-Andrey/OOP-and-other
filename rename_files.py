import os

ext = "jpg"
i = 1
dir = '/home/andrey/grocery_data/All_products_holders/oil/Shedriy_Dar(0.85l)'
for file in os.listdir(dir):
    if file.endswith(ext):
        os.rename(f'{dir}/{file}', f'{dir}/oil_shedriy_dar(0.85 l)_{i}.{ext}')
        i+=1
