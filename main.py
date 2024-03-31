from tkinter import *
from routing_zoning_algorithm import RoutingZoningAlgorithm


def get_routes():
    output = "Vehicle Routes:\n\n"
    routes_output = routes.output
    for i, route in enumerate(routes_output):
        output += f"{i+1}. {route}\n"
    canvas.itemconfig(text, text=f"{output}")


window = Tk()
routes = RoutingZoningAlgorithm()
window.title("Routing-Zoning Application")
window.config(padx=50, pady=50)


# Canvas
canvas = Canvas(width=300, height=414, background="grey")
text = canvas.create_text(150, 207, text="Vehicle routes goes here...",
                          width=250, fill="black", font=("Arial", 20, "bold"))
canvas.grid(column=0, row=0)

car_image = PhotoImage(file='true.png')
button = Button(highlightthickness=0, image=car_image, command=get_routes)
button.grid(row=1, column=0)

window.mainloop()
