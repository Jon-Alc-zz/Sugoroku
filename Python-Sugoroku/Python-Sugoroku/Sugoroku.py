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
P_red = Player("Red") # ---------- Players ----------
P_red.set_position(A) 

#
# player movement
#
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