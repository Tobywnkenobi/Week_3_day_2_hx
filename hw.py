import re

with open ('./user_records.txt') as f:
    data = f.readlines()

pattern = re.compile('\d{2}), ([A-Z][A-Za=z ]+)')

true_count = 0
false_count = 0

for d in data:
    found_num = pattern.search(d)
    if found_num:
        age = found_num.group(1)
        countries = found_num.group(2)
        print(f'Age: {age} \nCountry: {countries}\n')
        true_count += 1
    else:
        false_count += 1
        
print(f'Valid Count: {true_count}\nInvalid Count: {false_count}')