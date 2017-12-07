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
    def __init__(self, given_traverse_params=0, given_id=""):
        self.backward = None
        self.forward = None
        self.traverse_params = given_traverse_params
        self.id = given_id

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
    
    #print the node
    def prin(self):
        print("----id----")
        print("id [",self.id,"]")
        if self.id != "start":
            print("from", self.backward.get_id())
        if self.id != "end":
            print("to", self.forward.get_id())
        if isinstance(self.traverse_params, tuple):
            print("traverse", self.traverse_params)


class Board:

    #initialization
    def __init__(self):
        self.length = 3
        self.head = Space(0, "start")
        middle_space = Space(0,"middle")
        self.tail = Space(0, "end")
        self.head.set_forward(middle_space)
        middle_space.set_backward(self.head)
        middle_space.set_forward(self.tail)
        self.tail.set_backward(middle_space)

    #returns the length
    def get_length(self):
        return self.length

    #returns the head(start)
    def get_head(self):
        return self.head

    #returns the tail(end)
    def get_tail(self):
        return self.tail

    #updates the length because it might be changed during reproduction
    def update_length(self):
        temp_length = 1
        traveller = self.head
        while traveller.get_id() is not "end":
            traveller = traveller.get_forward()
            temp_length+=1
        self.length = temp_length

    #inserts a given node in a location with 1<location<length-1
    def insert(self, given_space, insert_location):
        traveller=self.head
        for i in range(0, insert_location):
            traveller=traveller.get_forward()
        given_space.set_backward(traveller.get_backward())
        given_space.set_forward(traveller)
        traveller.get_backward().set_forward(given_space)
        traveller.set_backward(given_space)
        self.length+=1

    #prints a string representation of the board in console
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

    def generate_children(self, other):
        parent1 = copy.deepcopy(self)
        parent2 = copy.deepcopy(other)
        point1 = random.randint(3, self.get_length()-1)
        point2 = random.randint(3, other.get_length()-1)

        traveller1 = parent1.get_head()
        traveller2 = parent2.get_head()

        for i in range(1, point1 - 1):
            traveller1=traveller1.get_forward()
        for j in range(1, point2 - 1):
            traveller2=traveller2.get_forward()

        temp1 = copy.deepcopy(traveller1)
        temp2 = copy.deepcopy(traveller2)
        
        traveller1.get_backward().set_forward(traveller2)
        traveller2.get_backward().set_forward(traveller1)
        traveller1.set_backward(temp2.get_backward())
        traveller2.set_backward(temp1.get_backward())

        parent1.update_length()
        parent2.update_length()
        
        return (parent1, parent2)

    def to_list(self):
        node = self.get_head()
        board_list = []
        while node.get_id() is not "end":
            board_list.append(node)
            node=node.get_forward()
        return board_list
        
        

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
    A.set_forward(B) # ---------- Connections ----------
    B.set_backward(A); B.set_forward(C)
    C.set_backward(B); C.set_forward(D)
    D.set_backward(C); D.set_forward(E)
    E.set_backward(D); E.set_forward(F)
    F.set_backward(E); F.set_forward(G)
    G.set_backward(F); G.set_forward(H)
    H.set_backward(G); H.set_forward(I)
    I.set_backward(H); I.set_forward(J)
    J.set_backward(I)

    game_board = Board()
    game_board.insert(I,1)
    game_board.insert(H,1)
    game_board.insert(G,1)
    game_board.insert(F,1)

    game_board2 = Board()
    game_board2.insert(E,1)
    game_board2.insert(D,1)
    game_board2.insert(C,1)
    game_board2.insert(B,1)

    P_red = Player("Red") # ---------- Players ----------
    P_red.set_position(game_board.get_head()) 

    #
    # player movement
    #
    generation = 1
    while generation < 10:
        while P_red.get_position().get_id() is not "end":
        
            # Player rolls first
            move = P_red.player_roll()
            print("Player location: ", P_red.get_position().get_id())
            print("Player rolls: ", move)
            for i in range(move):
                if P_red.get_position().get_forward() != None:
                    P_red.set_position(P_red.get_position().get_forward())

            print("Player location: ", P_red.get_position().get_id())

            # Space.traverse() is called
            effect = P_red.get_position().traverse()
            print("Location traverse: ", effect)
            if effect > 0:
                for i in range(effect):
                    if P_red.get_position().get_forward() != None:
                        P_red.set_position(P_red.get_position().get_forward())
            else:
                for i in range(abs(effect)):
                    if P_red.get_position().get_backward() != None:
                        P_red.set_position(P_red.get_position().get_backward())
                        
        new_space = Space(([4, 5, 6], random.randint(1, 6), random.randint(-6, -1)), random.randint(1,600)) # assigns new node with random big number ID
        new_space2 = Space(([4, 5, 6], random.randint(1, 6), random.randint(-6, -1)), random.randint(1,600)) # assigns new node with random big number ID
                          
        """new_space.set_forward(traveller) # insertion done here
        new_space.set_backward(traveller.get_backward())
        traveller.set_backward(new_space)
        traveller.get_backward().set_forward(new_space)"""
        game_board.insert(new_space, random.randint(1, game_board.get_length()-1))
        game_board2.insert(new_space2, random.randint(1, game_board2.get_length()-1))

        P_red.set_position(game_board.get_head()) # player reset done here
        print("\nGeneration: ", generation) 
        generation+=1

    game_board.to_string()
    game_board2.to_string()
    child = game_board.generate_children(game_board2)
    child[0].to_string()
    child[1].to_string()
    return child[0]

if __name__ == "__main__":
    main()