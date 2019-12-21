define bigbob position
(
      size [0.5 0.5 0.5]

      # the shape of Bigbob

      block
      (
            points 6
            point[5] [0 0]
            point[4] [0 1]
            point[3] [0.75 1]
            point[2] [1 0.75]
            point[1] [1 0.25]
            point[0] [0.75 0]
            z [0 1]
      )



      bigbobs_sonars_lf()
      bigbobs_sonars_lr()
      bigbobs_sonars_f()

)

define bigbobs_sonar sensor
(
    # define the size of each transducer [xsize ysize zsize] in meters
    size [0.01 0.05 0.01 ]
    # define the range bounds [min max]
    range [0.1 1.0]
    # define the angular field of view in degrees
    fov 20
    # define the color that ranges are drawn in the gui
    color_rgba [ 0 1 0 1 ]
)

define bigbobs_sonars_lf ranger
(
  bigbobs_sonar( pose [ 0.5 0.25 0 90]) # left side

)

define bigbobs_sonars_lr ranger
(
  bigbobs_sonar( pose [ 0 0.25 0 90]) # front

)

define bigbobs_sonars_f ranger
(
  bigbobs_sonar( pose [ 0.5 0.2 0 30]) # front

)
