# In this chapter, we are talking about how we can store data in a json file by using 'dump' and more functions!
import json 

# Suppose we have a data 
data = {"company": "Ford", "models" : ["mustang", "GT", "Focus", "Fiesta"], "highestprice" : "$5 million"}

# Let's change the string into JSON type language by using 'dumps'
change = json.dumps(data)       # In this, we needn't use a string to change into JSON compatible object. Instead, it would directly change it into json.
print(change)       

# Now let's try saving the data into a new file!
with open("sample2.json", "w") as f : 
    json.dump(data, f, indent=2)        # and hence, now you can see the new file 'sample2.json' which will be containing the data!

# The 'indent' parameter is just to specify how much space should be left while filling the data making the data file more prettier and understandable.
# The 'f' is actually filled in 'fp' parameter, it is used to specify the file object that was 'with open(...) as f', here the f is treated as 'fp'