"""
Sugoroku Project

Jonathan Alcantara
Yuvika Dube
Ryan Jaime
Jolina Lam
Ruihong Yu

Currently a very basic implementation demonstrating the main idea of Sugoroku.
"""
import random
import copy

# Space is a place on the board that a Player can land on.
class Space:
    
    # initialization
    def __init__(self, given_traverse_params=0, given_id="", given_board_id="normal"):
        self.backward = None
        self.forward = None
        self.traverse_params = given_traverse_params
        self.id = given_id
        self.board_id = given_board_id

    # links this Space ahead of a given one
    def set_backward(self, given_space):
        self.backward = given_space

    # links this Space before a given one
    def set_forward(self, given_space):
        self.forward = given_space

    # returns the previous Space
    def get_backward(self):
        return self.backward

    # returns the Space ahead
    def get_forward(self):
        return self.forward

    # traverse returns values provided
    def traverse(self):
        if isinstance(self.traverse_params, tuple): # tuples here will always have 3 values
            roll = random.randrange(1, 7)
            print("Player event roll: ", roll)
            print("Player needs: ", self.traverse_params[0])
            if roll in self.traverse_params[0]: # check if roll is in successful numbers ([0])
                return self.traverse_params[1] # if roll succeeds, return success jump value ([1])
            else:
                return self.traverse_params[2] # if roll fails, return failure jump value ([2])
        else: # traverse_params is an int, making it a guaranteed jump (!= 0), or empty Space (== 0)
            return self.traverse_params

    # used to check for "start" and "end"
    def get_id(self):
        return self.id

    # changes current node's id
    def set_id(self, new_id):
        self.id = new_id

    #returns the board it's currently a part of
    def get_board_id(self):
        return self.board_id

    def set_board_id(self, new_board_id):
        self.board_id = new_board_id
    
    # print the node
    def debug_print(self):
        print("----id----")
        print("id [",self.id,"]")
        if self.id != "start":
            print("from", self.backward.get_id())
        if self.id != "end":
            print("to", self.forward.get_id())
        if isinstance(self.traverse_params, tuple):
            print("traverse", self.traverse_params)

