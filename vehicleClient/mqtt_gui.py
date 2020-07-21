from tkinter import *

# dummy data
full_name = "Voller Name"
user_name = "Cooler Username"
token_id = "nasf8ouojfj"

speed = 68
temp = 30
st_angle = 12
alt = 520

def initGUI():
    # initialize window
    global window
    window = Tk()
    window.title("MQTT Broker")
    window.geometry("750x300")
    window.configure(background="white")

    #################
    # define frames
    #################

    # left, middle, center
    left_frame = Frame(window, width=200, height=100, highlightbackground="black", highlightcolor="black", highlightthickness=10)
    middle_frame = Frame(window, width=100, height=100, padx=10, pady=10)
    right_frame = Frame(window, width=300, height=100, padx=10, pady=10)
    bottom_frame = Frame(window, width=50, height=50, padx=10, pady=10)

    # define frame structure and position (grid)
    left_frame.grid(row=0, column=0, sticky="nsew")
    middle_frame.grid(row=0, column=1, sticky="nsew")
    right_frame.grid(row=0, column=2, sticky="nsew")
    bottom_frame.grid(row=0, column=3, columnspan="2", sticky="nsew")

    # define left text frame
    global display
    display = Text(left_frame, height="20", width="40", font=("Roboto", 10), fg="white", bg="black", )
    display.pack(side="top", anchor="nw", fill="y", expand=1)

    # define text frame with sensor data
    global display_data
    display_data = Text(right_frame, height="6", width="15", font=("Roboto", 12), spacing3=6)
    display_data.pack(side="top", anchor="nw", padx=5, pady=5)
    display_data.insert(END, "\n")

    # define behaviour is window is streched
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)

    # draw static labels
    Label(middle_frame, text="CURRENT VALUES", font=("Roboto", 15)).pack(side="top", anchor="w")
    drawSensorLabel(middle_frame, "Speed: ")
    drawSensorLabel(middle_frame, "Temperature: ")
    drawSensorLabel(middle_frame, "Steering Angle: ")
    drawSensorLabel(middle_frame, "Altitude: ")

    # define logout button
    logout_button = Button(bottom_frame, text="Logout", command=userLogout)
    logout_button.pack(side="bottom", anchor="se")

# function for drawing labels
def drawSensorLabel(frame, param):
    Label(frame, text=param, font=("Roboto", 12)).pack(side="top", anchor="w")

# user login function for initial login text output on left label
def userLogin(full_name, user_name, token_id):
    display.delete(1.0, END)
    display.insert(END, "Welcome " + full_name + "!\n\n")
    display.insert(END, "You successfully logged in.\n"
                        "Username: " + user_name + "\n"
                        "Token: " + token_id + "\n\n")
    display.insert(END, "Drive responsibly!\n")

def userLogout():
    display.delete(1.0, END)
    display.insert(END, "Bye Bye!\n")

# loop for updating dynamic labels
def updateData(speed, temp, st_angle, alt):
    display_data.delete(1.0, END)
    display_data.insert(END, "\n")
    display_data.insert(END, str(speed) + " km/h\n")
    display_data.insert(END, str(temp) + " °C\n")
    display_data.insert(END, str(st_angle) + "°\n")
    display_data.insert(END, str(alt) + " m\n")

#initialize GUI
initGUI()

# call userLogin on user login event
userLogin(full_name, user_name, token_id)

# call if user logs out
# userLogout()

# update dynamic labels
updateData(speed, temp, st_angle, alt)

window.mainloop()
