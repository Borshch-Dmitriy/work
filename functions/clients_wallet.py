clients={}

def bank(operation, id, amount):
    clients[id] = clients.get(id, 0)
    if operation == 'top up':
        clients[id] = clients.get(id,0) + amount
    if operation == 'withdraw':
        clients[id] = clients.get(id,0) - amount
    if operation == 'show balance':
        print(clients[id])
    if operation == 'pay':
        clients[id] = clients.get(id, 0) - amount

arthur = 'id-1004'
tony = 'id-78923'
bank('top up', tony, 500)
bank('show balance', arthur, None)
bank('pay', tony, 120)
bank('top up', arthur, 1000)
bank('show balance', arthur, None)
bank('withdraw', tony, 200)
bank('show balance', tony, None)