import customtkinter as ctk
import math

# System appearance settings
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class SmartCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("SmartCalc Pro - All In One")
        self.geometry("950x700")  # Calculator ke buttons fit karne ke liye thoda height badhaya hai
        self.resizable(False, False)

        # Calculator Expression Variable
        self.expression = ""

        # ---- LAYOUT CONFIGURATION ----
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ---- SIDEBAR FRAME ----
        self.sidebar_frame = ctk.CTkFrame(self, width=220, corner_radius=0, fg_color="#1a1c1e")
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_propagate(False)

        # App Title inside Sidebar
        self.app_title = ctk.CTkLabel(
            self.sidebar_frame, 
            text="SmartCalc Pro", 
            font=("Arial", 20, "bold"), 
            text_color="#3b9eff"
        )
        self.app_title.pack(pady=30, padx=20)

        # ---- NAVIGATION BUTTONS ----
        self.btn_calc = ctk.CTkButton(
            self.sidebar_frame, text="Scientific Calculator", font=("Arial", 14, "bold"), height=40,
            fg_color="#3b9eff", hover_color="#2b7ecf", command=self.show_calculator
        )
        self.btn_calc.pack(pady=10, padx=15, fill="x")

        self.btn_unit = ctk.CTkButton(
            self.sidebar_frame, text="Unit Converter", font=("Arial", 14, "bold"), height=40,
            fg_color="transparent", hover_color="#2d3034", command=self.show_unit_converter
        )
        self.btn_unit.pack(pady=10, padx=15, fill="x")

        self.btn_currency = ctk.CTkButton(
            self.sidebar_frame, text="Currency Exchange", font=("Arial", 14, "bold"), height=40,
            fg_color="transparent", hover_color="#2d3034", command=self.show_currency_converter
        )
        self.btn_currency.pack(pady=10, padx=15, fill="x")

        # ---- MAIN CONTENT CONTAINER ----
        self.content_frame = ctk.CTkFrame(self, fg_color="#111214", corner_radius=0)
        self.content_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        
        # Default view on startup
        self.show_calculator()

    def clear_content_frame(self):
        """Purani screen ke saare widgets ko saaf karne ke liye"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def update_sidebar_colors(self, active_btn):
        """Active button ko blue karne aur baaki ko transparent rakhne ke liye"""
        self.btn_calc.configure(fg_color="#3b9eff" if active_btn == "calc" else "transparent")
        self.btn_unit.configure(fg_color="#3b9eff" if active_btn == "unit" else "transparent")
        self.btn_currency.configure(fg_color="#3b9eff" if active_btn == "currency" else "transparent")


    # ==========================================
    # SCREEN 1: SCIENTIFIC CALCULATOR
    # ==========================================
    def show_calculator(self):
        self.clear_content_frame()
        self.update_sidebar_colors("calc")

        # Heading
        title = ctk.CTkLabel(self.content_frame, text="Scientific Calculator", font=("Arial", 22, "bold"), text_color="#ffffff")
        title.pack(anchor="w", padx=15, pady=(10, 10))

        # Calculator Display Entry
        self.display = ctk.CTkEntry(
            self.content_frame, font=("Arial", 24), justify="right", height=60, corner_radius=10,
            fg_color="#1e1e1e", text_color="#ffffff", border_color="#333333"
        )
        self.display.pack(fill="x", padx=15, pady=(0, 15))
        self.display.insert(0, self.expression)

        # Buttons Grid Frame
        button_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        button_frame.pack(fill="both", expand=True, padx=15, pady=5)

        # 6 Columns and 9 Rows setup
        for i in range(6): button_frame.grid_columnconfigure(i, weight=1, pad=5)
        for i in range(9): button_frame.grid_rowconfigure(i, weight=1, pad=5)

        # Layout Mapping (Row, Col)
        buttons_layout = [
            ('MC', 0, 0, '#2d2d2d'), ('MR', 0, 1, '#2d2d2d'), ('M+', 0, 2, '#2d2d2d'), ('M-', 0, 3, '#2d2d2d'), ('RAD', 0, 4, '#2d2d2d'), ('DEG', 0, 5, '#2d2d2d'),
            ('sin', 1, 0, '#2d2d2d'), ('cos', 1, 1, '#2d2d2d'), ('tan', 1, 2, '#2d2d2d'), ('asin', 1, 3, '#2d2d2d'), ('acos', 1, 4, '#2d2d2d'), ('atan', 1, 5, '#2d2d2d'),
            ('sinh', 2, 0, '#2d2d2d'), ('cosh', 2, 1, '#2d2d2d'), ('tanh', 2, 2, '#2d2d2d'), ('log', 2, 3, '#2d2d2d'), ('ln', 2, 4, '#2d2d2d'), ('10\u02e3', 2, 5, '#2d2d2d'),
            ('\u221a', 3, 0, '#2d2d2d'), ('\u00b3\u221a', 3, 1, '#2d2d2d'), ('x\u00b2', 3, 2, '#2d2d2d'), ('x\u00b3', 3, 3, '#2d2d2d'), ('x\u02b8', 3, 4, '#2d2d2d'), ('1/x', 3, 5, '#2d2d2d'),
            ('\u03c0', 4, 0, '#2d2d2d'), ('e', 4, 1, '#2d2d2d'), ('e\u02e3', 4, 2, '#2d2d2d'), ('x!', 4, 3, '#2d2d2d'), ('Abs', 4, 4, '#2d2d2d'), ('%', 4, 5, '#2d2d2d'),
            ('7', 5, 0, '#ff9500'), ('8', 5, 1, '#ff9500'), ('9', 5, 2, '#ff9500'), ('DEL', 5, 3, '#d43f3a'), ('AC', 5, 4, '#d43f3a'), ('\u00b1', 5, 5, '#2d2d2d'),
            ('4', 6, 0, '#ff9500'), ('5', 6, 1, '#ff9500'), ('6', 6, 2, '#ff9500'), ('\u00d7', 6, 3, '#2d2d2d'), ('\u00f7', 6, 4, '#2d2d2d'), ('Hyp', 6, 5, '#2d2d2d'),
            ('1', 7, 0, '#ff9500'), ('2', 7, 1, '#ff9500'), ('3', 7, 2, '#ff9500'), ('+', 7, 3, '#2d2d2d'), ('-', 7, 4, '#2d2d2d'), (',', 7, 5, '#2d2d2d'),
            ('0', 8, 0, '#ff9500'), ('00', 8, 1, '#ff9500'), ('.', 8, 2, '#ff9500'), ('EXP', 8, 3, '#2d2d2d'), ('=', 8, 4, '#4cd964'), ('^', 8, 5, '#2d2d2d')
        ]

        for text, row, col, color in buttons_layout:
            btn = ctk.CTkButton(
                button_frame, text=text, font=("Arial", 13, "bold"), fg_color=color,
                hover_color=self.get_hover_color(color), text_color="#ffffff", corner_radius=6,
                width=45, height=40, command=lambda t=text: self.on_calc_button_click(t)
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)

    def get_hover_color(self, hex_color):
        if hex_color == '#ff9500': return '#cc7a00' 
        if hex_color == '#d43f3a': return '#b22c28' 
        if hex_color == '#4cd964': return '#38b04a' 
        return '#3a3a3a' 

    def on_calc_button_click(self, char):
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

        # Update Live Display
        self.display.delete(0, ctk.END)
        self.display.insert(0, self.expression)


    # ==========================================
    # SCREEN 2: UNIT CONVERTER
    # ==========================================
    def show_unit_converter(self):
        self.clear_content_frame()
        self.update_sidebar_colors("unit")

        title = ctk.CTkLabel(self.content_frame, text="Unit Converter", font=("Arial", 24, "bold"), text_color="#ffffff")
        title.pack(anchor="w", padx=30, pady=(20, 30))

        lbl_from = ctk.CTkLabel(self.content_frame, text="From:", font=("Arial", 14), text_color="#aaaaaa")
        lbl_from.pack(anchor="w", padx=30, pady=2)
        
        entry_amount = ctk.CTkEntry(self.content_frame, placeholder_text="Enter Value", width=400, height=40, font=("Arial", 14))
        entry_amount.pack(anchor="w", padx=30, pady=(0, 15))

        combo_from = ctk.CTkComboBox(self.content_frame, values=["Meters (m)", "Kilometers (km)", "Miles (mi)"], width=400, height=40)
        combo_from.pack(anchor="w", padx=30, pady=15)

        lbl_to = ctk.CTkLabel(self.content_frame, text="To:", font=("Arial", 14), text_color="#aaaaaa")
        lbl_to.pack(anchor="w", padx=30, pady=2)

        combo_to = ctk.CTkComboBox(self.content_frame, values=["Kilometers (km)", "Meters (m)", "Miles (mi)"], width=400, height=40)
        combo_to.pack(anchor="w", padx=30, pady=(0, 30))

        btn_convert = ctk.CTkButton(self.content_frame, text="Convert", width=180, height=40, font=("Arial", 14, "bold"))
        btn_convert.pack(anchor="w", padx=30)


    # ==========================================
    # SCREEN 3: CURRENCY CONVERTER
    # ==========================================
    def show_currency_converter(self):
        self.clear_content_frame()
        self.update_sidebar_colors("currency")

        title = ctk.CTkLabel(self.content_frame, text="Currency Exchange", font=("Arial", 24, "bold"), text_color="#ffffff")
        title.pack(anchor="w", padx=30, pady=(20, 30))

        lbl_from = ctk.CTkLabel(self.content_frame, text="From:", font=("Arial", 14), text_color="#aaaaaa")
        lbl_from.pack(anchor="w", padx=30, pady=2)

        entry_amount = ctk.CTkEntry(self.content_frame, placeholder_text="Enter Amount", width=400, height=40, font=("Arial", 14))
        entry_amount.pack(anchor="w", padx=30, pady=(0, 15))

        combo_from = ctk.CTkComboBox(self.content_frame, values=["USD - United States Dollar", "EUR - Euro", "INR - Indian Rupee"], width=400, height=40)
        combo_from.pack(anchor="w", padx=30, pady=15)

        lbl_to = ctk.CTkLabel(self.content_frame, text="To:", font=("Arial", 14), text_color="#aaaaaa")
        lbl_to.pack(anchor="w", padx=30, pady=2)

        combo_to = ctk.CTkComboBox(self.content_frame, values=["INR - Indian Rupee", "USD - United States Dollar", "EUR - Euro"], width=400, height=40)
        combo_to.pack(anchor="w", padx=30, pady=(0, 20))

        lbl_output_title = ctk.CTkLabel(self.content_frame, text="Converted Amount", font=("Arial", 14), text_color="#aaaaaa")
        lbl_output_title.pack(anchor="w", padx=30, pady=2)
        
        lbl_result = ctk.CTkLabel(self.content_frame, text="0.00", font=("Arial", 32, "bold"), text_color="#ffffff")
        lbl_result.pack(anchor="w", padx=30, pady=(0, 30))

        actions_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        actions_frame.pack(anchor="w", padx=30)

        btn_convert = ctk.CTkButton(actions_frame, text="Convert", width=180, height=40, font=("Arial", 14, "bold"), fg_color="#00b4d8", hover_color="#0077b6")
        btn_convert.grid(row=0, column=0, padx=(0, 15))

        btn_swap = ctk.CTkButton(actions_frame, text="Swap", width=180, height=40, font=("Arial", 14, "bold"), fg_color="#2d3034", hover_color="#40444b")
        btn_swap.grid(row=0, column=1)


if __name__ == "__main__":
    app = SmartCalculator()
    app.mainloop()