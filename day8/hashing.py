mp = {}
mp = dict()
mp = {101: "Alice", 102: "Bob", 103: "Charlie"}
mp[101] = "Welsi"
print(mp.get(101))
print(mp.get(104, "Not Found"))
for keys in mp:
    print(keys, ":", mp[keys])
print(mp.pop(102))