import sys
from PyQt5.QtWidgets import QApplication, QWidget
import tkinter as tk
from datetime import datetime
import math
import pytz
import tkinter.colorchooser as colorchooser

class ResizableClock(QWidget):
    def __init__(self):
        super().__init__()

        # Clock
        self.window = tk.Tk()
        self.window.title("Analog and Digital Clock -- By Pro-operators")

        self.timezone_var = tk.StringVar()
        self.timezones = ["Asia/Kolkata", "America/New_York", "Europe/London", "Australia/Sydney", "Asia/Tokyo", "Africa/Cairo"]
        self.timezone_var.set("Asia/Kolkata")

        timezone_label = tk.Label(self.window, text="Select Time Zone:")
        timezone_label.pack()
        timezone_dropdown = tk.OptionMenu(self.window, self.timezone_var, *self.timezones)
        timezone_dropdown.pack()

        self.am_pm_var = tk.IntVar()
        self.am_pm_var.set(0)

        am_pm_check = tk.Checkbutton(self.window, text="Display AM/PM", variable=self.am_pm_var)
        am_pm_check.pack()

        self.background_color = "lightslateblue"  # Default background color

        color_button = tk.Button(self.window, text="Change Background Color", command=self.change_background_color)
        color_button.pack()

        self.canvas = tk.Canvas(self.window, bg=self.background_color)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.digital_time_label = tk.Label(self.window, text="", font=("Helvetica", 16), fg="white", bg="black")
        self.digital_time_label.pack()

        self.update_clock()

    def change_background_color(self):
        color, _ = colorchooser.askcolor(title="Choose Background Color")
        if color:
            # Convert RGB to hexadecimal format
            hex_color = '#{:02x}{:02x}{:02x}'.format(int(color[0]), int(color[1]), int(color[2]))
            self.background_color = hex_color
            self.canvas.configure(bg=self.background_color)

    def update_clock(self):
        self.canvas.delete("all")

        selected_timezone = self.timezone_var.get()
        tz = pytz.timezone(selected_timezone)
        current_time = datetime.now(tz)
        if self.am_pm_var.get():
            current_time_str = current_time.strftime("%I:%M:%S %p")
        else:
            current_time_str = current_time.strftime("%H:%M:%S")
        current_day_str = current_time.strftime("%A")

        self.digital_time_label.config(text=current_time_str)

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        # Draw clock face
        clock_size = min(canvas_width, canvas_height)
        self.canvas.create_oval(
            (canvas_width - clock_size) / 2,
            (canvas_height - clock_size) / 2,
            (canvas_width + clock_size) / 2,
            (canvas_height + clock_size) / 2,
            fill="white", outline="black", width=5
        )

        # Draw numbers on the clock face
        for i in range(1, 13):
            angle = math.radians(360 / 12 * i)
            x = (canvas_width / 2) + (clock_size / 2 - 20) * math.sin(angle)
            y = (canvas_height / 2) - (clock_size / 2 - 20) * math.cos(angle)
            self.canvas.create_text(x, y, text=str(i), font=("Helvetica", 12), fill="blue")

        self.canvas.create_text(canvas_width / 2, canvas_height - 100, text=current_day_str, font=("Helvetica", 15), fill="navy")

        # Draw clock hands
        second = current_time.second
        minute = current_time.minute
        hour = current_time.hour

        second_angle = math.radians(6 * second)
        minute_angle = math.radians(6 * (minute + second / 60))
        hour_angle = math.radians(30 * (hour + minute / 60))

        # Second hand
        self.canvas.create_line(
            canvas_width / 2, canvas_height / 2,
            canvas_width / 2 + (clock_size / 2 - 30) * math.sin(second_angle),
            canvas_height / 2 - (clock_size / 2 - 30) * math.cos(second_angle),
            fill="red", width=2
        )

        # Minute hand
        self.canvas.create_line(
            canvas_width / 2, canvas_height / 2,
            canvas_width / 2 + (clock_size / 2 - 40) * math.sin(minute_angle),
            canvas_height / 2 - (clock_size / 2 - 40) * math.cos(minute_angle),
            fill="blue", width=4
        )

        # Hour hand (shorter)
        self.canvas.create_line(
            canvas_width / 2, canvas_height / 2,
            canvas_width / 2 + (clock_size / 2 - 60) * math.sin(hour_angle),
            canvas_height / 2 - (clock_size / 2 - 70) * math.cos(hour_angle),
            fill="green", width=6
        )

        self.window.after(1000, self.update_clock)

    def run(self):
        self.window.mainloop()

def main():
    app = QApplication(sys.argv)
    resizable_clock = ResizableClock()
    resizable_clock.run()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()