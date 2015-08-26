define treetrunk model(	
 	color "brown" 
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
  size [30 6 0.02]
  color "grey"  
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
