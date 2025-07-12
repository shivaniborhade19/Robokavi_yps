from pyaxidraw import axidraw


def plot_svg(svg_path):
    try:
        print("🖨️ Plotting:", svg_path)

        ad = axidraw.AxiDraw()
        ad.plot_setup(svg_path)

        # AxiDraw speed/settings
        ad.options.pen_pos_up = 75
        ad.options.speed_pendown = 35
        ad.options.speed_penup = 80
        ad.options.accel = 15
        ad.options.model = 2
        ad.options.units = 1
        ad.options.const_speed = False
        
        ad.plot_run()
        ad.options.mode = "plot" # Ensure it's in standard plotting mode
        ad.options.page_size = "custom" # Important if your SVG defines its own custom size
        ad.options.x_offset = 0.0 # No offset
        ad.options.y_offset = 0.0 # No offset
        ad.options.rotate = 0.0 # No rotation

        print("✅ Plotting complete.")
    except Exception as e:
        print("❌ Plotting failed:", str(e))
