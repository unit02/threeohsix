define myLaser ranger 
( 
  sensor( range [ 0 10 ] fov 60.0 samples 60 ) 
  size [0.100 0.100 0.100] 
  color "black" 
  block( 
	points 4 
	point[0] [0 0] 
	point[1] [0.1 0] 
	point[2] [0.1 0.1] 
	point[3] [0 0.1] 
	z [0 0.1] 
	) 
) 

# define picker
define picker position 
( 
  #properties as name value pairs
  myLaser(pose [ 1.250 0.000 -0.800 0.000 ]) 
  size [2.500 1.500 1.000] 
  drive "diff" 
  velocity_bounds [ -10 10 0 0 -360 360 -90 90 ]

  block( 
	points 4  
	point[0] [0 0] 
	point[1] [1 0] 
	point[2] [1 1] 
	point[3] [0 1] 
	z [0 .5] 
  )

) 

# define carrier
define carrier position 
( 
  #properties as name value pairs
  myLaser(pose [ 0.900 0.000 -0.200 0.000 ])
  size [1.800 1.500 0.500]
  velocity_bounds [ -10 10 0 0 -360 360 -90 90 ] 
  drive "diff" 

  block( 
	points 4  
	point[0] [0 0] 
	point[1] [1 0] 
	point[2] [1 1] 
	point[3] [0 1] 
	z [0 .5] 
  )

) 

# Visitor
define person_visitor position
(
  myLaser(pose [ 0.250 0.000 -1.600 0.000 ])
  drive "diff"
  size [0.550 1.000 1.700]
  velocity_bounds [ -10 10 0 0 -360 360 -90 90 ]	
   #legs
   block 
   (
      color "blue"
      points 4
      point[0]  [ 0 0.1 ]
      point[1]  [ 0.5 0.1 ]
      point[2]  [ 0.5 0.5 ]
      point[3]  [ 0 0.5 ]
      z [0 0.8]
   )
   #legs
   block 
   (
      color "blue"
      points 4
      point[0]  [ 0 0.5 ]
      point[1]  [ 0.5 0.5 ]
      point[2]  [ 0.5 0.9 ]
      point[3]  [ 0 0.9 ]
      z [0 0.8]
   )
   #arms	
   block 
   (  
      color "tan"
      points 4
      point[0]  [ 0.1 0 ]
      point[1]  [ 0.4 0 ]
      point[2]  [ 0.4 0.1 ]
      point[3]  [ 0.1 0.1 ]
      z [0.7 1.35]
   )
   #arms	
   block 
   (  
      color "tan"
      points 4
      point[0]  [ 0.1 0.9 ]
      point[1]  [ 0.4 0.9 ]
      point[2]  [ 0.4 1 ]
      point[3]  [ 0.1 1 ]
      z [0.7 1.35]
   )
   #body	
   block 
   (  
      color "aquamarine"
      points 4
      point[0]  [ 0 0.1 ]
      point[1]  [ 0.5 0.1 ]
      point[2]  [ 0.5 0.9 ]
      point[3]  [ 0 0.9 ]
      z [0.8 1.4]
   )
   #head
   block
   (
      color "tan"
      points 4
      point[0]  [ 0 0.30 ]
      point[1]  [ 0.5 0.3 ]
      point[2]  [ 0.5 0.7 ]
      point[3]  [ 0 0.7 ]
      z [1.4 1.7]
   )
   #eyes
   block
   (
      color "black"
      points 4
      point[0]  [ 0.50 0.35 ]
      point[1]  [ 0.55 0.35 ]
      point[2]  [ 0.55 0.40 ]
      point[3]  [ 0.50 0.4]
      z [1.55 1.6]
   )
  #eyes
   block
   (
      color "black"
      points 4
      point[0]  [ 0.50 0.60 ]
      point[1]  [ 0.55 0.6 ]
      point[2]  [ 0.55 0.65 ]
      point[3]  [ 0.50 0.65 ]
      z [1.55 1.6]
   ) 	
)

