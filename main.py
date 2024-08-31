import customtkinter as ctk
from menu import menu
import settings
from menu import menu
from cart import cart

class main(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("light")
        self.title("BRANDON SNACKETTE SOLUTIONS")
        self.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
        self.resizable(True, True)

        # The Menu Frame
        self.menu_frame = menu()
        self.menu_frame.pack(fill="both", expand=True, side="top")

        # The Lower Frame
        self.cart_frame = cart()
        self.cart_frame.pack(fill="both", expand=True)
        



app = main()
app.mainloop()