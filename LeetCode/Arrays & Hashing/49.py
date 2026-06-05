test = ["eat", "tea", "tan", "ate", "nat", "bat"]

grupos = {}

for palabra in test:
    clave = "".join(sorted(palabra))
    
    if clave not in grupos:
        grupos[clave] = []
        
    grupos[clave].append(palabra)
    
print(list(grupos.values()))