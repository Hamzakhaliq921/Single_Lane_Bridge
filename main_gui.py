import tkinter as tk
from tkinter import ttk
import threading
import time
import random
from bridge_controller import BridgeController

class BridgeSimApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Single Lane Bridge Simulation")
        self.root.geometry("700x550")

        # Canvas
        self.canvas = tk.Canvas(self.root, bg="lightblue", height=320)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Controls
        control_frame = ttk.Frame(self.root)
        control_frame.pack(pady=5)

        ttk.Label(control_frame, text="North Farmers:").grid(row=0, column=0)
        self.north_spin = ttk.Spinbox(control_frame, from_=1, to=10, width=5)
        self.north_spin.set(4)
        self.north_spin.grid(row=0, column=1)

        ttk.Label(control_frame, text="South Farmers:").grid(row=0, column=2)
        self.south_spin = ttk.Spinbox(control_frame, from_=1, to=10, width=5)
        self.south_spin.set(4)
        self.south_spin.grid(row=0, column=3)

        ttk.Label(control_frame, text="Starvation Limit:").grid(row=0, column=4)
        self.starve_spin = ttk.Spinbox(control_frame, from_=1, to=10, width=5)
        self.starve_spin.set(3)
        self.starve_spin.grid(row=0, column=5)

        # Start, Reset, Pause/Resume Buttons
        self.start_button = ttk.Button(control_frame, text="Start Simulation", command=self.start_simulation)
        self.start_button.grid(row=0, column=6, padx=10)

        self.reset_button = ttk.Button(control_frame, text="Reset", command=self.reset_simulation)
        self.reset_button.grid(row=0, column=7)

        self.pause_button = ttk.Button(control_frame, text="Pause", command=self.toggle_pause)
        self.pause_button.grid(row=0, column=8)

        # Speed Slider
        ttk.Label(control_frame, text="Speed:").grid(row=0, column=9)
        self.speed_var = tk.DoubleVar(value=1.0)
        self.speed_slider = ttk.Scale(control_frame, from_=0.1, to=2.0, variable=self.speed_var, length=100)
        self.speed_slider.grid(row=0, column=10)

        # Log Console
        self.log_box = tk.Text(self.root, height=7, state="disabled", bg="#f8f8f8")
        self.log_box.pack(fill=tk.X, padx=10)

        # App State
        self.farmers = []
        self.is_paused = False

    def log(self, msg):
        self.log_box.config(state="normal")
        self.log_box.insert(tk.END, msg + "\n")
        self.log_box.see(tk.END)
        self.log_box.config(state="disabled")

    def reset_simulation(self):
        self.canvas.delete("all")
        self.log_box.config(state="normal")
        self.log_box.delete(1.0, tk.END)
        self.log_box.config(state="disabled")

    def toggle_pause(self):
        self.is_paused = not self.is_paused
        self.pause_button.config(text="Resume" if self.is_paused else "Pause")

    def draw_bridge(self):
        self.canvas.create_rectangle(240, 100, 360, 220, fill="#808080", outline="black", width=2)
        self.canvas.create_text(300, 160, text="🛤️ BRIDGE 🛤️", font=("Helvetica", 11, "bold"))

    def add_farmer(self, x, y, color, text):
        circle = self.canvas.create_oval(x, y, x+20, y+20, fill=color)
        label = self.canvas.create_text(x+10, y+30, text=text, font=("Arial", 8))
        return circle, label

    def set_farmer_color(self, farmer_id, color):
        self.canvas.itemconfig(farmer_id, fill=color)
        self.canvas.update()

    def move_farmer(self, canvas_id, from_x, to_x):
        dx = 5 if to_x > from_x else -5
        steps = abs(to_x - from_x) // abs(dx)
        for _ in range(steps):
            while self.is_paused:
                self.canvas.update()
                time.sleep(0.05)

            self.canvas.move(canvas_id, dx, 0)
            self.canvas.update()
            time.sleep(0.03 / self.speed_var.get())

    def start_simulation(self):
        self.canvas.delete("all")
        self.draw_bridge()
        self.farmers = []
        self.is_paused = False
        self.pause_button.config(text="Pause")

        north = int(self.north_spin.get())
        south = int(self.south_spin.get())
        limit = int(self.starve_spin.get())

        controller = BridgeController(limit)

        for i in range(north):
            y = 20 + i * 25
            farmer_id = i + 1
            farmer, label = self.add_farmer(10, y, "blue", f"N{farmer_id}")
            t = threading.Thread(target=self.farmer_gui_routine,
                                 args=(farmer_id, True, controller, farmer, 10, 280))
            t.daemon = True
            t.start()

        for i in range(south):
            y = 20 + i * 25
            farmer_id = north + i + 1
            farmer, label = self.add_farmer(570, y, "red", f"S{farmer_id}")
            t = threading.Thread(target=self.farmer_gui_routine,
                                 args=(farmer_id, False, controller, farmer, 570, 320))
            t.daemon = True
            t.start()

    def farmer_gui_routine(self, farmer_id, is_north, controller, canvas_id, start_x, bridge_x):
        direction = "NORTH" if is_north else "SOUTH"
        self.log(f"[Farmer {farmer_id}] Appeared ({direction})")
        self.set_farmer_color(canvas_id, "yellow")

        if is_north:
            controller.enter_north(farmer_id)
        else:
            controller.enter_south(farmer_id)

        self.log(f"[Farmer {farmer_id}] Entering bridge ({direction})")
        self.set_farmer_color(canvas_id, "green")
        self.move_farmer(canvas_id, start_x, bridge_x)

        time.sleep(random.randint(2, 4))  # Simulate time on bridge

        self.log(f"[Farmer {farmer_id}] Exiting bridge ({direction})")
        self.set_farmer_color(canvas_id, "gray")
        exit_x = 570 if is_north else 10
        self.move_farmer(canvas_id, bridge_x, exit_x)

        if is_north:
            controller.exit_north(farmer_id)
        else:
            controller.exit_south(farmer_id)

        self.log(f"[Farmer {farmer_id}] Finished crossing.")

# Run it
if __name__ == "__main__":
    root = tk.Tk()
    app = BridgeSimApp(root)
    root.mainloop()

