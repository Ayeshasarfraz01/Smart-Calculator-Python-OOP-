import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("340x480")
        self.resizable(False, False)
        self.configure(bg="#1e1e2e")

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=5)
        self.columnconfigure(0, weight=1)

        self.expr = ""

        self.setup_ui()
        self.bind("<Key>", self.handle_key)

    def setup_ui(self):
        display_frame = tk.Frame(self, bg="#1e1e2e", padx=10, pady=10)
        display_frame.grid(row=0, column=0, sticky="nsew")

        self.screen = tk.Entry(
            display_frame,
            font=("Segoe UI", 28, "bold"),
            bg="#181825",
            fg="#cdd6f4",
            bd=0,
            justify="right",
            insertbackground="#cdd6f4"
        )
        self.screen.pack(expand=True, fill="both", ipady=10)

        btn_frame = tk.Frame(self, bg="#1e1e2e", padx=10, pady=10)
        btn_frame.grid(row=1, column=0, sticky="nsew")

        for i in range(5):
            btn_frame.rowconfigure(i, weight=1)
        for i in range(4):
            btn_frame.columnconfigure(i, weight=1)

        layout = [
            ('C', 0, 0, "#110E0F"), ('(', 0, 1, "#131E31"), (')', 0, 2, "#131E31"), ('/', 0, 3, "#30241d"),
            ('7', 1, 0, '#313244'), ('8', 1, 1, '#313244'), ('9', 1, 2, '#313244'), ('*', 1, 3, "#30241d"),
            ('4', 2, 0, '#313244'), ('5', 2, 1, '#313244'), ('6', 2, 2, '#313244'), ('-', 2, 3, '#30241d'),
            ('1', 3, 0, '#313244'), ('2', 3, 1, '#313244'), ('3', 3, 2, '#313244'), ('+', 3, 3, '#30241d'),
            ('0', 4, 0, '#313244'), ('.', 4, 1, '#313244'), ('⌫', 4, 2, "#30241d"), ('=', 4, 3, '#30241d')
        ]

        accent_colors = ["#a1cee3", "#131318", "#0f0d0c"]

        for text, r, c, bg in layout:
            fg = "#11111b" if bg in accent_colors else "#cdd6f4"
            btn = tk.Button(
                btn_frame,
                text=text,
                font=("Segoe UI", 16, "bold"),
                bg=bg,
                fg=fg,
                activebackground="#45475a",
                activeforeground="#ffffff",
                bd=0,
                relief="flat",
                command=lambda val=text: self.press(val)
            )
            btn.grid(row=r, column=c, padx=4, pady=4, sticky="nsew")

    def press(self, val):
        if val == 'C':
            self.expr = ""
        elif val == '⌫':
            self.expr = self.expr[:-1]
        elif val == '=':
            self.evaluate()
            return
        else:
            self.expr += str(val)

        self.refresh()

    def handle_key(self, e):
        if e.char in "0123456789.+-*/()":
            self.expr += e.char
            self.refresh()
        elif e.keysym == "Return":
            self.evaluate()
        elif e.keysym == "BackSpace":
            self.expr = self.expr[:-1]
            self.refresh()
        elif e.keysym == "Escape":
            self.expr = ""
            self.refresh()

    def evaluate(self):
        try:
            res = eval(self.expr)
            if isinstance(res, float) and res.is_integer():
                res = int(res)
            self.expr = str(res)
        except Exception:
            self.expr = "Error"
        self.refresh()

    def refresh(self):
        self.screen.delete(0, tk.END)
        self.screen.insert(0, self.expr)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()