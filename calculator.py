import customtkinter as ctk
import math

# System settings for Dark Mode
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class ScientificCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Scientific Calculator V2")
        self.geometry("400x650")
        self.resizable(False, False)

        # Main Expression String
        self.expression = ""

        # ---- DISPLAY ----
        self.display = ctk.CTkEntry(
            self, 
            font=("Arial", 24), 
            justify="right", 
            height=70, 
            corner_radius=10,
            fg_color="#1e1e1e",
            text_color="#ffffff",
            border_color="#333333"
        )
        self.display.pack(fill="x", padx=15, pady=20)

        # ---- BUTTONS FRAME ----
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(fill="both", expand=True, padx=15, pady=10)

        # Grid configuration (6 columns)
        for i in range(6):
            self.button_frame.grid_columnconfigure(i, weight=1, pad=5)
        for i in range(9):
            self.button_frame.grid_rowconfigure(i, weight=1, pad=5)

        self.create_buttons()

    def create_buttons(self):
        # Buttons Layout Mapping (Row, Col)
        buttons_layout = [
            # Row 0
            ('MC', 0, 0, '#2d2d2d'), ('MR', 0, 1, '#2d2d2d'), ('M+', 0, 2, '#2d2d2d'), ('M-', 0, 3, '#2d2d2d'), ('RAD', 0, 4, '#2d2d2d'), ('DEG', 0, 5, '#2d2d2d'),
            # Row 1
            ('sin', 1, 0, '#2d2d2d'), ('cos', 1, 1, '#2d2d2d'), ('tan', 1, 2, '#2d2d2d'), ('asin', 1, 3, '#2d2d2d'), ('acos', 1, 4, '#2d2d2d'), ('atan', 1, 5, '#2d2d2d'),
            # Row 2
            ('sinh', 2, 0, '#2d2d2d'), ('cosh', 2, 1, '#2d2d2d'), ('tanh', 2, 2, '#2d2d2d'), ('log', 2, 3, '#2d2d2d'), ('ln', 2, 4, '#2d2d2d'), ('10\u02e3', 2, 5, '#2d2d2d'),
            # Row 3
            ('\u221a', 3, 0, '#2d2d2d'), ('\u00b3\u221a', 3, 1, '#2d2d2d'), ('x\u00b2', 3, 2, '#2d2d2d'), ('x\u00b3', 3, 3, '#2d2d2d'), ('x\u02b8', 3, 4, '#2d2d2d'), ('1/x', 3, 5, '#2d2d2d'),
            # Row 4
            ('\u03c0', 4, 0, '#2d2d2d'), ('e', 4, 1, '#2d2d2d'), ('e\u02e3', 4, 2, '#2d2d2d'), ('x!', 4, 3, '#2d2d2d'), ('Abs', 4, 4, '#2d2d2d'), ('%', 4, 5, '#2d2d2d'),
            
            # Row 5 (Numbers start here)
            ('7', 5, 0, '#ff9500'), ('8', 5, 1, '#ff9500'), ('9', 5, 2, '#ff9500'), ('DEL', 5, 3, '#d43f3a'), ('AC', 5, 4, '#d43f3a'), ('\u00b1', 5, 5, '#2d2d2d'),
            # Row 6
            ('4', 6, 0, '#ff9500'), ('5', 6, 1, '#ff9500'), ('6', 6, 2, '#ff9500'), ('\u00d7', 6, 3, '#2d2d2d'), ('\u00f7', 6, 4, '#2d2d2d'), ('Hyp', 6, 5, '#2d2d2d'),
            # Row 7
            ('1', 7, 0, '#ff9500'), ('2', 7, 1, '#ff9500'), ('3', 7, 2, '#ff9500'), ('+', 7, 3, '#2d2d2d'), ('-', 7, 4, '#2d2d2d'), (',', 7, 5, '#2d2d2d'),
            # Row 8 (0, 00, . ko ek sath set kiya hai)
            ('0', 8, 0, '#ff9500'), ('00', 8, 1, '#ff9500'), ('.', 8, 2, '#ff9500'), ('EXP', 8, 3, '#2d2d2d'), ('=', 8, 4, '#4cd964'), ('^', 8, 5, '#2d2d2d')
        ]

        for text, row, col, color in buttons_layout:
            btn = ctk.CTkButton(
                self.button_frame, 
                text=text,
                font=("Arial", 14, "bold"),
                fg_color=color,
                hover_color=self.get_hover_color(color),
                text_color="#ffffff",
                corner_radius=6,
                width=50,
                height=45,
                command=lambda t=text: self.on_button_click(t)
            )
            if text == '=':
                btn.grid(row=row, column=col, columnspan=1, sticky="nsew", padx=3, pady=3)
            else:
                btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)

    def get_hover_color(self, hex_color):
        if hex_color == '#ff9500': return '#cc7a00' 
        if hex_color == '#d43f3a': return '#b22c28' 
        if hex_color == '#4cd964': return '#38b04a' 
        return '#3a3a3a' 

    def on_button_click(self, char):
        if char == "AC":
            self.expression = ""
        elif char == "DEL":
            self.expression = self.expression[:-1]
        elif char == "=":
            try:
                expr = self.expression.replace('\u00d7', '*').replace('\u00f7', '/')
                self.expression = str(eval(expr))
            except Exception:
                self.expression = "Error"
        else:
            if self.expression == "Error":
                self.expression = ""
            self.expression += str(char)

        # Update Display
        self.display.delete(0, ctk.END)
        self.display.insert(0, self.expression)

if __name__ == "__main__":
    app = ScientificCalculator()
    app.mainloop()