from requests import Session
from time import sleep
from datetime import datetime

collection_name = input('Collection name: ')
template_id = input('Template ID: ')

s = Session()
url = (f'https://wax.api.atomicassets.io/atomicmarket/v1/sales?state=3&collection_name={collection_name}&template_id={template_id}&page=1&limit=10&order=desc&sort=created')

while True:
    now = datetime.now() 
    current_time = now.strftime("%H:%M:%S")
    response = s.get(url).json()
    sale_id1 = response['data'][0]['sale_id']
    
    for asset in response['data']:
        if asset['listing_symbol'] == 'WAX':
            price = int(asset["listing_price"]) * 0.00000001
            print('https://wax.atomichub.io/market/sale/' + asset['sale_id'] + '\n' + str(price), 'WAX' + '\n')
        else:
            price = int(asset["listing_price"]) * 0.01
            print('https://wax.atomichub.io/market/sale/' + asset['sale_id'] + '\n' + str(price), 'USD' + '\n')

    print('=================', current_time, '================='+'\n' + 'ждем обновление данных')
    while True:
        response2 = s.get(url).json()
        sale_id2 = response2['data'][0]['sale_id']
        if sale_id1 == sale_id2:
            sleep(10)
        else:
            break
