# Path-Second-Pass
FreeCAD Macro that collects polygons reamaining after a Path profile or pocket operation.

### Introduction 

**[FreeCAD](https://freecad.org)** is a Free Libre Open Source multi-platform CAD/CAM/FEM suite.
  One of the Workbenches it provides is the Path Workbench. That workbench takes edges and/or faces constructed in FreeCAD and produces CNC paths to pocket the face(s) and/or to profile the edges, among other possible operations. How much of the original FreeCAD geometry gets cut depends on the diameter of tool. With a larger diameter tool a face can be pocketed quickly, but a considerable area of the work piece, at the corners, will be left uncut. With a smaller diameter tool more of the original face gets cut, but the operation takes a longer time. The FreeCAD macro (a python script) provided here finds polygons left uncut by the Path operation and adds them to the FreeCAD document. These polygons can then be cut with a smaller diameter tool without having to go over the already cut portions of the work piece.

### Installation and use
 Copy the files path_second_path.FCMacro and geom2D.py to your local FreeCAD Macro directory. This directory can be set or changed under Macro menu. Select the operations you want to produce the polygons for (currently only Profile and Pocket operations are supported) and execute the macro path_second_path.FCMacro The uncut faces should be added to new groups in the document. Process any of these with new Path jobs as you see fit. Note that the algorithm uses a parameter `minOffset` that determines how far the cutting tool must be before the uncut polygon is added to the document. The current value is 0.2 mm. If this produces too many small polygons, you can edit the value by editing the macro and changing the value in the method `remaining_faces`.

 ### Examples
 The following image shows the polygons found for outside an inside profile operations. The green line shows the tool path.
 
![Sample operation](/Images/remaining_triangles-1.png)

A sample image showing left-over polygon for a pocketing operation with a sharp corner.

![Sample operation](/Images/remaining_triangles-2.png)


### Documentation
A brief description for the geometry used in deriving the polygons is provided here [Documentation](Docs/path_second_pass.pdf "Geometry description").

  ### Note:
  The macro does not currently have extensive tests for edge cases. It was developed largely for personal use and made available publicly in case some one else might find it useful.
  If you do find bugs and have requests for imporovements, please let me know, and I'll see if I can help.
  
## Author

Contact the author via email: muntherhindi[at]gmail[dot]com

