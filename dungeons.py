from tiles import *

Dungeons = {}

class Dungeon:
    def __init__(self,name,weight,arrangement):
        if type(arrangement[0]) != list:
            raise Exception("Dungeon must be a 2D array")

        ySize = len(arrangement)
        xSize = len(arrangement[0])

        if [len(i) == xSize for i in arrangement] != [True] * ySize:
            raise Exception("Dungeon must be a quadrilateral")
        if name in Dungeons:
            raise Exception("A dungeon with that name already exists")
        self.arrangement = arrangement
        if xSize < ySize:self.squareLength = ySize
        else:self.squareLength = xSize
        self.size = [xSize,ySize]
        self.weight = weight
        self.name = name
        Dungeons[name] = self
    def __repr__(self):
        return "DUNGEON OBJECT - "+self.name

Dungeon("Crossroad",10,[["Crossroad"]])
Dungeon("HallwayV",10,[["Vertical"]])
Dungeon("HallwayH",10,[["Horizontal"]])
Dungeon("DeadU",10,[["DeadU"]])
Dungeon("DeadD",10,[["DeadD"]])
Dungeon("DeadL",10,[["DeadL"]])
Dungeon("DeadR",10,[["DeadR"]])
Dungeon("3WayU",10,[["3WayU"]])
Dungeon("3WayD",10,[["3WayD"]])
Dungeon("3WayL",10,[["3WayL"]])
Dungeon("3WayR",10,[["3WayR"]])
Dungeon("CornerDL1",10,[["CornerDL1"]])
Dungeon("CornerDR1",10,[["CornerDR1"]])
Dungeon("CornerUL1",10,[["CornerUL1"]])
Dungeon("CornerUR1",10,[["CornerUR1"]])
Dungeon("Solid",10,[["Solid"]])
Dungeon("Empty",5,[["Empty"]])

Dungeon("Room",1000,
[["CornerUR2","SideU","SideU","SideU","CornerUL2"],
 ["SideL","Horizontal","Horizontal","Horizontal","SideR"],
 ["SideL","Empty","Empty","Empty","SideR"],
 ["CornerDR2","SideD","Empty","SideD","CornerDL2"]])
