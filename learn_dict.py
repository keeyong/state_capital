# two different types of dictionary usage
# 
# Let's use first name and last name as an example
# 1st approach is to use "first name" and "last name" as separate keys. this approach is preferred
# 2nd approach is to use first name value as key and last name as value

# ---- 1st apprach
name_1 = { 'firstname': 'keeyong', 'lastname': 'han' }
name_2 = { 'firstname': 'dennis', 'lastname': 'yang' }

names = []
names.append(name_1)
names.append(name_2)

for name in names:
    print("1st approach - first name:" + name["firstname"] + ", last name:" + name["lastname"])

# ---- 2nd approach
# 여기서는 키는 이름이 되고 값은 성이 되는 구조이다
name_1 = { 'keeyong': 'han' }
name_2 = { 'dennis': 'yang' }

names = []
names.append(name_1)
names.append(name_2)

for name in names:
    for key, value in name.items():
        print("2nd approach - first name:" + key + ", last name:" + value)
