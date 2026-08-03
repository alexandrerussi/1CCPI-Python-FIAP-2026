endpoints = ["/login", "/produtos", "/pedidos"]

status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
]

print(endpoints[0])
print(status[0])

def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299

print(eh_sucesso(500))