from tkinter import *
from time import sleep

# dummy data
#full_name = "John Doe"
#user_name = "jo851doe"
#token_id = "n1c3rf1d70k3n"

#speed = 68
#temp = 30
#st_angle = 12
#alt = 520

class GUI:
    def __init__(self):
        # initialize window
        global window
        window = Tk()
        window.title("Vehicle Interface")
        window.geometry("700x300")
        window.configure(background="white")

        # define left, middle, center and bottom frame
        left_frame = Frame(window, width=200, height=100, highlightbackground="black", highlightcolor="black", highlightthickness=10)
        middle_frame = Frame(window, width=100, height=100, padx=10, pady=10)
        right_frame = Frame(window, width=300, height=100, padx=10, pady=10)
        bottom_frame = Frame(window, width=50, height=50, padx=10, pady=10)

        # define frame structure and position (grid)
        left_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")
        middle_frame.grid(row=0, column=1, sticky="nsew")
        right_frame.grid(row=0, column=2, sticky="nsew")
        bottom_frame.grid(row=1, column=1, columnspan=2, sticky="nsew")
        # define left text frame
        global display
        display = Text(left_frame, height="20", width="25", font=("Roboto", 10), fg="white", bg="black")
        display.pack(side="top", anchor="nw", fill="y", expand=1)

        # empty frame for style purposes
        Label(right_frame, text="", font=("Roboto", 12)).pack(side="top", anchor="w")

        # define text frames with sensor data
        global speed_data
        speed_data = Text(right_frame, height="1", width="15", font=("Roboto", 12), spacing3=6)
        speed_data.pack(side="top", anchor="nw")
        speed_data.insert(END, "\n")

        global temp_data
        temp_data = Text(right_frame, height="1", width="15", font=("Roboto", 12), spacing3=6)
        temp_data.pack(side="top", anchor="nw")
        temp_data.insert(END, "\n")

        global steering_data
        steering_data = Text(right_frame, height="1", width="15", font=("Roboto", 12), spacing3=6)
        steering_data.pack(side="top", anchor="nw")
        steering_data.insert(END, "\n")

        global alt_data
        alt_data = Text(right_frame, height="1", width="15", font=("Roboto", 12), spacing3=6)
        alt_data.pack(side="top", anchor="nw")
        alt_data.insert(END, "\n")

        # define behaviour is window is streched
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(1, weight=1)

        # draw static labels
        Label(middle_frame, text="CURRENT STATE", font=("Roboto", 15)).pack(side="top", anchor="w")
        Label(middle_frame, text="Speed: ", font=("Roboto", 12)).pack(side="top", anchor="w")
        Label(middle_frame, text="Temperature: ", font=("Roboto", 12)).pack(side="top", anchor="w")
        Label(middle_frame, text="Steering Angle: ", font=("Roboto", 12)).pack(side="top", anchor="w")
        Label(middle_frame, text="Altitude: ", font=("Roboto", 12)).pack(side="top", anchor="w")

        # define logout button
        logout_button = Button(bottom_frame, text="Refresh", command=self.userLogout)
        logout_button.pack(side="bottom", anchor="se")

    # user login function for initial login text output on left label
    def userLogin(self, full_name, user_name, token_id):
        display.delete(1.0, END)
        display.insert(END, "Welcome " + full_name + "!\n\n")
        display.insert(END, "You successfully logged in.\n\n"
                            "Username: " + user_name + "\n"
                            "Token: " + token_id + "\n\n")
        display.insert(END, "Drive responsibly!\n")



    # loop for updating dynamic labels
    def updateData(self):
        filepath = 'data.txt'
        f = open(filepath, 'r')
        speed_data.delete(1.0, END)
        temp_data.delete(1.0, END)
        steering_data.delete(1.0, END)
        alt_data.delete(1.0, END)
        data = f.readlines()
        speed_data.insert(END, str(data[0]) + " km/h\n")
        temp_data.insert(END, str(data[1]) + " C\n")
        steering_data.insert(END, str(data[2]) + "\n")
        alt_data.insert(END, str(data[3]) + " m\n")


    def userLogout(self):
        self.updateData()
        
        
    def loop_forever(self):
        window.mainloop()


# call userLogin on user login event
#userLogin(full_name, user_name, token_id)

# call if user logs out
# userLogout()

# update dynamic labels
#updateData(speed, temp, st_angle, alt)

gui = GUI()
gui.userLogin("Bernd Schneider", "Berndi", "geilesToken")

gui.updateData()
gui.loop_forever()

