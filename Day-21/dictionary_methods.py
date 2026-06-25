# Dictionary Methods.
# 1. key() = returns all the key.
# 2. values() = returns all values.
# 3. items() = returns key - value pairs as tuple.
# 4. getkey() = safer way to access the value of particular key.
# 5. update(new_item) = add new item to the dictionary.

dict = {
    "name" : "shradha",
    "subject" : ["physics","maths","chemistry"],
    "cgpa" : 8.9
}

print(dict.keys()) # name, subject, cgpa
print("\n")

print(dict.values()) #
print("\n")
print(dict.items())
print("\n")
print(dict.get("cgpa"))

print("\n")
new = {"city": "delhi"}
print(dict.update(new))
print(dict)