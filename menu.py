import customtkinter as ctk
from middleware import get_products
import settings


class menu(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        # Putting the frame parts
        # Header
        self.header()
        self.menu_list()
        
       

    # Frame Header
    def header(self):
        # Setting up the header
        self.header = ctk.CTkFrame(self, height=20)
        self.header.pack(fill="x", expand=False, side="top")

        ctk.CTkLabel(self.header,text="WELCOME").pack(side="left", padx=3, fill="y")
        ctk.CTkLabel(self.header,text="DATE AND TIME").pack(side="right", padx=3, fill="y")

    # Menu list frame   
    def menu_list(self):
        self.menu_list = ctk.CTkFrame(self)
        self.menu_list.pack(fill="x")

        # title
        ctk.CTkLabel(self.menu_list, text="SELECT THE MEAL TAB YOU WANT", font=ctk.CTkFont(
            size=16, weight="bold", family="Times New Roman")).pack(side="top")
        
        # Creating a tab view
        self.menu_tabView = ctk.CTkTabview(self.menu_list)
        self.menu_tabView.pack(fill="x", expand=True, pady=5)
        self.menu_tabView.add("JUICE")
        self.menu_tabView.add("LUNCH")
        self.menu_tabView.add("SOFT DRINKS")
        self.menu_tabView.add("PLUS MEALS")
        self.menu_tabView.add("BEVERAGES")
        self.menu_tabView.add("FRUITS")
        self.menu_tabView.add("CAKES")

        # Adding tab content
        self.juice_tab()
        self.lunch_tab()
        self.drinks_tab()
        self.plus_tab()
        self.beverages_tab()
        self.fruits_tab()
        self.cakes_tab()


    # Juice tab
    def juice_tab(self):
        # The Scrollable frame
        self.juice_tab = ctk.CTkScrollableFrame(self.menu_tabView.tab("JUICE"), scrollbar_button_hover_color="blue")
        self.juice_tab.pack(fill="both", expand=True)
        # Tittle
        the_top = ctk.CTkFrame(self.juice_tab,height=25)
        the_top.pack(fill="x", expand = False, side="top")
        # Addin title bar
        self.tab_title_bar(the_top)
        
        # Items Frame
        self.juice_item_frames = ctk.CTkFrame(self.juice_tab, height=settings.frame_height)
        self.juice_item_frames.pack(fill="both", expand = True)

        # widgets
        self.juice_code_frame = ctk.CTkFrame(self.juice_item_frames)
        self.juice_code_frame.place(relx=0.1, rely=0)

        self.juice_name_frame = ctk.CTkFrame(self.juice_item_frames)
        self.juice_name_frame.place(relx=0.3, rely=0)
       

        self.juice_description_frame = ctk.CTkFrame(self.juice_item_frames)
        self.juice_description_frame.place(relx=0.5, rely=0)
    
        self.juice_price_frame = ctk.CTkFrame(self.juice_item_frames)
        self.juice_price_frame.place(relx=0.9, rely=0)


        # Getting the products
        code = "JU00"
        get_products(code, self.juice_code_frame, self.juice_name_frame, self.juice_description_frame, self.juice_price_frame)

    # Lunch Tab
    def lunch_tab(self):
        # The Scrollable frame
        self.lunch_tab = ctk.CTkScrollableFrame(self.menu_tabView.tab("LUNCH"), height=220)
        self.lunch_tab.pack(fill="x", expand=True)
        # Tittle
        the_top = ctk.CTkFrame(self.lunch_tab, height=30)
        the_top.pack(fill="both", expand = True, side="top")
        # Addin title bar
        self.tab_title_bar(the_top)
        
        
        # Items Frame
        self.lunch_item_frames = ctk.CTkFrame(self.lunch_tab, height=settings.frame_height)
        self.lunch_item_frames.pack(fill="both", expand = True)

        # widgets
        self.lunch_code_frame = ctk.CTkFrame(self.lunch_item_frames)
        self.lunch_code_frame.place(relx=0.1, rely=0)

        self.lunch_name_frame = ctk.CTkFrame(self.lunch_item_frames)
        self.lunch_name_frame.place(relx=0.3, rely=0)
        

        self.lunch_description_frame = ctk.CTkFrame(self.lunch_item_frames)
        self.lunch_description_frame.place(relx=0.5, rely=0)

        self.lunch_price_frame = ctk.CTkFrame(self.lunch_item_frames)
        self.lunch_price_frame.place(relx=0.9, rely=0)

         # Getting the products
        code = "LU00"
        get_products(code, self.lunch_code_frame, self.lunch_name_frame, self.lunch_description_frame, self.lunch_price_frame)
    
    # SOFT DRINKS TAB
    def drinks_tab(self):
        # The Scrollable frame
        self.drinks_tab = ctk.CTkScrollableFrame(self.menu_tabView.tab("SOFT DRINKS"), height=220)
        self.drinks_tab.pack(fill="x", expand=True)
        # Tittle
        the_top = ctk.CTkFrame(self.drinks_tab, height=30)
        the_top.pack(fill="both", expand = True, side="top")
        # Addin title bar
        self.tab_title_bar(the_top)
        
        # Items Frame
        self.drinks_item_frames = ctk.CTkFrame(self.drinks_tab, height=settings.frame_height)
        self.drinks_item_frames.pack(fill="both", expand = True)

        # widgets
        self.drinks_code_frame = ctk.CTkFrame(self.drinks_item_frames)
        self.drinks_code_frame.place(relx=0.1, rely=0)

        self.drinks_name_frame = ctk.CTkFrame(self.drinks_item_frames)
        self.drinks_name_frame.place(relx=0.3, rely=0)
       

        self.drinks_description_frame = ctk.CTkFrame(self.drinks_item_frames)
        self.drinks_description_frame.place(relx=0.5, rely=0)
    
        self.drinks_price_frame = ctk.CTkFrame(self.drinks_item_frames)
        self.drinks_price_frame.place(relx=0.9, rely=0)


        # Getting the products
        code = "SD00"
        get_products(code, self.drinks_code_frame, self.drinks_name_frame, self.drinks_description_frame, self.drinks_price_frame)

    # plus meals Tab
    def plus_tab(self):
        # The Scrollable frame
        self.plus_tab = ctk.CTkScrollableFrame(self.menu_tabView.tab("PLUS MEALS"), height=220)
        self.plus_tab.pack(fill="x", expand=True)
        # Tittle
        the_top = ctk.CTkFrame(self.plus_tab, height=30)
        the_top.pack(fill="both", expand = True, side="top")
        # Addin title bar
        self.tab_title_bar(the_top)
        
        
        # Items Frame
        self.plus_item_frames = ctk.CTkFrame(self.plus_tab, height=settings.frame_height)
        self.plus_item_frames.pack(fill="both", expand = True)

        # widgets
        self.plus_code_frame = ctk.CTkFrame(self.plus_item_frames)
        self.plus_code_frame.place(relx=0.1, rely=0)

        self.plus_name_frame = ctk.CTkFrame(self.plus_item_frames)
        self.plus_name_frame.place(relx=0.3, rely=0)
        

        self.plus_description_frame = ctk.CTkFrame(self.plus_item_frames)
        self.plus_description_frame.place(relx=0.5, rely=0)

        self.plus_price_frame = ctk.CTkFrame(self.plus_item_frames)
        self.plus_price_frame.place(relx=0.9, rely=0)

        # Getting the products
        code = "PM00"
        get_products(code, self.plus_code_frame, self.plus_name_frame, self.plus_description_frame, self.plus_price_frame)
   
   # beverages Tab
    def beverages_tab(self):
        # The Scrollable frame
        self.beverages_tab = ctk.CTkScrollableFrame(self.menu_tabView.tab("BEVERAGES"), height=220)
        self.beverages_tab.pack(fill="x", expand=True)
        # Tittle
        the_top = ctk.CTkFrame(self.beverages_tab, height=30)
        the_top.pack(fill="both", expand = True, side="top")
        # Addin title bar
        self.tab_title_bar(the_top)
        
        
        # Items Frame
        self.beverages_item_frames = ctk.CTkFrame(self.beverages_tab, height=settings.frame_height)
        self.beverages_item_frames.pack(fill="both", expand = True)

        # widgets
        self.beverages_code_frame = ctk.CTkFrame(self.beverages_item_frames)
        self.beverages_code_frame.place(relx=0.1, rely=0)

        self.beverages_name_frame = ctk.CTkFrame(self.beverages_item_frames)
        self.beverages_name_frame.place(relx=0.3, rely=0)
        

        self.beverages_description_frame = ctk.CTkFrame(self.beverages_item_frames)
        self.beverages_description_frame.place(relx=0.5, rely=0)

        self.beverages_price_frame = ctk.CTkFrame(self.beverages_item_frames)
        self.beverages_price_frame.place(relx=0.9, rely=0)

         # Getting the products
        code = "BV00"
        get_products(code, self.beverages_code_frame, self.beverages_name_frame, self.beverages_description_frame, self.beverages_price_frame)
    
    # Fruits Tab
    def fruits_tab(self):
        # The Scrollable frame
        self.fruits_tab = ctk.CTkScrollableFrame(self.menu_tabView.tab("FRUITS"), height=220)
        self.fruits_tab.pack(fill="x", expand=True)
        # Tittle
        the_top = ctk.CTkFrame(self.fruits_tab, height=30)
        the_top.pack(fill="both", expand = True, side="top")
        # Addin title bar
        self.tab_title_bar(the_top)
        
        
        # Items Frame
        self.fruits_item_frames = ctk.CTkFrame(self.fruits_tab, height=settings.frame_height)
        self.fruits_item_frames.pack(fill="both", expand = True)

        # widgets
        self.fruits_code_frame = ctk.CTkFrame(self.fruits_item_frames)
        self.fruits_code_frame.place(relx=0.1, rely=0)

        self.fruits_name_frame = ctk.CTkFrame(self.fruits_item_frames)
        self.fruits_name_frame.place(relx=0.3, rely=0)
        

        self.fruits_description_frame = ctk.CTkFrame(self.fruits_item_frames)
        self.fruits_description_frame.place(relx=0.5, rely=0)

        self.fruits_price_frame = ctk.CTkFrame(self.fruits_item_frames)
        self.fruits_price_frame.place(relx=0.9, rely=0)

         # Getting the products
        code = "FT00"
        get_products(code, self.fruits_code_frame, self.fruits_name_frame, self.fruits_description_frame, self.fruits_price_frame)

    # Cakes Tab
    def cakes_tab(self):
        # The Scrollable frame
        self.cakes_tab = ctk.CTkScrollableFrame(self.menu_tabView.tab("CAKES"), height=220)
        self.cakes_tab.pack(fill="x", expand=True)
        # Tittle
        the_top = ctk.CTkFrame(self.cakes_tab, height=30)
        the_top.pack(fill="both", expand = True, side="top")
        # Addin title bar
        self.tab_title_bar(the_top)
        
        
        # Items Frame
        self.cakes_item_frames = ctk.CTkFrame(self.cakes_tab, height=settings.frame_height)
        self.cakes_item_frames.pack(fill="both", expand = True)

        # widgets
        self.cakes_code_frame = ctk.CTkFrame(self.cakes_item_frames)
        self.cakes_code_frame.place(relx=0.1, rely=0)

        self.cakes_name_frame = ctk.CTkFrame(self.cakes_item_frames)
        self.cakes_name_frame.place(relx=0.25, rely=0)
        

        self.cakes_description_frame = ctk.CTkFrame(self.cakes_item_frames)
        self.cakes_description_frame.place(relx=0.4, rely=0)

        self.cakes_price_frame = ctk.CTkFrame(self.cakes_item_frames)
        self.cakes_price_frame.place(relx=0.9, rely=0)

         # Getting the products
        code = "CK00"
        get_products(code, self.cakes_code_frame, self.cakes_name_frame, self.cakes_description_frame, self.cakes_price_frame)


    # Title frame initialiser
    def tab_title_bar(self, location):
        # Widgets
        ctk.CTkLabel(location, text="CODE", font=ctk.CTkFont(
            size=18, weight="bold", family="Elephant"), text_color='red').place(relx=0.1, y=0)
        ctk.CTkLabel(location, text="NAME", font=ctk.CTkFont(
            size=18, weight="bold", family="Elephant"), text_color='red').place(relx=0.3, rely=0)
        ctk.CTkLabel(location, text="DESCRIPTION", font=ctk.CTkFont(
            size=18, weight="bold", family="Elephant"), text_color='red').place(relx=0.5, rely=0)
        ctk.CTkLabel(location, text="PRICE(Ksh)", font=ctk.CTkFont(
            size=18, weight="bold", family="Elephant"), text_color='red').place(relx=0.9, rely=0)

        
        
        
        


       
        