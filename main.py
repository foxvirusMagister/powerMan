import powerformule
from powerformule import can_int
import tkinter as tk


def main():
    form = powerformule.formula()

    def enter_values():
        if can_int(lvl_entry.get()):  # What the fuck, this is absolutly shitty code...
            form.level = int(lvl_entry.get())
        if can_int(rebirths_value.get()):  # Just write this check in powerformule method
            form.rebirths = int(rebirths_value.get())
        if can_int(potential_value.get()):
            form.potential = int(potential_value.get())  # Why you still need to convert str type to int
        if can_int(SG_value.get()):
            form.saint_help_lvl = int(SG_value.get())  # If you already know that it can be converted
        if can_int(HG_value.get()):
            form.hellish_help_lvl = int(HG_value.get())
        if can_int(HC_value.get()):
            form.hellish_curse_lvl = int(HC_value.get())
        answer_value.set(form.value)


    root = tk.Tk()
    root.geometry("650x400")

    answer_value = tk.IntVar(value=0)
    lvl_value = tk.IntVar(value=1)
    rebirths_value = tk.IntVar(value=0)
    potential_value = tk.IntVar(value=1)
    SG_value = tk.IntVar(value=1)  # Saint Gift Level
    HG_value = tk.IntVar(value=1)  # Hellish Gift Level
    HC_value = tk.IntVar(value=1)  # Hellish Curse Level

    answer = tk.Label(root, textvariable=answer_value)
    answer.place(relx=0.4, rely=0.9)

    lvl_entry = tk.Entry(root, textvariable=lvl_value)
    lvl_entry.place(relx=0.05, rely=0.1)

    calc_button = tk.Button(root, text="Calculate", command=enter_values)
    calc_button.place(relx=0.4, rely=0.5)

    root.mainloop()


if __name__ == "__main__":
    main()
