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

BOARD_LENGTH = 15

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

    # return params used for determining randomness
    def is_random_space(self):
        check = True
        if isinstance(self.traverse_params, tuple):
            check = False
        elif self.traverse_params!=0:
            check = False
        return check

    
    def set_traverse_params(self, given_traverse_params=0):
        self.traverse_params = given_traverse_params

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
            if traveller is not None and traveller.get_id() is not "end":
                traveller=traveller.get_forward()
            else:
                break
        given_space.set_backward(traveller.get_backward())
        given_space.set_forward(traveller)
        traveller.get_backward().set_forward(given_space)
        traveller.set_backward(given_space)
        given_space.set_board_id(self.id)
        self.length+=1
        
    # pops a node at location, 1<location<length-1
    def pop(self, pop_location):
        traveller=self.get_head()
        for i in range(0, pop_location):
            if traveller.get_forward().get_id() is not "end":
                traveller=traveller.get_forward()
        traveller.get_forward().set_backward(traveller.get_backward())
        traveller.get_backward().set_forward(traveller.get_forward())
        self.length-=1

    # pops the first node with the indicated id if it exists, else print
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
            
    # change number of spaces in bridge board
    def modify_bridge_spaces(self):
        if random.random() <.95:
            """# go through board and remove specially tagged spaces
            pointer = self.get_head().get_forward()
            back_pointer = self.get_head()

            while pointer.get_id() != "end":

                if pointer.get_id() != "": # delete tagged spaces, including "end"
                    temp = pointer
                    pointer = pointer.get_forward()
                    back_pointer.set_forward(pointer)
                    del(temp)

                else:
                    pointer = pointer.get_forward() # move both pointers forward
                    back_pointer = back_pointer.get_forward()

            self.update_length()

            # modify board length
            while self.get_length() < 15: # bridge should be 15-25 spaces
                self.insert(Space())

            for i in range(random.randrange(0, 5)): 
                self.insert(Space())

            while self.get_length() > 20:
                self.pop(self.get_length() - 1)"""
            traveller=self.get_head().get_forward()
            delete_count=0
            index=1
            while traveller.get_id() is not "end":
                if traveller.get_id() not in ["fall", "fall_start", "path_join"] and random.random() < .1:
                    self.pop(index)
                    delete_count+=1
                    index-=1
                traveller=traveller.get_forward()
                index+=1
            if delete_count>0:
                for i in range(0, random.randint(delete_count-1, delete_count+1)):
                    self.insert(Space(), random.randint(1, self.get_length()-1))
            traveller=self.get_head().get_forward()
            index=1
            while traveller.get_id() is not "end":
                if traveller.get_id() not in ["fall", "fall_start", "path_join"]:
                    traveller.set_id(str(index))
                    index+=1
                traveller=traveller.get_forward()
            

    # add tags to bridge board type
    def add_tags(self):

        pointer = self.get_head().get_forward()
        pointer.set_id("fall") # one fall space guaranteed
        pointer = pointer.get_forward()

        for i in range((int)((self.get_length() / 2) - 1)):
            if random.random() < .33: # 33% chance to create a fall space
                pointer.set_id("fall")
            pointer = pointer.get_forward()
        
        pointer = pointer.get_forward() # generate "fall_start" around halfway point
        pointer.set_id("fall_start")

        while pointer.get_forward().get_id() != "end":
            pointer = pointer.get_forward()

        pointer.set_id("path_join")

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
        combined_board=Board()
        combined_board.pop_id("middle")
        """self_copy= copy.deepcopy(self)
        other_copy = copy.deepcopy(other)
        
        self_tail = self_copy.get_tail()
        print(self_copy.get_head().get_id())
        print(self_tail.get_id())
        
        other_head = other_copy.get_head()
        print(other_head.get_id())
        print(other_copy.get_tail().get_id())
        
        self_tail.set_forward(other_head)
        other_head.set_backward(self_tail)
        
        other_head.set_id("begin")
        self_tail.set_id("finish")
        
        print(self_tail.get_forward().get_id())
        print(other_head.get_backward().get_id())
        
        self_copy.set_tail(other_copy.get_tail())

        self_copy.to_string()"""

        self_walker=self.get_head()
        while self_walker.get_forward() is not None and self_walker.get_id() is not "end":
            self_walker=self_walker.get_forward()
            combined_board.insert(copy.deepcopy(self_walker), combined_board.get_length()-1)
        self_walker.set_id("begin")
        #self_walker.set_forward(finish_space)
        combined_board.insert(copy.deepcopy(self_walker), combined_board.get_length()-1)
        other_walker=other.get_head()
        other_walker=other_walker.get_forward()
        while other_walker.get_forward() is not None and other_walker.get_id() is not "end":
            combined_board.insert(copy.deepcopy(other_walker), combined_board.get_length()-1)
            other_walker=other_walker.get_forward()
        end_space=Space(0,"end")
        combined_board.insert(end_space, combined_board.get_length()-1)
        combined_board.set_tail(end_space)

        combined_board.to_string()
        
        return combined_board
            

    #uses variable-point crossover, can change later
    #returns two children of varying length, so we don't end up getting same size boards over and over
    def generate_children(self, other):
        parent1 = copy.deepcopy(self)
        parent2 = copy.deepcopy(other)
        copy1=Board()
        copy2=Board()
        copy1.pop_id("middle")
        copy2.pop_id("middle")
        point1 = random.randint((int)(self.get_length()/2)-1, (int)(self.get_length()/2)+1)
        point2 = random.randint((int)(other.get_length()/2)-1, (int)(other.get_length()/2)+1)

        traveller1 = parent1.get_head()
        traveller2 = parent2.get_head()

        for i in range(1, point1 - 1): #chooses two random points for crossover
            traveller1=traveller1.get_forward()
            if traveller1.get_id() is not "start" and traveller1.get_id() is not "end":
                copy1.insert(copy.deepcopy(traveller1), copy1.get_length()-1)
        for j in range(1, point2 - 1):
            traveller2=traveller2.get_forward()
            if traveller2.get_id() is not "start" and traveller2.get_id() is not "end":
                copy2.insert(copy.deepcopy(traveller2), copy2.get_length()-1)
        while traveller1.get_id() is not "end":
            copy2.insert(copy.deepcopy(traveller1), copy2.get_length()-1)
            traveller1=traveller1.get_forward()
        while traveller2.get_id() is not "end":
            copy1.insert(copy.deepcopy(traveller2), copy2.get_length()-1)
            traveller2=traveller2.get_forward()

        temp1 = copy.deepcopy(traveller1)
        temp2 = copy.deepcopy(traveller2)
        tail1 = copy.deepcopy(parent1.get_tail())
        tail2 = copy.deepcopy(parent2.get_tail())
        
        traveller1.get_backward().set_forward(traveller2)
        traveller2.get_backward().set_forward(traveller1)
        traveller1.set_backward(temp2.get_backward())
        traveller2.set_backward(temp1.get_backward())
        
        parent1.set_tail(tail2)
        parent2.set_tail(tail1)

        parent1.update_length() #renews the length
        parent2.update_length()

        parent1.mutate()
        parent2.mutate()
        
        parent1.reassign_id()
        parent2.reassign_id()
        
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
            deviation = abs(BOARD_LENGTH - self.get_length())
            if self.get_length() > BOARD_LENGTH:
                if random.random() < (deviation * .07):
                    self.pop(random.randint(1,self.get_length()-1))
            elif self.get_length() < BOARD_LENGTH:
                if random.random() < (deviation * .3):
                    roll_list=[]
                    roll_list.append(random.randint(1,6))
                    roll_add_chance=random.random()
                    while roll_add_chance < .5:
                        to_add = random.randint(1,6)
                        if to_add not in roll_list:
                            roll_list.append(to_add)
                        roll_add_chance=random.random()
                    self.insert(Space((roll_list, random.randint(1, 4), random.randint(-4, -1)), random.randint(1,600), random.randint(1, self.get_length()-1)))
            if random.random() < .2:
                if random.random() <.5:
                    roll_list=[]
                    roll_list.append(random.randint(1,6))
                    roll_add_chance=random.random()
                    while roll_add_chance < .5:
                        to_add = random.randint(1,6)
                        if to_add not in roll_list:
                            roll_list.append(to_add)
                        roll_add_chance=random.random()
                    self.insert(Space((roll_list, random.randint(1, 4), random.randint(-4, -1)), random.randint(1,600), random.randint(1, self.get_length()-1)))
                else:
                    self.insert(Space(0,random.randint(1,600)), random.randint(1, self.get_length()-1))
                
            traveller=self.get_head() # 10% chance to assign any single node as a random traverse or nothing
            while traveller.get_forward().get_id() is not "end":
                traveller= traveller.get_forward()
                if random.random() < .1:
                    if random.random() < .5:
                        traveller.set_traverse_params()
                    else:
                        roll_list=[]
                        roll_list.append(random.randint(1,6))
                        roll_add_chance=random.random()
                        while roll_add_chance < .5:
                            to_add = random.randint(1,6)
                            if to_add not in roll_list:
                                roll_list.append(to_add)
                            roll_add_chance=random.random()
                        traveller.set_traverse_params((roll_list, random.randint(1, 4), random.randint(-4, -1)))
            
        if self.get_board_id() is "maze":
            self.scramble_spaces()

        if self.get_board_id() is "bridge":
            self.modify_bridge_spaces()

    def calculate_fitness(self, length, length_m=0, random_m=0, ideal_count=10, maze_m=0):
        fitness=15
        
        if self.get_board_id() is "normal":
            deviation = abs(length - self.get_length()) #length test
            fitness-=length_m * deviation
            traveller = self.get_head()
            rand_count=0 #random test
            while traveller.get_id() is not "end":
                if traveller.is_random_space() is True:
                    rand_count+=1
                traveller=traveller.get_forward()
            fitness+= random_m * rand_count
            
        if self.get_board_id() is "maze": #adds constant count for maze
            return maze_m

        P_test=Player("test") #player test with two players, weighted for ideal maze rolls
        P_test.set_position(self.get_head())
        P_test2=Player("test2")
        P_test2.set_position(self.get_head())
        
        turn_count=1
        turn_count2=1
        while (P_test.get_position()).get_id() is not "end":
            # Player rolls first
            roll = 2
            if random.random() < .33:
                roll=2
            elif random.random() < .66:
                roll=3
            else:
                roll=5
            print("Player location: ", P_test.get_position().get_id())
            print("Player rolls: ", roll)
            P_test.move(roll, P_test.get_position().get_board_id())
            turn_count+=1
        while (P_test2.get_position()).get_id() is not "end":
            # Player rolls first
            roll = 2
            if random.random() < .33:
                roll=2
            elif random.random() < .66:
                roll=3
            else:
                roll=5
            P_test2.move(roll, P_test2.get_position().get_board_id())
            turn_count2+=1
        fitness-=abs(ideal_count - ((turn_count+turn_count2)/2))
        
        return fitness
            

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
                if self.get_position().get_id() is "begin":
                    break
                if self.get_position().get_id() is not "end":
                    self.set_position(self.get_position().get_forward())

            self.get_position().traverse()

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
                        if self.get_position().get_forward() != None and self.get_position().get_id() is not "begin" and self.get_position().get_id() is not "end":
                            self.set_position(self.get_position().get_forward())
                        else:
                            print("space", tag, "not found")
                            break

                    # if not in forward, check backward
                    if self.get_position().get_id() != tag:
                        while self.get_position().get_id() != tag:
                            if self.get_position().get_backward() != None and self.get_position().get_id() is not "begin" and self.get_position().get_id() is not "start":
                                self.set_position(self.get_position().get_backward())
                            else:
                                print("space", tag, "not found")
                                break

            if roll_normally:
                for i in range(roll):
                        if self.get_position().get_forward() != None:
                            self.set_position(self.get_position().get_forward())

        # this models the bridge from Demon Island
        if board_type == "bridge":

            # movement is normal
            for i in range(roll):

                if self.get_position().get_forward() != None and self.get_position().get_id() is not "begin" and self.get_position().get_id() is not "end":
                    self.set_position(self.get_position().get_forward())

            # "fall" spaces jump to "fall_start"
            if self.get_position().get_id() == "fall":
                while self.get_position().get_id() != "fall_start":
                    if self.get_position().get_forward() != None:
                        self.set_position(self.get_position().get_forward())
                    else: # this should never happen
                        print("fall_start not found")
                        break

            # end of bridge, jump straight to path_join
            if self.get_position().get_forward() != None and self.get_position().get_forward().get_id() == "fall_start":
                while self.get_position().get_id() != "path_join":
                    if self.get_position().get_forward() != None:
                        self.set_position(self.get_position().get_forward())
                    else: # this should never happen
                        print("path_join not found")
                        break


