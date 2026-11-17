# 37A - Towers 


# c_torres = int(input("cantida de torres"))
# longitudes = {}

# for i in range(c_torres):
#     longitud = int(input("longitud"))    
    
#     longitudes[longitud] = longitudes.get(longitud, 0) + 1
    
    
longitudes = {
    4 : 3,
    2 : 2
}
print(longitudes.values())
torre_mas_alta = max(longitudes.values())
print(torre_mas_alta)