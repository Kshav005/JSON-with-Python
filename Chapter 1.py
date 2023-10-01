# JSON is an inbuilt module. It's full form is JavaScript Object Notation, used to store different values in form of key value pair, just like in Python dictionaries.
# You can just go on importing it by using 'import json'

import json

# There are two functions in json - 'load' and 'loads'
# Before telling about them, let's talk a little about json more. First rule is that, you should always use double quotes (") in JSON file and second rule is that it doesn't have the comment feature like python and HTML.
# It's pretty popular and is often called as better than XML.
# The json file has '.json' as extension.
# Parsing is a term used to save a particular code into JSON. This is where 'loads' is used.
data = '{"a" : 12, "b" : true, "c" : "Hello"}'        # The json data should be in form of a string and it has key value pairs in form of curly brackets!
parsed = json.loads(data)       # Uploading the data into json format. 
print(parsed)

# And now you can access the data values by using the example below. Suppose we want to get the value of 'c'.
print(parsed["c"])

# Now let's check out about 'load'
# First check out that there is a file called 'sample.json' and inside you can see that a json file is created. 
# Do learn that the json is written like that, just like in the sample json file. Now let's continue.
# So, 'load' is used to read a json file and use it in python. 
with open("sample.json", "r") as f : 
    b = json.load(f)
    print(b)
    print(b["age"])
    
# Basically, the difference between 'load' and 'loads' is that the 'loads' is used to parse (change) a string into JSON language while the 'load' is used to use a json extension file for reading.
