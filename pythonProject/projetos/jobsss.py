frutas = ['maça', 'banana', 'melancia', 'mamão', 'kiwi', 'coco', 'pêssego', 'figo']
nova_lista = []

for x in frutas:
    if 'a' not in x:
        nova_lista.append(x)
nova_lista = [x for x in frutas if "a" not in x]
print(nova_lista)