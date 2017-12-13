import json as simplejson
import Sugoroku

def main():
    path = './'
    fileName = 'input_board'
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    dataFile = open(filePathNameWExt,"w")
    letNum = 0
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    currentLetter = letters[letNum]
    # Example
    data = {}
    data['key'] = 'value'
    data['title'] = 'Generated Sugoroku Board'
    data['author'] = 'Team Sugoroku - CMPM 146'
    data['date'] = '2017'
    data['publisher'] = 'Sugoroku Board Generator Program'
    data['dice'] = 'D6'
    data['start'] = 'idk yet'
    data['goal'] = 'idk yet'
    """
    format of JSON file:
    info
    transitions
        ID
            Backward: previous node
            Forward: next node
            Rule:
                    Success rolls (#s)
                success roll effect (+n)
                failure effect (-n)
            Dice roll
                target: resulting location (ID)
    """
    game_board = Sugoroku.Board()
    game_board = Sugoroku.main() #spaces is now a list
    spaces = game_board.to_list()
    #print(Sugoroku.send_board_list())
    for thing in spaces:
        thing.debug_print()
    print("finished printing")
    # and the list of spaces each space leads to depending on the dice roll
    data['transitions'] = {}
    # game_board.to_string() # happens in Sugoroku.py now
    # WE NEED: 1) immediate next space 2) transition
    #checkpointCount = 1 # because User not smart enough to start at 0 :/
    n = 1
    for i in range(len(spaces)): # -1

        id = spaces[i].get_id()
        if "begin" in id:
            id = letters[letNum+1]
        elif id != "start":
            id += currentLetter
        if "fall_start" in id:
            id = "fs" + letters[letNum]
            
        elif "fall" in id:
            id = "f" + letters[letNum] + str(n)
            n += 1
        elif "path_join" in id:
            id = "pj" + letters[letNum]
            
            
            
        

        #spaces[i].set_id(str(spaces[i].get_id()) + currentLetter)
        print(id)
        # set immediate next/previous nodes

        # set the rules, from traverse_params (format: [good rolls], good roll result, failure result)
       
        data['transitions'][id] = {}
        if "start" not in id:
        #if spaces[i].get_id() != "start":
            if "begin" not in spaces[i].get_backward().get_id():
                data['transitions'][id]["backward"] = spaces[i].get_backward().get_id() + letters[letNum]
            else:
                data['transitions'][id]["backward"] = letters[letNum]
            
            if spaces[i].get_backward().get_id() == "fall_start":
                data['transitions'][id]["backward"] =  "fs" + str(letters[letNum])
            
            if spaces[i].get_backward().get_id() == "fall" and "fall" in id:
                data['transitions'][id]["backward"] =  "f" + str(letters[letNum]) + str(n-2)
            
            elif spaces[i].get_backward().get_id() == "fall":
                data['transitions'][id]["backward"] =  "f" + str(letters[letNum]) + str(n-1)
                
            if spaces[i].get_backward().get_id() == "path_join":
                data['transitions'][id]["backward"] =  "pj" + str(letters[letNum])
            
            if "start" == spaces[i].get_backward().get_id():
                data['transitions'][id]["backward"] = "start"
        else:
            data['transitions'][id]["backward"] = None
        if "end" != id:
        
        
            if spaces[i].get_forward().get_id() != "begin":
                data['transitions'][id]["forward"] =  spaces[i].get_forward().get_id() + currentLetter
            
            else:
                data['transitions'][id]["forward"] =  letters[letNum + 1]
            
            if spaces[i].get_forward().get_id() == "fall_start":
                data['transitions'][id]["forward"] =  "fs" + str(letters[letNum])
            
            if spaces[i].get_forward().get_id() == "fall":
                data['transitions'][id]["forward"] =  "f" + str(letters[letNum]) + str(n)
                
            if spaces[i].get_forward().get_id() == "path_join":
                data['transitions'][id]["forward"] =  "pj" + str(letters[letNum])
            
            if i == len(spaces)-1:
                data['transitions'][id]["forward"] = "end"
        else:
            data['transitions'][id]["forward"] = None
        



        if isinstance(spaces[i].traverse_params, tuple):
            
            localTuple = spaces[i].traverse_params
            instructions = "If you roll a "
            for i in range(len(localTuple[0])):
                if i == len(localTuple[0])-1 and i != 0:
                    instructions += "or "

                instructions += str(localTuple[0][i])
                if i != len(localTuple[0]) -1 and len(localTuple[0]) > 2:
                    instructions += ", "
                if 2 == len(localTuple[0]) and i != len(localTuple[0]) -1:
                    instructions += " "
                
                    
            instructions += ", move forward " + str(localTuple[1]) + "."
            
            instructions += " Else, move back "
            
            instructions += str(abs(localTuple[2])) + "!"
            
            
            data['transitions'][id]["rule"] = instructions
        elif "fs" in id:
            data['transitions'][id]["rule"] = "If you haven't fallen, go to path join (pj)"
        elif "f" in id:
            data['transitions'][id]["rule"] = "Fall to fall start (fs)"
        elif "pj" in id:
            data['transitions'][id]["rule"] = "Path join"
        
        else:
            
            data['transitions'][id]["rule"] = 0
            
        
        #localTuple[0] #roll to go goodly
        #localTuple[1] #goodly
        #localTuple[2] #noodgoodly
       
       
       

        #if "begin" in id: #CHECKPOINT
        if id == letters[letNum+1]:
                    # make it a checkpoint
                    letNum += 1
                    currentLetter = letters[letNum]
                    # increment the name
                    #checkpointName = letters[letNum+1]
                    
                    data['transitions'][id] = {}
                    data['transitions'][id]["backward"] = spaces[i].get_backward().get_id() + letters[letNum-1]
                    data['transitions'][id]["forward"] = spaces[i].get_forward().get_id() + letters[letNum]
                    data['transitions'][id]["rule"] = "checkpoint"
                    if spaces[i].get_backward().get_id() == "fall_start":
                        data['transitions'][id]["backward"] =  "fs" + str(letters[letNum])
                        
                    elif spaces[i].get_backward().get_id() == "fall":
                        data['transitions'][id]["backward"] =  "f" + str(letters[letNum]) + str(n-1)
                        
                    if spaces[i].get_forward().get_id() == "fall_start":
                        data['transitions'][id]["forward"] =  "fs" + str(letters[letNum])
                    
                    elif spaces[i].get_forward().get_id() == "fall":
                        data['transitions'][id]["forward"] =  "f" + str(letters[letNum]) + str(n)
                    if spaces[i].get_backward().get_id() == "path_join":
                        data['transitions'][id]["backward"] =  "pj" + str(letters[letNum])
                    #checkpointCount += 1
                    
        if isinstance(spaces[i].traverse_params, tuple):
            if len(spaces[i].traverse_params) >= 0: # if it has a rule
                
                    for r in range(7): # for each possible dice roll
                        if r != 0: # if the roll isn't 0
                            data['transitions'][id][r] = {}
                            if r in spaces[i].traverse_params[0]: # ON SUCCESS
                                temp = spaces[i]
                                for move in range(spaces[i].traverse_params[1]):
                                    if temp.get_id() != "end":
                                        temp = temp.get_forward()
                                        data['transitions'][id][r]["target"] = temp
                                    data['transitions'][id][r]["target"] = temp.get_id()
                                    if "begin" == temp.get_id():
                                        data['transitions'][id][r]["target"] = currentLetter
                            else:
                                temp = spaces[i]                    # ON FAILURE
                                for move in range(abs(spaces[i].traverse_params[2])):
                                    if temp.get_id() != "start":
                                        temp = temp.get_backward()
                                        data['transitions'][id][r]["target"] = temp 
                                    data['transitions'][id][r]["target"] = temp.get_id()
                                    if "begin" == temp.get_id():
                                        data['transitions'][id][r]["target"] = currentLetter
    # add the last node outside of the loop bc it has no transitions
    data['transitions']["end"] = {}
    data['transitions']["end"]["backward"] = spaces[-1].get_id() + currentLetter
    data['transitions']["end"]["forward"] = None
    data['transitions']["end"]["rule"] = 0

    dataFile.write(simplejson.dumps(data, indent=4)) # , sort_keys = True
    dataFile.close()

if __name__ == "__main__":
    main()