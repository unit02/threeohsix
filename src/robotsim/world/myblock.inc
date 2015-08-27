define treetrunk model(	
 	color "brown" 
        gui_move 0
	size [0.5 0.5 1.8] 	
	drive "diff" 
	block( 
	
	points 4 
	point[0] [0 0] 
	point[1] [1 0] 
	point[2] [1 1] 
	point[3] [0 1]
	z [0 1] )	
)

define tree model(	
 	gui_move 0
	size [5.5 1 1] 	
	block( 
	color "DarkGreen" 
	points 4 
	point[0] [0 0] 
	point[1] [1 0] 
	point[2] [1 1] 
	point[3] [0 1]
	z [0 1] )	
)  



define post model(
        gui_move 0	
	color "grey" 
 	size [0.5 0.5 2.8] 
	block( 
	points 3 
	point[0] [0 0] 
	point[1] [1 0] 
	point[2] [1 1] 
	z [0 1] )
	
)


define driveway model
(
  gui_move 0
  size [30 10 0.015]
  color "grey"  
  obstacle_return 0
  block
  (
    points [4]
    point[0] [0 0]
    point[1] [0 1]
    point[2] [1 1]
    point[3] [1 0]
    z [0 0.5]
  )
)
