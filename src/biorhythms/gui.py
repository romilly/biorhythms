# Shamelessly adapated from https://github.com/lawsie/guizero/issues/351
# Thanks, Laura!
from datetime import datetime

from guizero import App, TextBox, PushButton, Text
import tkinter as tk
import matplotlib

from src.biorhythms.calculator import rhythm_data

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def plot():
    birth_date = datetime.strptime(text_box.value, '%d/%m/%Y')
    start_date = datetime.now()
    data = rhythm_data(birth_date, start_date)
    # Example of altering the plot based on what you typed
    a.plot(data)
    canvas.draw()


# guizero stuff
app = App()
help = Text(app, 'enter birth date as DD/MM/YYYY')
message = Text(app, '')
text_box = TextBox(app)

plot_button = PushButton(app, text = 'plot biorhythms', command = plot)

# Matplotlib stuff (example)
f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111)

#a.plot(x, y)

# Make a special tkinter canvas that works with matplotlib,
# and add it to app.tk (i.e. the tk widget hidden inside the guizero App)
canvas = FigureCanvasTkAgg(f, app.tk)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Enter the infinite display loop (this has to come after creating the plot)
app.display()