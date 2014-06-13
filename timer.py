import tkinter as tk
import time, string, turtle, math

class Set_window(tk.Frame):
    def __init__(self, master=None):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.time = 0

        self.make_label()
        self.make_entry()
        self.make_button()
        self.frame.pack()

    def make_label(self):
        self.label = tk.Label(self.frame, font=("Arial",20), text="Minutes")
        self.label2 = tk.Label(self.frame, font=("Arial",20), text="Seconds")

        self.label.grid(row=0)
        self.label2.grid(row=1)

    def make_entry(self):
            vcmd = (self.master.register(self.validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
            self.entry = tk.Entry(self.frame, width=10, font=("Arial",20), validate="key", validatecommand=vcmd)
            self.entry2 = tk.Entry(self.frame, width=10, font=("Arial",20), validate="key", validatecommand=vcmd)

            self.entry.grid(row=0, column=1)
            self.entry2.grid(row=1, column=1)

    def validate(self, d, i, P, s, S, v, V, W):
        return S in string.digits

    def make_button(self):
        self.button = tk.Button(self.frame, text="Start", width=15, font=("Arial",20), command=self.open_main)
        self.button2 = tk.Button(self.frame, text="Stop", width=15, font=("Arial",20), command=self.close_timer)

        self.button.grid(row=2)
        self.button2.grid(row=2, column=1)

    def open_main(self):
        self.calculate_time()

        self.new_window = tk.Toplevel(self.master)
        self.new_window.configure(bg="orange")
        self.app = Main_window(self.time, self.new_window)

    def calculate_time(self):
        minutes = int(self.entry.get() if self.entry.get() != "" else 0)
        seconds = int(self.entry2.get() if self.entry2.get() != "" else 0)
        
        self.time = (minutes * 60) + seconds

    def close_timer(self):
            try:
                self.new_window.destroy()
            except AttributeError:
                pass

class Main_window(tk.Frame):
    def __init__(self, time_to_count, master=None):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.time_to_count = time_to_count

        self.time = int(time.time())
        self.calculate_end_time()
        self.update_timer()
        self.make_label()
        self.make_canvas()
        self.make_turtle()
        self.update()

    def make_label(self):
        self.label = tk.Label(self.frame, font=("Arial",30), text=self.minutes)
        self.label2 = tk.Label(self.frame, font=("Arial",30), text=":")
        self.label3 = tk.Label(self.frame, font=("Arial",30), text=self.seconds)
        self.label4 = tk.Label(self.frame, font=("Arial",30), text="Minutes")
        self.label5 = tk.Label(self.frame, font=("Arial",30), text="Seconds")

        self.label.grid(row=0)
        self.label2.grid(row=0, column=1)
        self.label3.grid(row=0, column=2)
        self.label4.grid(row=1, column=0)
        self.label5.grid(row=1, column=2)

    def make_canvas(self):
        self.canvas = tk.Canvas(self.frame, width=500, height=500)
        self.canvas.grid(row=2, columnspan=3)

    def make_turtle(self):
        self.turtle = turtle.RawTurtle(self.canvas)
        self.turtle.screen.bgcolor("orange")
        self.turtle.fillcolor("red")

        self.turtle.hideturtle()
        self.turtle.up()
        self.turtle.shape("turtle")
        self.turtle.goto(0, 200)
        self.turtle.showturtle()
        self.turtle.down()
        self.turtle.begin_fill()

        self.degrees_per_step = 360 / self.time_to_count

    def update_timer(self):
        self.time = int(time.time())
        self.time_left = self.end_time - self.time

        self.minutes = int(self.time_left / 60)
        self.seconds = self.time_left % 60

    def calculate_end_time(self):
        self.end_time = self.time + self.time_to_count

    def update_text(self):
        self.label.config(text=self.minutes)
        self.label3.config(text=self.seconds)

    def update_turtle(self):
        angle = self.degrees_per_step * self.time_left
        x = -math.sin(math.radians(angle)) * 200
        y = math.cos(math.radians(angle)) * 200
        
        self.turtle.goto(x, y)
        self.turtle.setheading(angle)

    def update(self):
        if self.time_left > 0:
            self.update_timer()
        else:
            self.turtle.end_fill()
        self.update_text()
        self.update_turtle()
        self.master.after(100, self.update)

def main():
    root = tk.Tk()
    root.wm_title("Turtle Timer")
    app = Set_window(root)
    root.mainloop()

if __name__ == "__main__":
    main()
