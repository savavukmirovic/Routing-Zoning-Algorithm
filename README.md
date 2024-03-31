# **Routing-Zoning Algorithm**
In this project is implemented an algorithm for routing vehicles to fulfill demand while optimizing distance and capacity constraints. Graphical user interface (GUI) is created with Tkinter for visualizing the resulting routes. When the button is clicked, it displays the routes on the canvas.

- Importing Data: Reads demand and distance data from Excel sheets.
- Utility Functions: Defines utility functions for data manipulation, such as finding nearest neighbors and calculating distances between nodes.
- Preprocessing: Prepares data by handling zero distances and creating dictionaries for easier computation.

## Routing Algorithm:
1. Finds the nearest neighbor for each node.
2. Generates new routes based on pairs of nodes.
3. Calculates the total demand along each route.
4. Computes the total distance along each valid route, considering vehicle capacity constraints.
5. Finds the shortest path using Dijkstra's algorithm.
6. Obtains the final routes for vehicle movement.
7. Converts the node IDs back to their original names for better interpretation.
8. Returns the final vehicle movement paths.

## GUI Setup:

1. Creates a tkinter window (window) for the GUI application.
2. Creates a canvas for displaying the vehicle routes.
3. Configures the canvas with appropriate padding and positioning.
4. Loads an image as a button to trigger the route retrieval.
5. Starts the main event loop with window.mainloop().

## Input:
Input data is imported from excel using pandas. Below is a pictorial description of the input data.

![image](https://github.com/savavukmirovic/Routing-Zoning-Algorithm/assets/126354345/c87ee8dc-7f6c-4ba2-8cdc-97fa43071063)

![image](https://github.com/savavukmirovic/Routing-Zoning-Algorithm/assets/126354345/50a6f0fa-849b-4d54-a041-cbd6f61fe886)

## Output:
![image](https://github.com/savavukmirovic/Routing-Zoning-Algorithm/assets/126354345/21413d08-decc-46e6-b9f3-2d8e98e4a8ae)
