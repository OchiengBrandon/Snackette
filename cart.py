import customtkinter as ctk
from middleware import get_products
import settings

class cart(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)

        self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)

        # Putting Other Frames
        self.left_bar()
        self.right_bar()


    # The left bar
    def left_bar(self):
        self.left_bar = ctk.CTkFrame(self)
        self.left_bar.grid(row = 0, column=0)
        ctk.CTkButton(self.left_bar,text="How is the testing").pack()

        

    # The right Bar
    def right_bar(self):
        self.right_bar = ctk.CTkFrame(self)
        self.right_bar.grid(row = 0, column=1)
        ctk.CTkButton(self.right_bar,text="How is the testing").pack()
        