# Worker
define person_worker position
(
  myLaser(pose [ 0.250 0.000 -1.600 0.000 ])
  drive "diff"
  size [0.550 1.000 1.750]
  velocity_bounds [ -10 10 0 0 -360 360 -90 90 ]	
   #legs
   block 
   (
      color "brown"
      points 4
      point[0]  [ 0 0.1 ]
      point[1]  [ 0.5 0.1 ]
      point[2]  [ 0.5 0.5 ]
      point[3]  [ 0 0.5 ]
      z [0 0.8]
   )
   #legs
   block 
   (
      color "brown"
      points 4
      point[0]  [ 0 0.5 ]
      point[1]  [ 0.5 0.5 ]
      point[2]  [ 0.5 0.9 ]
      point[3]  [ 0 0.9 ]
      z [0 0.8]
   )
   #arms	
   block 
   (  
      color "tan"
      points 4
      point[0]  [ 0.1 0 ]
      point[1]  [ 0.4 0 ]
      point[2]  [ 0.4 0.1 ]
      point[3]  [ 0.1 0.1 ]
      z [0.7 1.35]
   )
   #arms	
   block 
   (  
      color "tan"
      points 4
      point[0]  [ 0.1 0.9 ]
      point[1]  [ 0.4 0.9 ]
      point[2]  [ 0.4 1 ]
      point[3]  [ 0.1 1 ]
      z [0.7 1.35]
   )
   #body	
   block 
   (  
      color "ForestGreen"
      points 4
      point[0]  [ 0 0.1 ]
      point[1]  [ 0.5 0.1 ]
      point[2]  [ 0.5 0.9 ]
      point[3]  [ 0 0.9 ]
      z [0.8 1.4]
   )
   #head
   block
   (
      color "tan"
      points 4
      point[0]  [ 0 0.30 ]
      point[1]  [ 0.5 0.3 ]
      point[2]  [ 0.5 0.7 ]
      point[3]  [ 0 0.7 ]
      z [1.4 1.7]
   )
   #Workhat
   block
   (
      color "gold"
      points 4
      point[0]  [ 0 0.25 ]
      point[1]  [ 0.6 0.25 ]
      point[2]  [ 0.6 0.75 ]
      point[3]  [ 0 0.75 ]
      z [1.7 1.8]
   )
   #Workhat top
   block
   (
      color "gold"
      points 4
      point[0]  [ 0.05 0.30 ]
      point[1]  [ 0.5 0.3 ]
      point[2]  [ 0.5 0.7 ]
      point[3]  [ 0.05 0.7 ]
      z [1.8 1.9]
   )
   #eyes
   block
   (
      color "black"
      points 4
      point[0]  [ 0.50 0.35 ]
      point[1]  [ 0.55 0.35 ]
      point[2]  [ 0.55 0.40 ]
      point[3]  [ 0.50 0.4]
      z [1.55 1.6]
   )
  #eyes
   block
   (
      color "black"
      points 4
      point[0]  [ 0.50 0.60 ]
      point[1]  [ 0.55 0.6 ]
      point[2]  [ 0.55 0.65 ]
      point[3]  [ 0.50 0.65 ]
      z [1.55 1.6]
   ) 	
)

define bucket position
( 
  myLaser(pose [ 0.500 0.000 -0.400 0.000 ])
  drive "diff"
  size [1.000 1.000 1.000]
  color "firebrick"
  velocity_bounds [ -10 10 0 0 -360 360 -90 90 ]  
  block
  (
    points [4]
    point[0] [0 0]
    point[1] [0 1]
    point[2] [1 1]
    point[3] [1 0]
    z [0 1]
  )
)

