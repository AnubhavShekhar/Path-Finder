# Maze Solving Visualization

This Python script provides a visualization of maze-solving using a simple breadth-first search algorithm. The maze is displayed in the terminal, and the algorithm finds the path from the starting position "O" to the ending position "X" while visualizing the process.

## Requirements

- Python 3.x
- curses library (comes with Python standard library)

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/AnubhavShekhar/Path-Finder.git
   ```

2. Navigate to the directory:

   ```bash
   cd maze-solving-visualization
   ```

3. Run the script:

   ```bash
   python maze_solver.py
   ```

4. Press any key to exit after the visualization is complete.

## Customization

You can customize the maze by modifying the `maze` variable in the `maze_solver.py` script. The maze is represented as a 2D list of characters where "#" represents walls, "O" is the starting point, and "X" is the destination.

Feel free to experiment with different maze configurations.

## Note

This script uses the `curses` library for terminal-based graphics. It may not work correctly in all terminal environments.
