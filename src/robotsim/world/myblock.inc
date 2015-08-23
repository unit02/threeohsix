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


define fenceHorizontal model(
 	color "yellow" 
 	size [91 1 2.5] 	
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
 	size [1 61 2.5] 	
	block( 
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

define ground model
(
  size [90 60 0.01]
  color "YellowGreen"  
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

define pergola model
(
  size [1.7 3.5 0.5]
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

# define weed
define weed model
( 
  size [0.50 0.50 0.50]  
  color "ForestGreen"
  #base
  block( 
	points 4  
	point[0] [0 0] 
	point[1] [1 0] 
	point[2] [1 1] 
	point[3] [0 1] 
	z [0 0.05] 
  )
  #poky bit
  block( 
	points 4  
	point[0] [0 0] 
	point[1] [0.2 0] 
	point[2] [0.2 0.2] 
	point[3] [0 0.2] 
	z [0.05 0.6] 
  )
  #poky bit
  block( 
	points 4  
	point[0] [0.4 0] 
	point[1] [0.6 0] 
	point[2] [0.6 0.2] 
	point[3] [0.4 0.2] 
	z [0.05 1] 
  )
  #poky bit
  block( 
	points 4  
	point[0] [0.8 0] 
	point[1] [1 0] 
	point[2] [1 0.2] 
	point[3] [0.8 0.2] 
	z [0.05 0.9] 
  )
  #poky bit
  block( 
	points 4  
	point[0] [0 0.4] 
	point[1] [0.2 0.4] 
	point[2] [0.2 0.6] 
	point[3] [0 0.6] 
	z [0.05 0.8] 
  )
  #poky bit
  block( 
	points 4  
	point[0] [0.4 0.4] 
	point[1] [0.6 0.4] 
	point[2] [0.6 0.6] 
	point[3] [0.4 0.6] 
	z [0.05 0.7] 
  )
  #poky bit
  block( 
	points 4  
	point[0] [0.8 0.4] 
	point[1] [1 0.4] 
	point[2] [1 0.6] 
	point[3] [0.8 0.6] 
	z [0.05 1] 
  )
  #poky bit
  block( 
	points 4  
	point[0] [0 0.8] 
	point[1] [0.2 0.8] 
	point[2] [0.2 1] 
	point[3] [0 1] 
	z [0.05 0.6] 
  )
  #poky bit
  block( 
	points 4  
	point[0] [0.4 0.8] 
	point[1] [0.6 0.8] 
	point[2] [0.6 1] 
	point[3] [0.4 1] 
	z [0.05 1] 
  )
  #poky bit
  block( 
	points 4  
	point[0] [0.8 0.8] 
	point[1] [1 0.8] 
	point[2] [1 1] 
	point[3] [0.8 1] 
	z [0.05 0.9] 
  )
) 
