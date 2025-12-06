import powerformule
import tkinter as tk
from tkinter import font
import math


def main():
    form = powerformule.formula()

    def enter_values():
        form.level = lvl_entry.get()
        form.rebirths = rebirths_value.get()
        form.potential = potential_value.get()
        form.saint_help_lvl = SG_value.get()
        form.hellish_help_lvl = HG_value.get()
        form.hellish_curse_lvl = HC_value.get()
        answer_value.set(form.value)

    root = tk.Tk()
    root.geometry("650x400")
    root.title("Change the power!")

    tk_font = font.Font(size=16)

    answer_value = tk.StringVar(value="0")
    lvl_value = tk.StringVar(value="1")
    rebirths_value = tk.StringVar(value="0")
    potential_value = tk.StringVar(value="1")
    SG_value = tk.StringVar(value="1")  # Saint Gift Level
    HG_value = tk.StringVar(value="1")  # Hellish Gift Level
    HC_value = tk.StringVar(value="1")  # Hellish Curse Level

    answer = tk.Label(root, textvariable=answer_value, font=tk_font)
    answer.pack(anchor='s', side="bottom")

    lvl_entry = tk.Entry(root, textvariable=lvl_value, font=tk_font)  # Level
    lvl_label = tk.Label(root, text="Level", font=tk_font)
    lvl_entry.place(relx=0.2, rely=0.1, relwidth=0.15, relheight=0.1)
    lvl_label.place(relx=0, rely=0.1, relwidth=0.2, relheight=0.1)

    rebirths_entry = tk.Entry(root, textvariable=rebirths_value, font=tk_font)
    rebirths_label = tk.Label(root, text="Rebirth", font=tk_font)
    rebirths_entry.place(relx=0.2, rely=0.2, relwidth=0.15, relheight=0.1)
    rebirths_label.place(relx=0, rely=0.2, relwidth=0.2, relheight=0.1)

    potential_entry = tk.Entry(root, textvariable=potential_value, font=tk_font)
    potential_label = tk.Label(root, text="Potential", font=tk_font)
    potential_entry.place(relx=0.2, rely=0.3, relwidth=0.15, relheight=0.1)
    potential_label.place(relx=0, rely=0.3, relwidth=0.2, relheight=0.1)

    SG_entry = tk.Entry(root, textvariable=SG_value, font=tk_font)
    SG_label = tk.Label(root, text="Saint gift", font=tk_font)
    SG_entry.place(relx=0.2, rely=0.4, relwidth=0.15, relheight=0.1)
    SG_label.place(relx=0, rely=0.4, relwidth=0.2, relheight=0.1)

    HG_entry = tk.Entry(root, textvariable=HG_value, font=tk_font)
    HG_label = tk.Label(root, text="Hellish gift", font=tk_font)
    HG_entry.place(relx=0.2, rely=0.5, relwidth=0.15, relheight=0.1)
    HG_label.place(relx=0, rely=0.5, relwidth=0.2, relheight=0.1)

    HC_entry = tk.Entry(root, textvariable=HC_value, font=tk_font)
    HC_label = tk.Label(root, text="Hellish curse", font=tk_font)
    HC_entry.place(relx=0.2, rely=0.6, relwidth=0.15, relheight=0.1)
    HC_label.place(relx=0, rely=0.6, relwidth=0.2, relheight=0.1)

    calc_button = tk.Button(root, text="Calculate", command=enter_values, font=tk_font)
    calc_button.place(relx=0.4, rely=0.5, relheight=0.2, relwidth=0.2)

    def window_size_changed(event):
        xpix, ypix = root.winfo_geometry().split("x")
        ypix = int(ypix.split("+")[0])
        xpix = int(xpix)
        diag = math.sqrt(xpix ** 2 + ypix ** 2)
        fontsize = diag * 0.01
        fontsize = int(fontsize) * 2
        tk_font.configure(size=fontsize)

    root.bind("<Configure>", window_size_changed)

    root.mainloop()


if __name__ == "__main__":
    main()
