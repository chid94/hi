def calculate(num1, num2):
    return num1 + num2

def test_calculate():
    assert calculate(2, 4) == 6
    assert calculate(0, 0) == 0












































# import tkinter as tk
# from tkinter import messagebox

# # Dummy credentials
# USERNAME = "admin"
# PASSWORD = "password123"

# Function to open the new window (dashboard)
# def test_opendashboard():
#     dashboard = tk.Toplevel(root)
#     dashboard.state('zoomed')
#     dashboard.title("Dashboard")
#     dashboard.geometry("400x300")
    
#     # Dashboard UI
#     tk.Label(dashboard, text="Welcome to the Dashboard!", font=("Helvetica", 16)).pack(pady=20)
    
#     tk.Button(dashboard, text="Feature 1", width=20, command=lambda: messagebox.showinfo("Feature", "Feature 1 clicked")).pack(pady=10)
#     tk.Button(dashboard, text="Feature 2", width=20, command=lambda: messagebox.showinfo("Feature", "Feature 2 clicked")).pack(pady=10)
#     tk.Button(dashboard, text="Logout", width=20, command=dashboard.destroy).pack(pady=20)

# # Login functi on
# def test_login():
#     user = entry_username.get()
#     pw = entry_password.get()
#     if user == USERNAME and pw == PASSWORD:
#         messagebox.showinfo("Fuck YOU Yeah,")
#         test_opendashboard()
#     else:
#       messagebox.showerror( "Invalid username xor password, Sorry!")

# # Main Window
# root = tk.Tk() 
# root.state('zoomed')
# root.title("Login Page")
# root.geometry("300x200")
# root.resizable(False, False)

# # Username Entry
# tk.Label(root, text="Username").pack(pady=(20, 5))
# entry_username = tk.Entry(root)
# entry_username.pack()

# # Password Entry
# tk.Label(root, text="Password").pack(pady=(10, 5))
# entry_password = tk.Entry(root, show="*")
# entry_password.pack()

# # Login Button
# tk.Button(root, text="Login", command=test_login).pack(pady=20)

# # Run app
# root.mainloop()