define tractor position
(
  myLaser(pose [ 2.500 0.000 -2.500 0.000 ])
  #myLaser(pose [ 2.500 0.000 -1.000 0.000 ])
  drive "diff"
  size [5.000 3.000 3.000]
  velocity_bounds [ -10 10 0 0 -360 360 -90 90 ]	
   #grill	
   block 
   (  
      color "black"
      points 4
      point[0]  [ 0.9 0.25 ]
      point[1]  [ 0.9 0.75 ]
      point[2]  [ 0.92 0.75 ]
      point[3]  [ 0.92 0.25 ]
      z [0.25 0.55]
   )
   #base	
   block 
   (  
      color "red2"
      points 4
      point[0]  [ 0 0.2 ]
      point[1]  [ 0.9 0.2 ]
      point[2]  [ 0.9 0.8 ]
      point[3]  [ 0 0.8 ]
      z [0.2 0.6]
   )
   #seat back
   block 
   (  
      color "red"
      points 4
      point[0]  [ 0.25 0.32 ]
      point[1]  [ 0.3 0.32 ]
      point[2]  [ 0.3 0.68 ]
      point[3]  [ 0.25 0.68 ]
      z [0.6 0.82]
   )
   #body	
   block 
   (  
      color "ForestGreen"
      points 4
      point[0]  [ 0.3 0.4 ]
      point[1]  [ 0.4 0.4 ]
      point[2]  [ 0.4 0.6 ]
      point[3]  [ 0.3 0.6 ]
      z [0.6 0.8]
   )
   #head
   block
   (
      color "tan"
      points 4
      point[0]  [ 0.3 0.45 ]
      point[1]  [ 0.4 0.45 ]
      point[2]  [ 0.4 0.55 ]
      point[3]  [ 0.3 0.55 ]
      z [0.8 0.9]
   )
   #eye
   block
   (
      color "black"
      points 4
      point[0]  [ 0.4 0.46 ]
      point[1]  [ 0.41 0.46 ]
      point[2]  [ 0.41 0.48 ]
      point[3]  [ 0.4 0.48 ]
      z [0.85 0.87]
   )
   #eye
   block
   (
      color "black"
      points 4
      point[0]  [ 0.4 0.52 ]
      point[1]  [ 0.41 0.52 ]
      point[2]  [ 0.41 0.54 ]
      point[3]  [ 0.4 0.54 ]
      z [0.85 0.87]
   )
   #Workhat
   block
   (
      color "gold"
      points 4
      point[0]  [ 0.28 0.4 ]
      point[1]  [ 0.42 0.4 ]
      point[2]  [ 0.42 0.6 ]
      point[3]  [ 0.28 0.6 ]
      z [0.9 0.95]
   )
   #Workhat top
   block
   (
      color "gold"
      points 4
      point[0]  [ 0.3 0.45 ]
      point[1]  [ 0.4 0.45 ]
      point[2]  [ 0.4 0.55 ]
      point[3]  [ 0.3 0.55 ]
      z [0.95 1]
   )
   #arms	
   block 
   (  
      color "tan"
      points 4
      point[0]  [ 0.325 0.4 ]
      point[1]  [ 0.375 0.4 ]
      point[2]  [ 0.375 0.35 ]
      point[3]  [ 0.325 0.35 ]
      z [0.6 0.8]
   )
   #arms	
   block 
   (  
      color "tan"
      points 4
      point[0]  [ 0.325 0.6 ]
      point[1]  [ 0.375 0.6 ]
      point[2]  [ 0.375 0.65 ]
      point[3]  [ 0.325 0.65 ]
      z [0.6 0.8]
   )
   # large wheel back right
   block
   (
      color "black"
      points 4
      point[0]  [ 0.05 0.1 ]
      point[1]  [ 0.3 0.1 ]
      point[2]  [ 0.3 0.2 ]
      point[3]  [ 0.05 0.2 ]
      z [0 0.5]
   )
 # large wheel back left
   block
   (
      color "black"
      points 4
      point[0]  [ 0.05 0.9 ]
      point[1]  [ 0.3 0.9 ]
      point[2]  [ 0.3 0.8 ]
      point[3]  [ 0.05 0.8 ]
      z [0 0.5]
   )
 # small wheel front left
   block
   (
      color "black"
      points 4
      point[0]  [ 0.85 0.9 ]
      point[1]  [ 0.7 0.9 ]
      point[2]  [ 0.7 0.8 ]
      point[3]  [ 0.85 0.8 ]
      z [0 0.3]
   )
 # small wheel front right
   block
   (
      color "black"
      points 4
      point[0]  [ 0.7 0.1 ]
      point[1]  [ 0.85 0.1 ]
      point[2]  [ 0.85 0.2 ]
      point[3]  [ 0.7 0.2 ]
      z [0 0.3]
   )
)

define dog position
( 
  myLaser(pose [ 0.500 0.000 -0.400 0.000 ])
  drive "diff"
  size [1.5 0.500 0.700]
  velocity_bounds [ -10 10 0 0 -360 360 -90 90 ]	
   #body
   block 
   (
      color "grey"
      points 4
      point[0]  [ 0.2 0.15 ]
      point[1]  [ 0.75 0.15 ]
      point[2]  [ 0.75 0.65 ]
      point[3]  [ 0.2 0.65 ]
      z [0.2 0.55]
   )
   #legs
   block 
   (
      color "DarkGrey"
      points 4
      point[0]  [ 0.25 0.2 ]
      point[1]  [ 0.35 0.2 ]
      point[2]  [ 0.35 0.3 ]
      point[3]  [ 0.25 0.3 ]
      z [0 0.2]
   )
   #legs
   block 
   (
      color "LightGrey"
      points 4
      point[0]  [ 0.25 0.5 ]
      point[1]  [ 0.35 0.5 ]
      point[2]  [ 0.35 0.6 ]
      point[3]  [ 0.25 0.6 ]
      z [0 0.2]
   )
   #legs
   block 
   (
      color "Grey"
      points 4
      point[0]  [ 0.65 0.5 ]
      point[1]  [ 0.75 0.5 ]
      point[2]  [ 0.75 0.6 ]
      point[3]  [ 0.65 0.6 ]
      z [0 0.2]
   )
   #legs
   block 
   (
      color "DarkGrey"
      points 4
      point[0]  [ 0.65 0.2 ]
      point[1]  [ 0.75 0.2 ]
      point[2]  [ 0.75 0.3 ]
      point[3]  [ 0.65 0.3 ]
      z [0 0.2]
   )
  #head
   block 
   (
      color "DarkGrey"
      points 4
      point[0]  [ 0.75 0.20 ]
      point[1]  [ 0.9 0.20 ]
      point[2]  [ 0.9 0.60 ]
      point[3]  [ 0.75 0.60 ]
      z [0.4 0.65]
   )
  #nose
   block 
   (
      color "Grey"
      points 4
      point[0]  [ 0.9 0.25 ]
      point[1]  [ 0.95 0.25 ]
      point[2]  [ 0.95 0.55 ]
      point[3]  [ 0.9 0.55 ]
      z [0.45 0.55]
   )

  #ears
   block 
   (
      color "LightGrey"
      points 4
      point[0]  [ 0.80 0.22 ]
      point[1]  [ 0.85 0.22 ]
      point[2]  [ 0.85 0.35 ]
      point[3]  [ 0.80 0.35 ]
      z [0.65 0.7]
   )
  #ears
   block 
   (
      color "DarkGrey"
      points 4
      point[0]  [ 0.80 0.45 ]
      point[1]  [ 0.85 0.45 ]
      point[2]  [ 0.85 0.58 ]
      point[3]  [ 0.80 0.58 ]
      z [0.65 0.7]
   )

   #tail
   block 
   (
      color "Grey"
      points 4
      point[0]  [ 0.15 0.35 ]
      point[1]  [ 0.2 0.35 ]
      point[2]  [ 0.2 0.45 ]
      point[3]  [ 0.15 0.45 ]
      z [0.1 0.5]
   )
)

