dictionary = {
    'value': 11
}

dictionary1 = dictionary

print('Before value is updated :')
print(f" dictionary = {dictionary}")
print(f" dictionary_1 = {dictionary1}")

print(f" \ndictionary is points to : {id(dictionary)}")
print(f" \ndictionary_1 is points to {id(dictionary1)}")

dictionary1['value'] = 22

print(f"\n After value is updated: ")
print(f"dictionary = {dictionary}")
print(f" dictionary = {dictionary1}")

print(f" \ndictionary is points to : {id(dictionary)}")
print(f" \ndictionary_1 is points to {id(dictionary1)}")
