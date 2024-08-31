from backend import createConnection
import settings
from tkinter import messagebox
import customtkinter as ctk

connection = createConnection(settings.msql_password)
cursor = connection.cursor()

# Fetch Products from the database  
def get_products(category_id, location1, location2, location3, location4):
    cursor.execute("SELECT product_id, name, description, unitPrice FROM products WHERE category_id = %s", (category_id,))
    for result in cursor:
        ctk.CTkLabel(location1, text=result[0], font=ctk.CTkFont(size=16, family="elephant"), anchor="w").pack(pady=2)
        ctk.CTkLabel(location2, text=result[1], font=ctk.CTkFont(size=16, family="elephant"), anchor="w").pack(pady=2)
        ctk.CTkLabel(location3, text=result[2], font=ctk.CTkFont(size=12, family="elephant"), anchor="w").pack(pady=2)
        ctk.CTkLabel(location4, text=result[3], font=ctk.CTkFont(size=16, family="elephant"), anchor="w").pack(pady=2)







# cursor.execute("SELECT product_id, name, description, unitPrice FROM products WHERE category_id ='JU00'")
# results = cursor.fetchall()
# for result in results:
    # print(result)
