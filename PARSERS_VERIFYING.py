import json

with open('prices_store3.json') as f:
    store=json.load(f)

print(store)
obolon_premium_atb=store['obolon_premium_1.1_l']['atb']
print(f'Цена в атб на Оболонь : {obolon_premium_atb}')