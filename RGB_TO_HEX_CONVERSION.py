def rgb(r, g, b):
    
    options = {
        10 : 'A',
        11 : 'B',
        12 : 'C',
        13 : 'D',
        14 : 'E',
        15 : 'F'
    }
    
    resultado = []
    
    for i in (r, g, b):
        
        i = max(0, min(255, i))
        
        dividendo = i // 16
        residuo = i % 16
        
        if dividendo >= 10:
            dividendo = options[dividendo]
        else:
            dividendo = str(dividendo)
        
        if residuo >= 10:
            residuo = options[residuo]
        else:
            residuo = str(residuo)
        
        resultado.append(dividendo + residuo)
    
    return ''.join(resultado)