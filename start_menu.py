from tkinter import *

def rules(canvas):
    canvas.delete("text")
    canvas.delete("button")

    canvas.create_text(500, 125, text="You shoot the other guy till they die!", tags="text")
    back_button = Button(canvas, text="Go back!", command=lambda: start(canvas))
    
    canvas.create_window(450,255,width=90,height=35, anchor='nw', window=back_button, tags="button")

def play(canvas):
    canvas.delete("text")
    canvas.delete("button")

    #GO MAKE THE MAP
    map = Canvas(canvas, width=1000, height=900, highlightthickness=0,)
    map.create_rectangle(0,0,1000,900, fill="pink")
    canvas.create_window(0,100,width=1000,height=900, anchor='nw', window=map, tags="map")

    canvas.create_text(250, 10, text="Player:", tags="text")
    canvas.create_text(750, 10, text="Puter:", tags="text")


def start(canvas):
    canvas.delete("text")
    canvas.delete("button")

    canvas.create_text(500, 125, text="Welcome to Maze Fight!", tags="text")

    play_button = Button(canvas, text="Play!", command=lambda: play(canvas))
    rules_button = Button(canvas, text="Rules!", command=lambda: rules(canvas))

    canvas.create_window(450,255,width=90,height=35, anchor='nw', window=play_button, tags="button")
    canvas.create_window(450,300,width=90,height=35, anchor='nw', window=rules_button, tags="button")

window = Tk()
window.title("Maze Fight")
window.geometry("1000x1000")
window.minsize(300,300)
frame=Frame(window)
frame.place(x=0,y=0,width=800,height=1000)
#label isa thing with text in them
canvas = Canvas(window, width=1000, height=1000, highlightthickness=0)
canvas.place(x=0, y=0)
start(canvas)

window.mainloop()