def combine_best_subboards(final_board_list, normal_count, maze_count, bridge_count):
    n_count=normal_count
    m_count=maze_count
    b_count=bridge_count
    combination_list=[]
    fitness_count=0
    final_list = sorted(final_board_list, key=lambda board: board.calculate_fitness(BOARD_LENGTH, .3, .4, 10, 0), reverse=True)
    base_board = random.choice(final_list)
    fitness_count+=base_board.calculate_fitness(BOARD_LENGTH, .3, .4, 10, 0)

    if base_board.get_board_id() is "normal":
        n_count-=1
    elif base_board.get_board_id() is "maze":
        m_count-=1
    elif base_board.get_board_id() is "bridge":
        b_count-=1
        
    for i in range(0, n_count):
        for board in final_list:
            if board.get_board_id() is "normal":
                combination_list.append(board)
                fitness_count+=board.calculate_fitness(BOARD_LENGTH, .3, .4, 10, 0)
                final_list.remove(board)
                break

    for i in range(0, m_count):
        for board in final_list:
            if board.get_board_id() is "maze":
                combination_list.append(board)
                fitness_count+=board.calculate_fitness(BOARD_LENGTH, .3, .4, 10, 0)
                final_list.remove(board)
                break

    for i in range(0, b_count):
        for board in final_list:
            if board.get_board_id() is "bridge":
                combination_list.append(board)
                fitness_count+=board.calculate_fitness(BOARD_LENGTH, .3, .4, 10, 0)
                final_list.remove(board)
                break

    while len(combination_list) > 0:
        append_board=random.choice(combination_list)
        base_board=base_board.combine(append_board)
        combination_list.remove(append_board)

    return base_board
        
        

