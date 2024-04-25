# Odyssey Tacticians Information and Working Guide.

# Description
_Odyssey Tacticians_: A DSA project by __Abeer Masroor__ and __Mohammad Khadeer Bin Kashif Najam__ a.k.a __The Wanderlusteers__ (Group 10).
Odyssey Tactician is a rendition of the classic conundrum in computer science and optimization theory called the Travelling Salesman Problem (TSP). Odyssey Tactician's main aim is to find the shortest path within the selected number of cities for the salesman going through all the cities exactly once. The project employs two methods that are calculating and displaying the shortest path according to their own Algorithmic logic, One is Held-Karp algorithm and the other is a Greedy Algorithm.

# Information regarding the code files.
- The **UI_files** folder includes all the **.ui** skeleton files for the User interface and will **not** be required to run for the woking of the code.
- The **display_1_pyfile.py** file is for the main screen dialog.
- The **display_2_pyfile.py** file is for the second dialog screen.
- The **display_3.py** file is for the third dialog screen that displays the shortest paths.
- The **plotter.py**file is for plotting the time complexity graph between the two algorithms.
- The **DSA_proj** file contains all the functions for the algorithms and making of the cyclic graph.
- The **map_rc.py** file contains the ui to py converted code for the generation of the background image being used in the display. The file does not need to be run seperately.

# Working guide for the code
- To **run** the code, go to the **display_1_pyfile.py** and then click on the run button. This is because the main driver function that runs all the classes and the files is in this file.
- Doing the above mentioned steps will only show the shortest path in the dialog and a cyclic graph of all the desired cities with their distances.
- To **run** the graph of the time complexities between the two algorithms, run the file named *plotter.py*. 
- The **plotter.py** will take time to run and show output. It took approximately *1-5 minutes* during our testing.
- Trying to run any other file than **display_1_pyfile.py** and **plotter.py** will **not** display anything on the screen or the terminal.

# Libraries used for the code
- **PyQt5** library with imports **QtCore, QtGui, QtWidgets**.
- **sys** library
- **networkx** library
- **matplotlib** library
- **time** and **random** library

it is advised to have the above mentioned libraries installed in your python directory to ensure smooth running for your code.