define person model
(

  drive "diff"
  obstacle_return 0
  block
  (
  size [1 1.75 3.75]
    color "SkyBlue"
    points [4]
    point[0] [0 0]
    point[1] [0 1]
    point[2] [1 1]
    point[3] [1 0]
    z [0 1.5]
  )
  block
  (
  size [1 1.75 3.75]
    color "black"
    points [4]
    point[0] [1 0]
    point[1] [1 1]
    point[2] [2 0]
    point[3] [2 1]
    z [0 1.5]
  )
  block
  (
  size  [1 1.75 3.75]
    color "SkyBlue"
    points [4]
    point[0] [0 1]
    point[1] [0 2]
    point[2] [1 1]
    point[3] [1 2]
    z [0 1.5]
  )
  block
  (
  size  [1 1.75 3.75]
    color "black"
    points [4]
    point[0] [1 1]
    point[1] [1 2]
    point[2] [2 1]
    point[3] [2 2]
    z [0 1.5]
  )
 
  
)