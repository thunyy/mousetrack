from graphics import Canvas
import time

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
DELAY = 0.01

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    while True:
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        
        in_bound = (0 <= mouse_x < CANVAS_WIDTH - CIRCLE_SIZE) and (0 <= mouse_y < CANVAS_HEIGHT - CIRCLE_SIZE)
        

        if in_bound:
            # Draw the circle at the mouse position
            ball = canvas.create_oval(mouse_x, mouse_y, mouse_x + CIRCLE_SIZE, mouse_y + CIRCLE_SIZE, 'blue')
        
        # Delay
        time.sleep(DELAY)
        


if __name__ == "__main__":
    main()
