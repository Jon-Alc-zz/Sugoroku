import json as simplejson

path = './'
fileName = 'input_board'
filePathNameWExt = './' + path + '/' + fileName + '.json'
dataFile = open(filePathNameWExt,"w")

# Example
data = {}
data['key'] = 'value'
data['title'] = 'idk yet'
data['author'] = 'idk yet'
data['date'] = 'idk yet'
data['publisher'] = 'idk yet'
data['dice'] = 'idk yet'
data['start'] = 'idk yet'
data['goal'] = 'idk yet'

spaces = ["A","B","C","D"]

data['transitions'] = {}


for i in range(len(spaces)-1):
    
    data['transitions'][spaces[i]] = {}
    
    if i != 0:
        data['transitions'][spaces[i]][str(i)] = {}
        data['transitions'][spaces[i]]["rule"] = "rule placeholder" 
        data['transitions'][spaces[i]][str(i)]["target"] = "target placeholder"
    for r in range(6):
        if r+i+1 < len(spaces):
            # spaces[i] = the space's name (A, B, C, etc)
            # str(r+1) = the dice roll
            # spaces[r+i+1] = the space the roll moves you to
            data['transitions'][spaces[i]][str(r+1)] = {}
            data['transitions'][spaces[i]][str(r+1)]["target"] = spaces[r+i+1]
            #print(spaces[i],i,spaces[i+1])
        else:
            data['transitions'][spaces[i]][str(r+1)] = {}
            data['transitions'][spaces[i]][str(r+1)]["target"] = spaces[-1]

data['transitions'][spaces[len(spaces)-1]] = {}

# We don't know how to do row, col yet           
#data['transitions']["A"]["Row"] = "1"
#data['transitions']["A"]["Column"] = "1"
#data['transitions']["B"]["Row"] = "1"
#data['transitions']["B"]["Column"] = "2"
#data['transitions']["C"]["Row"] = "2"
#data['transitions']["C"]["Column"] = "2"

dataFile.write(simplejson.dumps(data, indent=4, sort_keys = True)) # , sort_keys = True
dataFile.close()

