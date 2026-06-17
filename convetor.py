import customtkinter as ctk

# System appearance settings
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class SmartCalcPro(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("SmartCalc Pro - Converters")
        self.geometry("900x600")
        self.resizable(False, False)

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

        # Sidebar Buttons
        self.btn_unit = ctk.CTkButton(
            self.sidebar_frame, 
            text="Unit Converter", 
            font=("Arial", 14, "bold"),
            height=40,
            fg_color="#3b9eff",  # Initial active color
            hover_color="#2b7ecf",
            command=self.show_unit_converter
        )
        self.btn_unit.pack(pady=10, padx=15, fill="x")

        self.btn_currency = ctk.CTkButton(
            self.sidebar_frame, 
            text="Currency Exchange", 
            font=("Arial", 14, "bold"),
            height=40,
            fg_color="transparent",
            hover_color="#2d3034",
            command=self.show_currency_converter
        )
        self.btn_currency.pack(pady=10, padx=15, fill="x")

        # ---- MAIN CONTENT CONTAINER ----
        self.content_frame = ctk.CTkFrame(self, fg_color="#111214", corner_radius=0)
        self.content_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        
        # Initialize the first view
        self.show_unit_converter()

    def clear_content_frame(self):
        """Purani screen ke widgets hatane ke liye function"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def update_sidebar_colors(self, active_btn):
        """Button select hone par blue color switch karne ke liye"""
        if active_btn == "unit":
            self.btn_unit.configure(fg_color="#3b9eff")
            self.btn_currency.configure(fg_color="transparent")
        else:
            self.btn_unit.configure(fg_color="transparent")
            self.btn_currency.configure(fg_color="#3b9eff")

    # ---- SCREEN 1: UNIT CONVERTER ----
    def show_unit_converter(self):
        self.clear_content_frame()
        self.update_sidebar_colors("unit")

        # Heading
        title = ctk.CTkLabel(self.content_frame, text="Unit Converter", font=("Arial", 24, "bold"), text_color="#ffffff")
        title.pack(anchor="w", padx=30, pady=(20, 30))

        # Input Box
        lbl_from = ctk.CTkLabel(self.content_frame, text="From:", font=("Arial", 14), text_color="#aaaaaa")
        lbl_from.pack(anchor="w", padx=30, pady=2)
        
        entry_amount = ctk.CTkEntry(self.content_frame, placeholder_text="Enter Value", width=400, height=40, font=("Arial", 14))
        entry_amount.pack(anchor="w", padx=30, pady=(0, 15))

        # Dropdowns (Combobox)
        combo_from = ctk.CTkComboBox(self.content_frame, values=["Meters (m)", "Kilometers (km)", "Miles (mi)"], width=400, height=40)
        combo_from.pack(anchor="w", padx=30, pady=15)

        lbl_to = ctk.CTkLabel(self.content_frame, text="To:", font=("Arial", 14), text_color="#aaaaaa")
        lbl_to.pack(anchor="w", padx=30, pady=2)

        combo_to = ctk.CTkComboBox(self.content_frame, values=["Kilometers (km)", "Meters (m)", "Miles (mi)"], width=400, height=40)
        combo_to.pack(anchor="w", padx=30, pady=(0, 30))

        # Convert Button
        btn_convert = ctk.CTkButton(self.content_frame, text="Convert", width=180, height=40, font=("Arial", 14, "bold"))
        btn_convert.pack(anchor="w", padx=30)

    # ---- SCREEN 2: CURRENCY CONVERTER ----
    def show_currency_converter(self):
        self.clear_content_frame()
        self.update_sidebar_colors("currency")

        # Heading
        title = ctk.CTkLabel(self.content_frame, text="Currency Exchange", font=("Arial", 24, "bold"), text_color="#ffffff")
        title.pack(anchor="w", padx=30, pady=(20, 30))

        # Input Box
        lbl_from = ctk.CTkLabel(self.content_frame, text="From:", font=("Arial", 14), text_color="#aaaaaa")
        lbl_from.pack(anchor="w", padx=30, pady=2)

        entry_amount = ctk.CTkEntry(self.content_frame, placeholder_text="Enter Amount", width=400, height=40, font=("Arial", 14))
        entry_amount.pack(anchor="w", padx=30, pady=(0, 15))

        # Dropdowns
        combo_from = ctk.CTkComboBox(self.content_frame, values=["USD - United States Dollar", "EUR - Euro", "INR - Indian Rupee"], width=400, height=40)
        combo_from.pack(anchor="w", padx=30, pady=15)

        lbl_to = ctk.CTkLabel(self.content_frame, text="To:", font=("Arial", 14), text_color="#aaaaaa")
        lbl_to.pack(anchor="w", padx=30, pady=2)

        combo_to = ctk.CTkComboBox(self.content_frame, values=["INR - Indian Rupee", "USD - United States Dollar", "EUR - Euro"], width=400, height=40)
        combo_to.pack(anchor="w", padx=30, pady=(0, 20))

        # Output Display Label
        lbl_output_title = ctk.CTkLabel(self.content_frame, text="Converted Amount", font=("Arial", 14), text_color="#aaaaaa")
        lbl_output_title.pack(anchor="w", padx=30, pady=2)
        
        lbl_result = ctk.CTkLabel(self.content_frame, text="0.00", font=("Arial", 32, "bold"), text_color="#ffffff")
        lbl_result.pack(anchor="w", padx=30, pady=(0, 30))

        # Action Buttons Frame
        actions_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        actions_frame.pack(anchor="w", padx=30)

        btn_convert = ctk.CTkButton(actions_frame, text="Convert", width=180, height=40, font=("Arial", 14, "bold"), fg_color="#00b4d8", hover_color="#0077b6")
        btn_convert.grid(row=0, column=0, padx=(0, 15))

        btn_swap = ctk.CTkButton(actions_frame, text="Swap", width=180, height=40, font=("Arial", 14, "bold"), fg_color="#2d3034", hover_color="#40444b")
        btn_swap.grid(row=0, column=1)

if __name__ == "__main__":
    app = SmartCalcPro()
    app.mainloop()