class Board:

    # initialization
    def __init__(self, board_id="normal"):
        self.length = 3
        self.head = Space(0, "start")
        middle_space = Space(0,"middle")
        self.tail = Space(0, "end")
        self.head.set_forward(middle_space)
        middle_space.set_backward(self.head)
        middle_space.set_forward(self.tail)
        self.tail.set_backward(middle_space)
        self.id = board_id

    # returns the length
    def get_length(self):
        return self.length

    # returns the head(start)
    def get_head(self):
        return self.head

    def set_head(self, given_space):
        self.head=given_space

    # returns the tail(end)
    def get_tail(self):
        return self.tail

    def set_tail(self, given_space):
        self.tail=given_space

    # updates the length because it might be changed during reproduction
    def update_length(self):
        temp_length = 1
        traveller = self.head
        while traveller.get_id() is not "end":
            traveller = traveller.get_forward()
            temp_length+=1
        self.length = temp_length

    # inserts a given node in a location where 1 < location < length - 1
    def insert(self, given_space, insert_location=1):
        traveller=self.head
        for i in range(0, insert_location):
            traveller=traveller.get_forward()
        given_space.set_backward(traveller.get_backward())
        given_space.set_forward(traveller)
        traveller.get_backward().set_forward(given_space)
        traveller.set_backward(given_space)
        given_space.set_board_id(self.id)
        self.length+=1
        
    #pops a node at location, 1<location<length-1
    def pop(self, pop_location):
        traveller=self.get_head()
        for i in range(0, pop_location):
            if traveller.get_forward().get_id() is not "end":
                traveller=traveller.get_forward()
        traveller.get_forward().set_backward(traveller.get_backward())
        traveller.get_backward().set_forward(traveller.get_forward())
        self.length-=1

    #pops the first node with the indicated id if it exists, else print
    def pop_id(self, space_id=""):
        traveller=self.get_head()
        index=0
        while traveller.get_id() is not space_id and traveller.get_id() is not "end":
            traveller=traveller.get_forward()
            index+=1
        if traveller.get_id() is "end":
            print("No node with id = ", space_id,"found!")
        else:
            self.pop(index)
        

    # prints a string representation of the board in console
    def to_string(self):
        node = self.get_head()
        string = ""
        while node.get_id() is not "end":
            string+= str(node.get_id())
            string+= "-->"
            node=node.get_forward()
        string+=node.get_id()
        print("")
        print(string)

    #returns the board id
    def get_board_id(self):
        return self.id

    #reassigns ids in ascending numerical order
    def reassign_id(self):
         node = self.get_head()
         node=node.get_forward()
         new_id_count = 1
         while node.get_id() is not "end":
             node.set_id(str(new_id_count))
             new_id_count+=1
             node=node.get_forward()

    def scramble_spaces(self, start_index=-1, end_index=100000):
        space_list=[]
        index=0
        index2=0
        traveller = self.get_head().get_forward()
        if start_index == -1 and end_index == 100000:
            while traveller.get_id() is not "end":
                space_list.append(traveller)
                traveller=traveller.get_forward()
            for space in space_list:
                    space.set_forward(None)
                    space.set_backward(None)
            self.get_head().set_forward(self.get_tail())
            self.get_tail().set_backward(self.get_head())
            while len(space_list) > 0:
                random_space = random.choice(space_list)
                self.insert(random_space, 1)
                space_list.remove(random_space)
            self.pop_id("maze_zero")
            self.pop_id("maze_end")
            self.insert(Space(0,"maze_zero"),1)
            self.insert(Space(0,"maze_end"),8)
        elif start_index != -1 and end_index == 100000:
            for i in range(1, start_index):
                index+=1
                traveller = traveller.get_forward()
            anchor = traveller.get_backward()
            while traveller.get_id() is not "end":
                space_list.append(traveller)
                traveller=traveller.get_forward()
            anchor.set_forward(self.get_tail())
            self.get_tail().set_backward(anchor)
            while len(space_list) > 0:
                random_space = random.choice(space_list)
                self.insert(random_space, index)
                space_list.remove(random_space)
        else:
            for i in range(1, start_index):
                index+=1
                traveller = traveller.get_forward()
            anchor = traveller.get_backward()
            index2+=index
            for i in range(1, end_index - start_index):
                if traveller.get_id() is not "end":
                    index2+=1
                    space_list.append(traveller)
                    traveller=traveller.get_forward()
            reacher = traveller.get_forward()
            anchor.set_forward(reacher)
            reacher.set_backward(anchor)
            while len(space_list) > 0:
                random_space = random.choice(space_list)
                self.insert(random_space, index)
                space_list.remove(random_space)
            
             
    #swaps spaces
    def swap_spaces(self, location1, location2): #1 < locations < length - 1, location1 != location2
        print("Locations: ", location1, location2)
        if location1 != location2:
            traveller1 = self.get_head()
            traveller2 = self.get_head()
            for i in range(1, location1):
                if traveller1.get_forward().get_id() is not "end":
                    traveller1=traveller1.get_forward()
            for i in range(1, location2):
                if traveller2.get_forward().get_id() is not "end":
                    traveller2=traveller2.get_forward()
                    
            temp1=copy.deepcopy(traveller1)
            temp2=copy.deepcopy(traveller2)
            
            if traveller1.get_forward() is not traveller2 and traveller2.get_forward() is not traveller1 and abs(location1-location2) > 1:
                print("1")
                traveller1.get_forward().set_backward(traveller2)
                traveller2.get_forward().set_backward(traveller1)
                traveller1.get_backward().set_forward(traveller2)
                traveller2.get_backward().set_forward(traveller1)
                traveller1.set_forward(traveller2.get_forward())
                traveller1.set_backward(traveller2.get_backward())
                traveller2.set_forward(temp1.get_forward())
                traveller2.set_backward(temp1.get_backward())
                
            elif traveller1.get_forward() is traveller2:
                print("2")
                traveller1.get_backward().set_forward(traveller2)
                traveller2.get_forward().set_backward(traveller1)
                traveller2.set_forward(traveller1)
                traveller1.set_backward(traveller2)
                traveller2.set_backward(temp1.get_backward())
                traveller1.set_forward(temp2.get_forward())

            elif traveller2.get_forward() is traveller1:
                print("3")
                traveller2.get_backward().set_forward(traveller1)
                traveller1.get_forward().set_backward(traveller2)
                traveller1.set_forward(traveller2)
                traveller1.set_backward(traveller2.get_backward())
                traveller2.set_backward(traveller1)
                traveller2.set_forward(temp1.get_forward())

    #attaches another board onto self, reassigning self's end id and other's start id
    def combine(self, other):          
        self_tail = self.get_tail()
        other_head = other.get_head()
        self_tail.set_forward(other_head)
        other_head.set_backward(self_tail)
        other_head.set_id("begin")
        self_tail.set_id("finish")
        self.set_tail(other.get_tail())
        return self
            

    #uses variable-point crossover, can change later
    #returns two children of varying length, so we don't end up getting same size boards over and over
    def generate_children(self, other):
        parent1 = copy.deepcopy(self)
        parent2 = copy.deepcopy(other)
        point1 = random.randint(3, self.get_length()-1)
        point2 = random.randint(3, other.get_length()-1)

        traveller1 = parent1.get_head()
        traveller2 = parent2.get_head()

        for i in range(1, point1 - 1): #chooses two random points for crossover
            traveller1=traveller1.get_forward()
        for j in range(1, point2 - 1):
            traveller2=traveller2.get_forward()

        temp1 = copy.deepcopy(traveller1)
        temp2 = copy.deepcopy(traveller2)
        
        traveller1.get_backward().set_forward(traveller2)
        traveller2.get_backward().set_forward(traveller1)
        traveller1.set_backward(temp2.get_backward())
        traveller2.set_backward(temp1.get_backward())

        parent1.update_length() #renews the length
        parent2.update_length()
        
        return (parent1, parent2)

    def to_list(self):
        node = self.get_head()
        board_list = []
        while node.get_id() is not "end":
            board_list.append(node)
            node=node.get_forward()
        return board_list

    def mutate(self):
        if self.get_board_id() is "normal":
            deviation = abs(15 - self.get_length())
            if self.get_length() > 15:
                if random.random() < (deviation * .07):
                    self.pop(random.randint(1,self.get_length()-1))
            elif self.get_length() < 15:
                if random.random() < (deviation * .3):
                    self.insert(Space(([4, 5, 6], random.randint(1, 4), random.randint(-4, -1)), random.randint(1,600)),random.randint(1, self.get_length()-1))
            if random.random() < .2:
                self.insert(Space(([4, 5, 6], random.randint(1, 4), random.randint(-4, -1)), random.randint(1,600)), random.randint(1, self.get_length()-1))
        if self.get_board_id() is "maze":
            self.scramble_spaces()
            

