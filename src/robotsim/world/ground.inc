define fenceHorizontal model( 
	color "yellow"
 	size [101 1 2.5] 
	block( 
	points 4 
	point[0] [0 0]
 	point[1] [1 0]
 	point[2] [1 1] 
	point[3] [0 1]
	z [0 1] )
)
define fenceVertical model( 
	color "yellow"  
	size [1 64.5 2.5]  
	block(  
	points 4  
	point[0] [0 0]  
	point[1] [1 0]  
	point[2] [1 1]  
	point[3] [0 1] 
z [0 1] ) 
)
define ground model 
( 
	size [100 63.5 0.01] 
	color "YellowGreen"  
	block 
( 
	points [4] 
	point[0] [0 0] 
	point[1] [0 1] 
	point[2] [1 1] 
	point[3] [1 0] 
	z [0 0.5])
)
define pergola model
(
	size [1.7 4.5 0.5]
	color "DarkGreen"  
	block
(
 	points [4]
	point[0] [0 0]
 	point[1] [0.5 0]
	point[2] [0.5 3.5]
 	point[3] [0 3.5]
 	z [0 0.5]
)
	block
 (
 	points [4]
 	point[0] [0.5 0.2]
 	point[1] [0.9 0.2]
	 point[2] [0.9 3.3]
 	point[3] [0.5 3.3]
 	z [0 0.5]
 )
	 block
 (
	points [4]
 	point[0] [0.9 0.4]
 	point[1] [1.1 0.4]
 	point[2] [1.1 3.1]
 	point[3] [0.9 3.1]
 	z [0 0.5]
)
	  block
(
	 points [4]
 	point[0] [-0.4 0.2]
	 point[1] [0 0.2]
 	point[2] [0 3.3]
 	point[3] [-0.4 3.3]
 	z [0 0.5]
 )
	block
 (
	 points [4]
 	point[0] [-0.4 0.4]
	point[1] [-0.6  0.4]
	 point[2] [-0.6  3.1]
 	point[3] [-0.4 3.1]
 	z [0 0.5]
)
)