def generate_successors(board_list):
    potential_list = sorted(board_list, key=lambda board: board.calculate_fitness(BOARD_LENGTH, .3, .4, 10, 0), reverse=True)
    new_list=[]
    for i in range(0,10):
        if potential_list[i].get_board_id() is "normal" and potential_list[i+1].get_board_id() is "normal":
            children = potential_list[i].generate_children(potential_list[i+1])
            new_list.append(children[0])
            new_list.append(children[1])
            
    for board in potential_list:
        if board.get_board_id() is "maze":
            board.mutate()
            new_list.append(board)

    for board in potential_list:
        if board.get_board_id() is "bridge":
            board.mutate()
            new_list.append(board)
            
    return new_list
    
    

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

    initial_population=[]
    for i in range(0,10):
        initial_population.insert(0, Board("normal"))
        normal_board=initial_population[0]
        for j in range(0,10):
            if random.random()<.5:
                normal_board.insert(Space(0,random.randint(1,600)), random.randint(1, normal_board.get_length()-1))
            else:
                roll_list=[]
                roll_list.append(random.randint(1,6))
                roll_add_chance=random.random()
                while roll_add_chance < .5:
                    to_add = random.randint(1,6)
                    if to_add not in roll_list:
                        roll_list.append(to_add)
                    roll_add_chance=random.random()
                normal_board.insert(Space((roll_list, random.randint(1, 4), random.randint(-4, -1)), random.randint(1,600), random.randint(1, normal_board.get_length()-1)))
        normal_board.pop_id("middle")
    for i in range(0,5):
        initial_population.insert(0, Board("maze"))
        maze_board=initial_population[0]
        maze_board.insert(Space(0, "maze_end"), 1)
        maze_board.insert(Space(0, "maze_six"), 1)
        maze_board.insert(Space(0, "maze_five"), 1)
        maze_board.insert(Space(0, "maze_four"), 1)
        maze_board.insert(Space(0, "maze_three"), 1)
        maze_board.insert(Space(0, "maze_two"), 1)
        maze_board.insert(Space(0, "maze_one"), 1)
        maze_board.insert(Space(0, "maze_zero"), 1)
        maze_board.pop_id("middle")
    for i in range(0,5):
        initial_population.insert(0, Board("bridge"))
        bridge_board = initial_population[0]
        bridge_board.pop_id("middle")
        for i in range(0,15):
            bridge_board.insert(Space())
        bridge_board.insert(Space(0, "fall"), 3)
        bridge_board.insert(Space(0, "fall"), 6)
        bridge_board.insert(Space(0, "fall"), 7)
        bridge_board.insert(Space(0, "fall_start"), 10)
        bridge_board.insert(Space(0, "path_join"), 15)

    initial_population[0].to_string()
    initial_population[0].mutate()
    initial_population[0].to_string()
    initial_population[0].mutate()
    initial_population[0].to_string()
    initial_population[0].mutate()
    initial_population[0].to_string()
    initial_population[0].mutate()
    initial_population[0].to_string()
    initial_population[0].mutate()
    initial_population[0].to_string()
    initial_population[0].mutate()
    initial_population[0].to_string()
    
    population_limit=10
    for i in range(0, population_limit):
        next_population=generate_successors(initial_population)
        initial_population=next_population
    """normal_board=Board()
    for j in range(0,10):
        if random.random()<.5:
            normal_board.insert(Space(0,random.randint(1,600)), random.randint(1, normal_board.get_length()-1))
        else:
            roll_list=[]
            roll_list.append(random.randint(1,6))
            roll_add_chance=random.random()
            while roll_add_chance < .5:
                to_add = random.randint(1,6)
                if to_add not in roll_list:
                    roll_list.append(to_add)
                roll_add_chance=random.random()
            normal_board.insert(Space((roll_list, random.randint(1, 4), random.randint(-4, -1)), random.randint(1,600), random.randint(1, normal_board.get_length()-1)))
    normal_board.pop_id("middle")

    normal_board2=Board()
    for j in range(0,10):
        if random.random()<.5:
            normal_board2.insert(Space(0,random.randint(1,600)), random.randint(1, normal_board2.get_length()-1))
        else:
            roll_list=[]
            roll_list.append(random.randint(1,6))
            roll_add_chance=random.random()
            while roll_add_chance < .5:
                to_add = random.randint(1,6)
                if to_add not in roll_list:
                    roll_list.append(to_add)
                roll_add_chance=random.random()
            normal_board2.insert(Space((roll_list, random.randint(1, 4), random.randint(-4, -1)), random.randint(1,600), random.randint(1, normal_board2.get_length()-1)))
    normal_board2.pop_id("middle")

    normal_board.reassign_id()
    normal_board2.reassign_id()
    
    game_board = normal_board.combine(normal_board2)
    game_board.to_string()"""
    game_board=combine_best_subboards(initial_population, 3,1,1)
    
    game_board.to_string()

    """# ---------- Spaces ----------

    # straight board spaces
    A = Space(0, "start")
    B = Space(([1, 3, 5], 1, -1), "B")
    C = Space(0, "C")
    D = Space(0, "D")
    E = Space(([4, 5, 6], 0, -2), "E")
    F = Space(0, "F")
    G = Space(([1, 3, 5], 1, 0), "G")
    H = Space(0, "H")
    I = Space(([1, 2, 5, 6], 0, -3), "I")
    J = Space(0, "end")

    # maze board spaces
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

    # bridge board spaces
    bridgeA = Space()
    bridgeB = Space()
    bridgeC = Space(0, "fall")
    bridgeD = Space()
    bridgeE = Space()
    bridgeF = Space(0, "fall")
    bridgeG = Space(0, "fall")
    bridgeH = Space()
    bridgeI = Space()
    bridgeJ = Space(0, "fall_start")
    bridgeK = Space()
    bridgeL = Space()
    bridgeM = Space()
    bridgeN = Space()
    bridgeO = Space()
    bridgeP = Space()
    bridgeQ = Space()
    bridgeR = Space(0, "path_join")
    bridgeS = Space()

    game_board3 = Board("bridge")
    game_board3.insert(bridgeS)
    game_board3.insert(bridgeR)
    game_board3.insert(bridgeQ)
    game_board3.insert(bridgeP)
    game_board3.insert(bridgeO)
    game_board3.insert(bridgeN)
    game_board3.insert(bridgeM)
    game_board3.insert(bridgeL)
    game_board3.insert(bridgeK)
    game_board3.insert(bridgeJ)
    game_board3.insert(bridgeI)
    game_board3.insert(bridgeH)
    game_board3.insert(bridgeG)
    game_board3.insert(bridgeF)
    game_board3.insert(bridgeE)
    game_board3.insert(bridgeD)
    game_board3.insert(bridgeC)
    game_board3.insert(bridgeB)
    game_board3.insert(bridgeA)
    game_board3.pop_id("middle")

    # ---------- Players ----------
    P_red = Player("Red")
    P_red.set_position(game_board3.get_head()) 

    # mutation, generating, and genetic algorithms
    for i in range(0, 9):

        straight_board.mutate()
        game_board.mutate()
        game_board2.mutate()
        game_board3.mutate()

    straight_board.reassign_id()
    game_board3.reassign_id()
    game_board3.add_tags()
    game_board3.to_string()

    game_board.combine(straight_board).to_string()
    game_board.combine(game_board2).to_string()
    game_board.combine(game_board3).to_string()

    # play the game
    while (P_red.get_position()).get_id() is not "end":
        # Player rolls first
        roll = P_red.player_roll()
        print("Player location: ", P_red.get_position().get_id())
        print("Player rolls: ", roll)
        P_red.move(roll, P_red.get_position().get_board_id())

    game_board.to_string()

    print(game_board.calculate_fitness(BOARD_LENGTH, .4, .5, 10, 2))"""

    return game_board

if __name__ == "__main__":
    main()
