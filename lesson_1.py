



name = ["aplle", "orange", "banan"]
price = [100, 70, 20]
availability = [True, False, False]

with open('text.txt') as f:
    text = f.read()

def merge_list_of_dict(**arrays):
    array_zip = zip(arrays["name"], arrays["price"])
    array_zip = dict(array_zip)
    return array_zip

array_dict = merge_list_of_dict(name=name, price=price)
i = 0

for a, v  in array_dict.items():
    array_dict[a] = list() 
    array_dict[a].append(v)
    array_dict[a].append(availability[i])    
    i += 1
    
print(text)  
print(array_dict)