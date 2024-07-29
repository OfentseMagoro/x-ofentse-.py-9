import tkinter as tk
from tkinter import ttk, messagebox
import pyodbc

# Database connection function
def connect_to_database(server, database, username, password):
    try:
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        conn = pyodbc.connect(connection_string)
        return conn
    except Exception as e:
        messagebox.showerror("Connection Error", f"Failed to connect to database: {e}")
        return None

# Function to fetch data from the database
def fetch_data():
    server = server_entry.get()
    database = database_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    
    conn = connect_to_database(server, database, username, password)
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM TableTkinter")  # Replace with your actual table name
            rows = cursor.fetchall()
            for row in rows:
                tree.insert("", tk.END, values=row)
        except Exception as e:
            messagebox.showerror("Fetch Error", f"Failed to fetch data: {e}")
        finally:
            cursor.close()
            conn.close()

# Setting up the main application window
root = tk.Tk()
root.title("Database Fetcher")
root.geometry("600x400")
root.configure(bg='#4CAF50')

# Frame for database connection inputs
frame = ttk.Frame(root)
frame.pack(pady=20)

# Input fields for database connection
ttk.Label(frame, text="Server:").grid(row=0, column=0, padx=5, pady=5)
server_entry = ttk.Entry(frame)
server_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame, text="Database:").grid(row=1, column=0, padx=5, pady=5)
database_entry = ttk.Entry(frame)
database_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame, text="Username:").grid(row=2, column=0, padx=5, pady=5)
username_entry = ttk.Entry(frame)
username_entry.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(frame, text="Password:").grid(row=3, column=0, padx=5, pady=5)
password_entry = ttk.Entry(frame, show='*')
password_entry.grid(row=3, column=1, padx=5, pady=5)

# Button to fetch data
fetch_button = ttk.Button(root, text="Fetch Data", command=fetch_data)
fetch_button.pack(pady=10)

# Treeview for displaying data
tree = ttk.Treeview(root, columns=("Column1", "Column2", "Column3"), show='headings')  # Adjust columns as needed
tree.heading("Column1", text="Project ID")
tree.heading("Column2", text="Name")
tree.heading("Column3", text="Date")
tree.pack(pady=20)

# Run the application
root.mainloop()