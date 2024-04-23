import tkinter as tk

class Ball:
    def __init__(self, canvas, color, size, x_speed, y_speed):
        self.canvas = canvas
        self.id = canvas.create_oval(0, 0, size, size, fill=color)
        self.canvas.move(self.id, 200, 200)
        self.x_speed = x_speed
        self.y_speed = y_speed

    def move(self):
        self.canvas.move(self.id, self.x_speed, self.y_speed)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 or pos[2] >= self.canvas.winfo_width():
            self.x_speed = -self.x_speed
        if pos[1] <= 0 or pos[3] >= self.canvas.winfo_height():
            self.y_speed = -self.y_speed

def update():
    ball.move()
    root.after(10, update)

root = tk.Tk()
root.title("Bouncing Ball Animation")

canvas = tk.Canvas(root, width=400, height=700)
canvas.pack()

ball = Ball(canvas, "red", 30, 2, 2)

root.after(10, update)  # Start the animation loop
root.mainloop()
