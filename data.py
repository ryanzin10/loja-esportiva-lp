category = {
    '1': {'name': 'Chuteira', 'sub': {'1': {'tipo': 'Campo'}, '2': {'tipo': 'Society'}, '3': {'tipo': 'Futsal'}}},
    '2': {'name': 'Luva', 'sub': {'1': {'tipo': 'Flat'}, '2': {'tipo': 'Rollfinger'}}},
    '3': {'name': 'Meia', 'sub': {'1': {'tipo': 'Cano alto'}, '2': {'tipo': 'Cano baixo'}}}
}

def consultar():
    with open('database.txt', 'r') as bd:
        for valor in bd:
            print(valor)