# Player is a pointer that navigates through Spaces until it hits the "end" Space.
class Player:
    
    # initialization
    def __init__(self, given_id=""):
        self.id = given_id
        self.position = None

    # sets the Player's position to a given space
    def set_position(self, given_space):
        self.position = given_space
    
    # returns the Space the Player is on
    def get_position(self):
        return self.position

    # returns a number from 1-6, used for movement
    def player_roll(self):
        return random.randrange(1, 7)
 
    # move Player based on board type and their roll
    def move(self, roll, board_type):   
        if board_type == "normal":
            for i in range(roll):
                if self.get_position().get_id() is "finish":
                    self.set_position(self.get_position().get_forward())
                    break
                if self.get_position().get_id() is not "end":
                    self.set_position(self.get_position().get_forward())

        # this board type models Demon Island's Cave maze
        if board_type == "maze":

            current_space_id = self.get_position().get_id()

            tag = "" # used for jumping to a specific space
            roll_normally = False # is the die's value used normally?

            # Meant to simulate stopping at the maze entrance,
            # -----------------------------------------------------
            if current_space_id == "start":
                self.set_position(self.get_position().get_forward())
            # -----------------------------------------------------

            elif current_space_id == "maze_zero": # entrance: roll to decide which tile you move to
                roll_normally = True

            elif current_space_id == "maze_one": # one: even = maze_four, odd = exit

                if roll % 2 == 0:
                    tag = "maze_four"
                else:
                    tag = "maze_end"

            elif current_space_id == "maze_two": # two: roll and move to that maze tile
                
                tag = "maze_zero"
                roll_normally = True

            elif current_space_id == "maze_three": # three: exit (2, 5), 2 (anything else)

                if roll == 2 or roll == 5:
                    tag = "maze_end"
                else:
                    tag = "maze_two"

            elif current_space_id == "maze_four": # four: any other tile (1-3, 5-6) or start (4)

                if roll == 4: # roll 4 sends to start
                    tag = "start"
                else:
                    tag = "maze_zero"
                    roll_normally = True

            elif current_space_id == "maze_five": # adapting five, since combat doesn't exist: 5 exits, anything else stays

                if roll == 5:
                    tag = "maze_end"

            elif current_space_id == "maze_six": # six: exit or itself, must roll at least 10 with 3 rolls

                roll_two = self.player_roll()
                roll_three = self.player_roll()
                print("Rolls 2 and 3: ", roll_two, roll_three)
                if roll + roll_two + roll_three >= 10:
                    tag = "maze_end"

            else: # outside of the maze
                roll_normally = True

            # done with tiles, movement happens below

            if tag != "":

                    # search forward
                    while self.get_position().get_id() != tag:
                        if self.get_position().get_forward() != None and self.get_position().get_id() is not "finish" and self.get_position().get_id() is not "end":
                            self.set_position(self.get_position().get_forward())
                        else:
                            break

                    # if not in forward, check backward
                    if self.get_position().get_id() != tag:
                        while self.get_position().get_id() != tag:
                            if self.get_position().get_backward() != None and self.get_position().get_id() is not "begin" and self.get_position().get_id() is not "start":
                                self.set_position(self.get_position().get_backward())
                            else:
                                break

            if roll_normally:
                for i in range(roll):
                        if self.get_position().get_forward() != None:
                            self.set_position(self.get_position().get_forward())

