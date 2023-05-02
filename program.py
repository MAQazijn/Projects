import tkinter as tk

class MyApp:
    def __init__(self, master):
        self.master = master
        master.title("Witaj!")

        self.label = tk.Label(master, text="Podaj swoje imię:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="OK", command=self.greet)
        self.button.pack()

    def greet(self):
        self.master.withdraw()
        name = self.entry.get()
        new_window = tk.Toplevel(self.master)
        greeting = f"Witaj, {name}!"
        self.app = Greeting(new_window, greeting)

class Greeting:
    def __init__(self, master, greeting):
        self.master = master
        master.title("Witaj!")
        self.label = tk.Label(master, text=greeting)
        self.label.pack()
        self.close_button = tk.Button(master, text="Zamknij", command=master.destroy)
        self.close_button.pack()

root = tk.Tk()
app = MyApp(root)
root.mainloop()