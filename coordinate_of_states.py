import turtle

BACKGROUND_IMAGE = "IndiaMap.gif"

screen = turtle.Screen()
screen.addshape(BACKGROUND_IMAGE)
screen.title("Guess the Indian State")

turtle.shape(BACKGROUND_IMAGE)

def get_mouse_click_coordinates(x, y):
    print(x, y)

turtle.onscreenclick(fun= get_mouse_click_coordinates)

turtle.mainloop()