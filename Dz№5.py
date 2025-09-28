text = input("Введите строку: ")    
if len(text) > 10:   
    result = text[:10] + "..."  
else:    
    result = text   
print("Результат:", result)
