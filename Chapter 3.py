# Now let's try learning, how to append something in a json file!
# We will be performing all the actions in 'sample.json' file this time.

import json 

# Appending is not much done in json files, so we have to load the data instead and then add the items using python.

with open("sample3.json", "r") as x : 
    data = json.load(x)
    wrdata = {"name":"Alvaro", "surname" :"Page", "age":29, "position":"CEO"}
    data.update({"name":"Alva", "surname" :"Pae", "age":9, "position":"O"})

with open("sample3.json", "w") as f :
        json.dump(data, f) 
        