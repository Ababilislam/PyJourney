thisdict = {
    "brand": "Ford",
    "model": "mustang",
    "year": 1964
}

thisdict.update({"year":2020})
thisdict["color"]="white"
print(thisdict)

for x in thisdict:
    print(x)

print(key for key in thisdict)
