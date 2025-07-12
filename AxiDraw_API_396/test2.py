from pyaxidraw import axidraw
ad = axidraw.AxiDraw()
ad.plot_setup("robo_kavi_box_with_footer_vectorized.svg")
ad.options.pen_pos_down = 30      # adjust as needed
ad.options.pen_pos_down = 30      # adjust as needed
ad.options.pen_pos_up = 70        # adjust as needed
ad.options.speed_pendown = 25     # plotting speed
ad.options.speed_penup = 75       # pen-up travel speed
ad.options.accel = 15
ad.options.model = 2              # most recent models
ad.options.units = 1              # SVG units (mm)          # SVG units (mm)
ad.plot_run()
ad.options.const_speed = False
ad.options.mode = "plot" # Ensure it's in standard plotting mode
ad.options.page_size = "custom" # Important if your SVG defines its own custom size
ad.options.x_offset = 0.0 # No offset
ad.options.y_offset = 0.0 # No offset
ad.options.rotate = 0.0 # No rotation
