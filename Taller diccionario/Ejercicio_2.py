Diccionario = {'Mikel' : 3, 'Ane' : 8, 'Amaia' : 12, 'Unai' : 5, 'Jon': 8, 'Ainhoa' : 7, 'Maite' : 5 }
Lista = []
for valores in Diccionario.items ():
    A = ((valores [1]))
    Lista.append (A)
B = (set (Lista))
print (list (B))