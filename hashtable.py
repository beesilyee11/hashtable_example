hashtable = list(None for n in range(7))
#hashtable = [None * 7]

def get_key(input):
    return hash(input)
#키 생성하기

def hash_func(key):
    return key % 5
#해시 함수 - division법 이용

def save_data(data, value):
    hash_table_key = hash_func(get_key(data))
    if hashtable[hash_table_key] != None:
        print("hash 충돌발생")
    hashtable[hash_table_key] = value

def read_data(data):
    hash_table_key = hash_func(get_key(data))
    return [hash_table_key, data]

save_data("user", "12345678")
save_data("anonymous", "blank")

print(read_data("user"))
print(read_data("anonymous"))

print(f"""
-----------------------------
{hashtable}
""")

# print(get_key("user"))
# print(hash_func(get_key("user")))
