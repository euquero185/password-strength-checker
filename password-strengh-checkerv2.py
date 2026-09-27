import tkinter as tk
import time

def program():
    # Create the main window
    root = tk.Tk()
    root.title("Password Strengh Checker")
    root.geometry("600x500")
    root.resizable(False, False)

    label_top = tk.Label(root, text="Please insert a password", font=("Arial", 20, "bold"))
    label_top.pack(side="top", pady= 20)

    password = entry = tk.Entry(root, width= 40)
    entry.pack(pady= 30)

    label_show = None
    label_final = None

    def checker():
        nonlocal label_show, label_final

        password = entry.get()

        # Remove os labels da verificação anterior antes de mostrar os novos
        if label_show is not None:
            label_show.destroy()
            label_show = None
        if label_final is not None:
            label_final.destroy()
            label_final = None

        has_upper = False
        has_lower = False
        has_number = False
        has_less_than_8_letters = False
        has_more_than_8_letter = False
        has_more_than_16_letter = False

        for char in password:
            if char.isupper():
                has_upper = True
            if char.islower():
                has_lower = True
            if char.isdigit():
                has_number = True

            if len(password) >= 16:
                has_more_than_16_letter = True
            if len(password) >= 8:
                has_more_than_8_letter = True
            if len(password) < 8:
                has_less_than_8_letters = True

        #Final Part
        if has_upper and has_lower and has_number and has_more_than_16_letter:
            label_show = tk.Label(root, text="Calculating password strengh", font=("Arial", 20, "bold"))
            label_show.pack(anchor="center", pady=20)
            root.update()
            time.sleep(3)
            label_final = tk.Label(root, text="Your password is very strong", font=("Arial", 20, "bold"))
            label_final.pack(anchor="center", pady=20)
        elif has_upper and has_lower and has_number and has_more_than_8_letter:
            label_show = tk.Label(root, text="Calculating password strengh", font=("Arial", 20, "bold"))
            label_show.pack(anchor="center", pady=20)
            root.update()
            time.sleep(3)
            label_final = tk.Label(root, text="Your password is strong", font=("Arial", 20, "bold"))
            label_final.pack(anchor="center", pady=20)
        elif (has_upper and has_lower) or (has_upper and has_number) or (has_lower and has_number):
            label_show = tk.Label(root, text="Calculating password strengh", font=("Arial", 20, "bold"))
            label_show.pack(anchor="center", pady=20)
            root.update()
            time.sleep(3)
            if has_more_than_8_letter:
                label_final = tk.Label(root, text="Your password is medium", font=("Arial", 20, "bold"))
                label_final.pack(anchor="center", pady=20)
            else:
                label_final = tk.Label(root, text="Your password is weak", font=("Arial", 20, "bold"))
                label_final.pack(anchor="center", pady=20)
        else:
            label_final = tk.Label(root, text="Your password is very weak", font=("Arial", 20, "bold"))
            label_final.pack(anchor="center", pady=20)

    #Add a button
    button = tk.Button(root, text="Check Password", command=checker)
    button.pack(pady=20)

    root.mainloop()

program()
