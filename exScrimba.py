#Exercise: Scrimba
freelancers = {'name':'freelancing Shop',
               'brian': 70,
               'black knight':20,
               'biccus diccus':100,
               'grim reaper':500,
               'minstrel':-15}
antiques = {'name':'Antique Shop',
            'french castle':400,
            'wooden grail':3,
            'scythe':150,
            'catapult':75,
            'german joke':5}
pet_shop = {'name':'Pet Shop',
            'blue parrot':10,
            'white rabbit':5,
            'newt': 2}

stock = {**freelancers, **antiques, **pet_shop}
stock.pop('name')
print('Estoque das lojas no começo do dia: ', sorted(stock.items()))


cart = {}
purse = 1000
total = 0
buy_items = ''

for shop in (freelancers, antiques,pet_shop):
    buy = input(f'Bem vindo a {shop["name"]} qual dos itens você deseja comprar? {shop}')
    if buy in shop:
        buy_items = buy_items + f' {buy}:{shop[buy]}GP'
        cart.update({buy:shop.pop(buy)})
        total= sum(cart.values())

purse -= total
print(f'Você comprou os seguintes itens:{buy_items}. Sua compra ficou em {total} moedas de ouro.')
print(f'Seu saldo agora é de {purse} moedas de ouro.')

stock_after = {**freelancers, **antiques, **pet_shop}
stock_after.pop('name')
print('Estoque das lojas no fim do dia:', sorted(stock_after.items()))

