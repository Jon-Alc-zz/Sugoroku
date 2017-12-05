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

class Space:
    
    def __init__(self, given_distance=0, given_id=""):
        self.backward = None
        self.forward = None
        self.distance = given_distance
        self.id = given_id

    def set_backward(self, given_space):
        self.backward = given_space

    def set_forward(self, given_space):
        self.forward = given_space

    def get_backward(self):
        return self.backward

    def get_forward(self):
        return self.forward

    def traverse(self):
        return self.distance

    def get_id(self):
        return self.id

class Player:
    
    def __init__(self, given_id=""):
        self.id = given_id
        self.position = None

    def set_position(self, given_space):
        self.position = given_space
    
    def get_position(self):
        return self.position

    def player_roll(self):
        return random.randrange(1, 7)


A = Space(0, "start")
B = Space(1, "B")
C = Space(0, "C")
D = Space(0, "D")
E = Space(-2, "E")
F = Space(0, "F")
G = Space(1, "G")
H = Space(0, "H")
I = Space(-3, "I")
J = Space(0, "end")
A.set_forward(B)
B.set_backward(A); B.set_forward(C)
C.set_backward(B); C.set_forward(D)
D.set_backward(C); D.set_forward(E)
E.set_backward(D); E.set_forward(F)
F.set_backward(E); F.set_forward(G)
G.set_backward(F); G.set_forward(H)
H.set_backward(G); H.set_forward(I)
I.set_backward(H); I.set_forward(J)
J.set_backward(I)
P_red = Player("Red")
P_red.set_position(A)

while P_red.get_position().get_id() is not "end":
    move = P_red.player_roll()
    print("Player location: ", P_red.get_position().get_id())
    print("Player rolls: ", move)
    for i in range(move):
        if P_red.get_position().get_forward() != None:
            P_red.set_position(P_red.get_position().get_forward())
    effect = P_red.get_position().traverse()
    print("Player location: ", P_red.get_position().get_id())
    print("Location traverse: ", P_red.get_position().traverse())
    if effect > 0:
        for i in range(effect):
            if P_red.get_position().get_forward() != None:
                P_red.set_position(P_red.get_position().get_forward())
    else:
        for i in range(abs(effect)):
            if P_red.get_position().get_backward() != None:
                P_red.set_position(P_red.get_position().get_backward())
                
                
                
                
                