import re
with open('./user_records.txt') as f:
    data = f.readlines()
    # print(data)
pattern = re.compile('([0-9]{2}), ([A-Z][A-Za-z ]+)')
true_ct = 0
false_ct = 0
for info in data:
    count = pattern.search(info)
    if count:
        ages = count.group(1)
        countries = count.group(2)
        true_ct += 1
        print(f'Age:{ages}')
        print(f'Country: {countries}')
    else:
        false_ct += 1
print(f'Valid Count: {true_ct}\nInvalid Count: {false_ct}')