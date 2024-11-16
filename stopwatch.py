import tkinter as tk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.update_time = 0
        
        # Label to display the time
        self.time_display = tk.Label(root, text="00:00:00", font=("Arial", 30), width=10, height=2)
        self.time_display.grid(row=0, column=0, padx=20, pady=20)
        
        # Start button
        self.start_button = tk.Button(root, text="Start", font=("Arial", 15), width=10, command=self.start_stop)
        self.start_button.grid(row=1, column=0, padx=5, pady=5)
        
        # Reset button
        self.reset_button = tk.Button(root, text="Reset", font=("Arial", 15), width=10, command=self.reset)
        self.reset_button.grid(row=2, column=0, padx=5, pady=5)
        
        self.update_timer()

    def start_stop(self):
        if self.running:
            self.running = False
            self.start_button.config(text="Start")
        else:
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            self.start_button.config(text="Pause")
            self.update_timer()

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.start_time = 0
        self.start_button.config(text="Start")
        self.update_display(0)
        
    def update_timer(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.update_display(self.elapsed_time)
            self.root.after(10, self.update_timer)
        elif self.start_time > 0:
            self.update_display(self.elapsed_time)
        
    def update_display(self, elapsed_time):
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        milliseconds = int((elapsed_time * 100) % 100)
        time_str = f"{minutes:02}:{seconds:02}:{milliseconds:02}"
        self.time_display.config(text=time_str)

# Create the main window
root = tk.Tk()

# Create the stopwatch app
stopwatch_app = Stopwatch(root)

# Start the GUI event loop
root.mainloop()
