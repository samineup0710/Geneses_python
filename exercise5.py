elements_list = ["car", "3324", "hero", 98, "bus", "plane", "boat"] 
print(elements_list)
print(len(elements_list))
"""pop operations"""
print(elements_list.pop())                   #this pops last elements from the list.
print(elements_list.pop(4))                  #this pops last elements at specific index in from list.
print(elements_list)                         #after pop operation list changes
"""insert operations"""
print(elements_list.insert(2,"apples"))      #insert at 2nd index
print(elements_list)
print(elements_list.insert(1,"apples"))      #insert at 1st index
print(elements_list)

"""remove operations"""
print(elements_list.remove("hero"))          #remove elements by element value
print(elements_list)
print(elements_list.remove("car"))          
print(elements_list)
print(elements_list.remove(98))     
print(elements_list)