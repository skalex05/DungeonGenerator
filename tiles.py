Tiles = {}

class Tile:
    def __init__(self,name,arrangement):
        if type(arrangement[0]) != list:
            raise Exception("Tile must be a 2D array")
        elif len(arrangement) != 3 or [len(i) == 3 for i in arrangement[0:3]] != [True] * 3:
            raise Exception("Tile dimensions must be 3x3")
        if name in Tiles:
            raise Exception("A tile with that name already exists")
        self.arrangement = arrangement
        self.name = name
        Tiles[name] = self
    def __repr__(self):
        return "TILE OBJECT - "+self.name

Tile("Error",
[["X","X","X"],
 ["X","X","X"],
 ["X","X","X"]])

Tile("Empty",
[[" "," "," "],
 [" "," "," "],
 [" "," "," "]])

Tile("Solid",
[["#","#","#"],
 ["#","#","#"],
 ["#","#","#"]])

Tile("Horizontal",
[["#","#","#"],
 [" "," "," "],
 ["#","#","#"]])

Tile("Vertical",
[["#"," ","#"],
 ["#"," ","#"],
 ["#"," ","#"]])

Tile("DeadU",
[["#","#","#"],
 ["#"," ","#"],
 ["#"," ","#"]])

Tile("DeadD",
[["#"," ","#"],
 ["#"," ","#"],
 ["#","#","#"]])

Tile("DeadR",
[["#","#","#"],
 [" "," ","#"],
 ["#","#","#"]])

Tile("DeadL",
[["#","#","#"],
 ["#"," "," "],
 ["#","#","#"]])

Tile("Crossroad",
[["#"," ","#"],
 [" "," "," "],
 ["#"," ","#"]])

Tile("3WayU",
[["#"," ","#"],
 [" "," "," "],
 ["#","#","#"]])

Tile("3WayD",
[["#","#","#"],
 [" "," "," "],
 ["#"," ","#"]])

Tile("3WayL",
[["#"," ","#"],
 [" "," ","#"],
 ["#"," ","#"]])

Tile("3WayR",
[["#"," ","#"],
 ["#"," "," "],
 ["#"," ","#"]])

Tile("CornerDR1",
[["#"," ","#"],
 ["#"," "," "],
 ["#","#","#"]])

Tile("CornerDL1",
[["#"," ","#"],
 [" "," ","#"],
 ["#","#","#"]])

Tile("CornerUR1",
[["#","#","#"],
 ["#"," "," "],
 ["#"," ","#"]])

Tile("CornerUL1",
[["#","#","#"],
 [" "," ","#"],
 ["#"," ","#"]])

Tile("CornerDR2",
[["#"," "," "],
 ["#"," "," "],
 ["#","#","#"]])

Tile("CornerDL2",
[[" "," ","#"],
 [" "," ","#"],
 ["#","#","#"]])

Tile("CornerUR2",
[["#","#","#"],
 ["#"," "," "],
 ["#"," "," "]])

Tile("CornerUL2",
[["#","#","#"],
 [" "," ","#"],
 [" "," ","#"]])

Tile("SideR",
[[" "," ","#"],
 [" "," ","#"],
 [" "," ","#"]])

Tile("SideL",
[["#"," "," "],
 ["#"," "," "],
 ["#"," "," "]])

Tile("SideD",
[[" "," "," "],
 [" "," "," "],
 ["#","#","#"]])

Tile("SideU",
[["#","#","#"],
 [" "," "," "],
 [" "," "," "]])
