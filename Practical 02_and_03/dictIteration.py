person={"name":"Jessa","country":"USA","telephone":"1178"}

print('key',':','value')
for key in person:
    print(key,':',person[key])

print('key',':','value')
for key_value in person.items():
    print(key_value[0],key_value[1])

