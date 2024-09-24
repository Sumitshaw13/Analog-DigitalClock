# Resizable Analog and Digital Clock

This project is a resizable Analog and Digital Clock with customizable timezones, background colors, and an optional AM/PM format. It is built using Python with Tkinter and PyQt5 for the graphical interface and features multi-timezone support using the pytz library.

# Features
- **Analog Clock**: Displays an animated, real-time analog clock.
- **Digital Clock**: Displays a digital clock with options to toggle between 24-hour and 12-hour AM/PM formats.
- **Multi-timezone Support**: Choose from several predefined timezones (e.g., Asia/Kolkata, America/New_York).
- **Changeable Background Color**: Users can select a background color of their choice for the clock interface.
- **Resizable Window**: The clock dynamically adjusts to the window size.
- **Day Display**: Shows the current day of the week.
## Prerequisites
- **Python 3.x**
- **Tkinter (Usually included with Python)**
- **PyQt5 (pip install PyQt5)**
- **pytz for timezone support (pip install pytz)**
Installation
Clone the repository or download the Python script.
1) Install the required libraries by running:
   ```bash

   pip install PyQt5 pytz
2) Run the script:
   ```bash

    python Analog_Digital_Clock.py
## How to Use

- **Select a Timezone**:  
  Use the dropdown menu to select the timezone for which you want to display the time.

- **Toggle AM/PM Format**:  
  Check the "Display AM/PM" checkbox to switch between 24-hour and 12-hour formats.

- **Change Background Color**:  
  Click on the "Change Background Color" button to choose a custom background color for the clock.

- **Resizable Window**:  
  You can resize the window, and the clock will automatically adjust its dimensions accordingly.

## Code Overview

### Key Components:

- **Analog Clock**:  
  Utilizes Canvas to draw the clock face, numbers, and hands. The hands update every second using the `after()` method.

- **Digital Clock**:  
  Displays the current time in the selected format below the clock face.

- **Timezone and AM/PM Selector**:  
  Dropdown for timezone selection and a checkbox for AM/PM format toggling.

- **Background Color Picker**:  
  Button to open a color chooser dialog and apply the selected color to the background.

### Main Libraries:

- **Tkinter**: For building the GUI.
- **pytz**: For managing and displaying time in different timezones.
- **PyQt5**: To create a resizable window for the clock.

## Project Structure

- `resizable_clock.py`: The main Python script that contains all the functionality of the clock.

## Future Enhancements

- Add more timezones to the dropdown menu.
- Save user preferences (timezone, AM/PM format, background color) across sessions.
- Add customization for the clock face (numbers, colors, etc.).