define cat position
( 
  myLaser(pose [ 0.500 0.000 -0.400 0.000 ])
  drive "diff"
  size [1.000 0.800 0.700]
  velocity_bounds [ -10 10 0 0 -360 360 -90 90 ]	
   #body
   block 
   (
      color "orange"
      points 4
      point[0]  [ 0.25 0 ]
      point[1]  [ 0.75 0 ]
      point[2]  [ 0.75 0.8 ]
      point[3]  [ 0.25 0.8 ]
      z [0.2 0.55]
   )
   #legs
   block 
   (
      color "DarkOrange"
      points 4
      point[0]  [ 0.25 0 ]
      point[1]  [ 0.35 0 ]
      point[2]  [ 0.35 0.1 ]
      point[3]  [ 0.25 0.1 ]
      z [0 0.2]
   )
   #legs
   block 
   (
      color "orange"
      points 4
      point[0]  [ 0.25 0.7 ]
      point[1]  [ 0.35 0.7 ]
      point[2]  [ 0.35 0.8 ]
      point[3]  [ 0.25 0.8 ]
      z [0 0.2]
   )
   #legs
   block 
   (
      color "orange"
      points 4
      point[0]  [ 0.65 0.7 ]
      point[1]  [ 0.75 0.7 ]
      point[2]  [ 0.75 0.8 ]
      point[3]  [ 0.65 0.8 ]
      z [0 0.2]
   )
   #legs
   block 
   (
      color "orange"
      points 4
      point[0]  [ 0.65 0 ]
      point[1]  [ 0.75 0 ]
      point[2]  [ 0.75 0.1 ]
      point[3]  [ 0.65 0.1 ]
      z [0 0.2]
   )
  #head
   block 
   (
      color "orange"
      points 4
      point[0]  [ 0.75 0.20 ]
      point[1]  [ 0.9 0.20 ]
      point[2]  [ 0.9 0.60 ]
      point[3]  [ 0.75 0.60 ]
      z [0.4 0.65]
   )
  #nose
   block 
   (
      color "DarkOrange"
      points 4
      point[0]  [ 0.9 0.25 ]
      point[1]  [ 1 0.25 ]
      point[2]  [ 1 0.55 ]
      point[3]  [ 0.9 0.55 ]
      z [0.45 0.55]
   )

  #ears
   block 
   (
      color "orange"
      points 4
      point[0]  [ 0.80 0.22 ]
      point[1]  [ 0.85 0.22 ]
      point[2]  [ 0.85 0.35 ]
      point[3]  [ 0.80 0.35 ]
      z [0.65 0.7]
   )

   #ears
   block 
   (
      color "DarkOrange"
      points 4
      point[0]  [ 0.80 0.45 ]
      point[1]  [ 0.85 0.45 ]
      point[2]  [ 0.85 0.58 ]
      point[3]  [ 0.80 0.58 ]
      z [0.65 0.7]
   )

   #tail tip
   block 
   (
      color "DarkOrange"
      points 4
      point[0]  [ 0.15 0.35 ]
      point[1]  [ 0.2 0.35 ]
      point[2]  [ 0.2 0.45 ]
      point[3]  [ 0.15 0.45 ]
      z [0.65 0.7]
   )

   #tail
   block 
   (
      color "orange"
      points 4
      point[0]  [ 0.2 0.35 ]
      point[1]  [ 0.25 0.35 ]
      point[2]  [ 0.25 0.45 ]
      point[3]  [ 0.2 0.45 ]
      z [0.4 0.7]
   )
)