#
# main is here
#

#
# TRAVERSE PARAMETER NOTES
#
# Give a tuple if you need to roll for an effect
# ([list of successful numbers], spaces to jump on success, spaces to jump on fail)
def main():
    A = Space(0, "start") # ---------- Spaces ----------
    B = Space(([1, 3, 5], 1, -1), "B")
    C = Space(0, "C")
    D = Space(0, "D")
    E = Space(([4, 5, 6], 0, -2), "E")
    F = Space(0, "F")
    G = Space(([1, 3, 5], 1, 0), "G")
    H = Space(0, "H")
    I = Space(([1, 2, 5, 6], 0, -3), "I")
    J = Space(0, "end")

    before_cave = Space(0, "maze_zero")
    cave_one = Space(0, "maze_one")
    cave_two = Space(0, "maze_two")
    cave_three = Space(0, "maze_three")
    cave_four = Space(0, "maze_four")
    cave_five = Space(0, "maze_five")
    cave_six = Space(0, "maze_six")
    after_cave = Space(0, "maze_end")

    before_cave1 = Space(0, "maze_zero")
    cave_one1 = Space(0, "maze_one")
    cave_two1 = Space(0, "maze_two")
    cave_three1 = Space(0, "maze_three")
    cave_four1 = Space(0, "maze_four")
    cave_five1 = Space(0, "maze_five")
    cave_six1 = Space(0, "maze_six")
    after_cave1 = Space(0, "maze_end")

    game_board = Board("maze")
    game_board.insert(after_cave, 1)
    game_board.insert(cave_six, 1)
    game_board.insert(cave_five, 1)
    game_board.insert(cave_four, 1)
    game_board.insert(cave_three, 1)
    game_board.insert(cave_two, 1)
    game_board.insert(cave_one, 1)
    game_board.insert(before_cave, 1)
    game_board.pop_id("middle")

    game_board2 = Board("maze")
    game_board2.insert(after_cave1, 1)
    game_board2.insert(cave_six1, 1)
    game_board2.insert(cave_five1, 1)
    game_board2.insert(cave_four1, 1)
    game_board2.insert(cave_three1, 1)
    game_board2.insert(cave_two1, 1)
    game_board2.insert(cave_one1, 1)
    game_board2.insert(before_cave1, 1)
    game_board2.pop_id("middle")

    straight_board = Board("normal")
    straight_board.insert(B)
    straight_board.insert(C)
    straight_board.insert(D)
    straight_board.insert(E)
    straight_board.insert(F)
    straight_board.insert(G)
    straight_board.insert(H)
    straight_board.insert(I)
    straight_board.pop_id("middle")

    P_red = Player("Red") # ---------- Players ----------
    P_red.set_position(game_board.get_head()) 
        
    for i in range(0,9):
        straight_board.mutate()
        game_board.to_string()
        game_board.mutate()
        game_board2.mutate()

    straight_board.reassign_id()
    game_board.combine(straight_board).to_string()
    game_board.combine(game_board2).to_string()

    while (P_red.get_position()).get_id() is not "end":
        # Player rolls first
        roll = P_red.player_roll()
        print("Player location: ", P_red.get_position().get_id())
        print("Player rolls: ", roll)
        P_red.move(roll, P_red.get_position().get_board_id())


    game_board.to_string()
    
    return game_board

if __name__ == "__main__":
    main()
