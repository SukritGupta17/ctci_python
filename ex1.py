def isUnique(String):
    text = list(String)
    print(text)
    for word in text:
        if text.count(word) > 1:    
        	return False
        
        
    return True   
         
        

print(isUnique("Satnam") == False) 
print(isUnique("Sukrit") == True)
print(isUnique("00 23 Satn6m") == False)