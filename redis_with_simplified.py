import redis

r = redis.Redis(host='localhost', port=6379)

r.set('France', 'Paris')
r.set('Germany', 'Berlin')
r.set('Italy', 'Rome')
r.set('Spain', 'Madrid')
r.set('United Kingdom', 'London')
r.set('United States', 'Washington, D.C.')
r.set('Canada', 'Ottawa')
r.set('Japan', 'Tokyo')
r.set('China', 'Beijing')


france_capital = r.get('France')
print(france_capital)
print(type(france_capital))
