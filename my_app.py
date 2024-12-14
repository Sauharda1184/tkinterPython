import tkinter as tk

root = tk.Tk()
root.title("MY APP")

def on_button_click():
    #print("Button Clicked")
    lbl.config(text="Button Clicked")

lbl = tk.Label(root, text = "Label 1")
lbl.grid(row=0, column=0)

print(lbl.config().keys())

btn = tk.Button(root, text = "Button 1", command=on_button_click)
btn.grid(row=0, column=1)


root.mainloop()
