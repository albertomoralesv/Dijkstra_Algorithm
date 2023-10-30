# Dijkstra_Algorithm (Pygame needed)
To create the graph, you can create as many nodes as needed. To create a node, simply click on the screen, and the node will be created in that position.

To establish connections, you can select any previously created node, which will be highlighted in blue when selected. Then, you should select a second node to which the connection will be created. Once you have two nodes selected (both in blue), the user needs to enter the weight of that connection. It can be a number of any number of digits (if the user enters a non-numeric key, it will not be considered). Once the number is entered, the user should press the ENTER key to confirm the weight, and the connection will be created. If an error is made, you can simply reselect the nodes and repeat the same process.

Once the user has created the graph, they need to set the initial and final nodes. To do this, click either on the "Initial Node" or "Final Node" button. The selected node will be highlighted in blue to indicate it's being selected, and then click on the node you want to set as the initial or final. The selected node will be displayed in the respective box. Once both the initial and final nodes are set, a green button will appear to search for the route. Clicking on this button will execute the Dijkstra's algorithm, and the result of the search, including the total path weight and the route taken, will be displayed in the console. If it's not possible to reach from the initial to the final node, it will be indicated in the console.

At any time, you can change both the Initial and Final nodes within the same graph. By clicking the "Calculate Route" button again, the weight and route between the set nodes will be displayed.

If you need to start over or create a new graph, you can click the "CLEAR" button, and the graph will be reset, and the screen will return to the default state.
