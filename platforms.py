from tiles import *

level = 0

if level == 0:
    platforms = [
            GrassMid(150, 800),
            GrassMid(250, 800),
            GrassMid(350, 800),
            Grass(250, 300),
            Grass(450, 300),
            Grass(650, 700),
            Grass(850, 600),
            GrassHillRight(700, 400),
            GrassMid(650, 400),
            GrassRight(450, 800),
            GrassHillRight(0, 700),
            GrassHillRight2(50, 800)
        ]

elif level == 1:
    platforms = [
        GrassMid(150, 800),
        GrassMid(250, 800),
        GrassMid(350, 800),
        # Grass(250, 300),
        # Grass(450, 300),
        # Grass(650, 700),
        # Grass(850, 600),
        # GrassHillRight(700, 400),
        # GrassMid(650, 400),
        GrassRight(450, 800),
        GrassHillRight(0, 700),
        GrassHillRight2(50, 800)
    ]

doors = [
    Door(450, 700),
    Door(250, 700),
    Door(250, 200),
    Door(450, 200),
    Door(650, 300),
    Door(650, 600),
    Door(850, 500),
    # Door_2(),
    # Door_2(),
    # Door_2(),
    # Door_2(),
    # Door_2(),
    # Door_2(),
    # Door_2(),
    Door_3(450, 659),
    Door_3(250, 659),
    Door_3(250, 159),
    Door_3(450, 159),
    Door_3(650, 259),
    Door_3(650, 559),
    Door_3(850, 459),

]