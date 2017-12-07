import json as simplejson
import Sugoroku

def main():
    path = './'
    fileName = 'input_board'
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    dataFile = open(filePathNameWExt,"w")

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
    print("hell")
    """
    format of JSON file:
    info
    transitions
        ID
            Backward: previous node
            Forward: next node
            Rule:
                    Success rolls (#s)
                sucess roll effect (+n)
                failure effect (-n)
            Dice roll
                target: resulting location (ID)
    """
    game_board = Sugoroku.Board()
    game_board = Sugoroku.main() #spaces is now a list
    spaces = game_board.to_list()
    #print(Sugoroku.send_board_list())
    #for thing in spaces:
    #    thing.prin()
    #print("finished printing")
    # and the list of spaces each space leads to depending on the dice roll
    data['transitions'] = {}
    game_board.to_string() 
    # WE NEED: 1) immediate next space 2) transition
    for i in range(len(spaces)-1):

        data['transitions'][spaces[i].get_id()] = {}
        # set immediate next/previous nodes
        if spaces[i].get_id() != "start":
            data['transitions'][spaces[i].get_id()]["backward"] = spaces[i].get_backward().get_id()
        else:
            data['transitions'][spaces[i].get_id()]["backward"] = None

        if spaces[i].get_id() != "end":
            data['transitions'][spaces[i].get_id()]["forward"] =  spaces[i].get_forward().get_id()
        else:
            data['transitions'][spaces[i].get_id()]["forward"] = None

        # set the rules, from traverse_params (format: [good rolls], good roll result, failure result)
        if i != 0:
            data['transitions'][spaces[i].get_id()]["rule"] = spaces[i].traverse_params
        

        if isinstance(spaces[i].traverse_params, tuple):
            if len(spaces[i].traverse_params) > 1: # if it has a rule
                for r in range(7): # for each possible dice roll
                    if r != 0: # if the roll isn't 0
                        data['transitions'][spaces[i].get_id()][r] = {}
                        if r in spaces[i].traverse_params[0]: # ON SUCESS
                            temp = spaces[i]
                            for move in range(spaces[i].traverse_params[1]):
                                if temp.get_id() != "end":
                                    temp = temp.get_forward()
                                    data['transitions'][spaces[i].get_id()][r]["target"] = temp
                                data['transitions'][spaces[i].get_id()][r]["target"] = temp.get_id()
                        else:
                            temp = spaces[i]                    # ON FAILURE
                            for move in range(abs(spaces[i].traverse_params[2])):
                                if temp.get_id() != "start":
                                    temp = temp.get_backward()
                                    data['transitions'][spaces[i].get_id()][r]["target"] = temp
                                data['transitions'][spaces[i].get_id()][r]["target"] = temp.get_id()
    # add the last node outside of the loop bc it has no transitions
    data['transitions'][spaces[len(spaces)-1].get_id()] = {}

    dataFile.write(simplejson.dumps(data, indent=4)) # , sort_keys = True
    dataFile.close()

if __name__ == "__main__":
    main()