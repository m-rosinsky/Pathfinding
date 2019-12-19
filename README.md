# Pathfinding
Showcasing pathfinding Algorithms using Pygame

![img](https://i.imgur.com/brAlI2n.png)

# Start-up Instructions
1) Install pygame
```
python3 -m pip install -U pygame --user
```
2) Run pathfinding.py
```
python3 pathfinding.py
```

# Using the Application
- Drag with left mouse button to create walls
- Drag with right mouse button to erase walls
- Press Space to reset grid
- Press Return to run pathfinding algorithm
- Click anywhere to clear the path after it has been run

- Note the algorithm will not run if there is no solution. The console will simply print "No Solution Possible"

# Version History / Changelog

### 12/16/2019
- Created the skeleton of the visualization
- Added Breadth First Search pathfinding

### 12/17/2019
- Animated path reaching its target

### 12/18/2019
- Restructured code into a cleaner version
- Shoved grid properties and methods into a class instead of having them hang out in global

# Future Plans
- Add more kinds of pathfinding (A*, Dijkstra's, DFS, etc.)
- Save files so mazes created won't be lost
- ~~Animate path reaching target~~
- Add or create a maze generating algorithm (growing tree, maybe something custom)
- Animate nodes being searching during search process
