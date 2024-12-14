import tkinter as tk
from tkinter import ttk

def main():
    app = Application()
    app.mainloop()
    

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Class App")
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        
        frame = InputForm(self)
        frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        frame2 = InputForm(self)
        frame2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
       
        
        

    

class InputForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.entry = ttk.Entry(self)
        self.entry.grid(row=0, column=0, sticky="ew")

        self.entry.bind("<Return>", self.add_to_listbox)

        self.entry_btn = ttk.Button(self, text="Add", command=self.add_to_listbox)
        self.entry_btn.grid(row=0, column=1)
        
        self.entry_btn2 = ttk.Button(self, text="Clear", command=self.clear_listbox)
        self.entry_btn2.grid(row=0, column=2)

        self.text_listbox = tk.Listbox(self)
        self.text_listbox.grid(row=1, column=0, columnspan=3, sticky="nsew")
        
    def add_to_listbox(self, event=None):
        text = self.entry.get()
        if text:
            # Insert at the end if there is text
            self.text_listbox.insert(tk.END, text)
            self.entry.delete(0, tk.END)
            
    def clear_listbox(self):
        self.text_listbox.delete(0, tk.END)
        
if __name__ == "__main__":
    main()
    
#Using classes with tkinter
#root = tk.Tk()
#root.title("Simple Class App")
#root.mainloop()


    