#Task 1 - Working with Lists
fruit_list = ['pineapple', 'mango', 'kiwi', 'passionfruit', 'guava']
print("Original list: " + str(fruit_list))
fruit_list.append('papaya') #append new fruit to list
print("After adding a fruit: " + str(fruit_list))
fruit_list.remove('passionfruit') #remove one fruit from list
print("After removing a fruit: " + str(fruit_list))
print("Reversed list: " + str(fruit_list[::-1])) #print list in reverse order

#Task 2 - Exploring Dictionaries
my_dict = {"name": "Ariana", "age": 20, "city": "Hoboken"}
my_dict.update({"favorite color" : "green"}) #add new key-value pair to dictionary for "favorite color"
my_dict["city"] = "Philadelphia" #update city key with new value
keys = []
values = []
for key, value in my_dict.items():
    keys.append(key)
    values.append(str(value))

print("Keys: " + ", ".join(keys))
print("Values: " + ", ".join(values))

#Task 3 - Using Tuples
my_tuple = ('Everything Everywhere All at Once', 'Hope Your Dreams Come True', 'Their Eyes Were Watching God')
print("Favorite things: " + str(my_tuple))
try: #attempt to change one of the elements, tuples are immutable so attempt is made in try except block
    my_tuple[1] = 'Vex'
except:
    print("Oops! Tuples cannot be changed")

print("Length of tuple: " + str(len(my_tuple)))