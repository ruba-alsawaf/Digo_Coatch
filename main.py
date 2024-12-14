import tkinter as tk
from tkinter import messagebox
from exercises.squats import SquatsExercise
from exercises.arm_stretch import ArmStretchExercise

# تمارين متوفرة
exercises = {
    "Squats": SquatsExercise,
    "Arm Stretch": ArmStretchExercise
}

def start_exercise():
    exercise_name = selected_exercise.get()
    if exercise_name == "Select an exercise":
        messagebox.showwarning("Warning", "Please select an exercise.")
    else:
        exercise_class = exercises.get(exercise_name)
        exercise = exercise_class(exercise_name)  # تمرير اسم التمرين
        exercise.start()

# إنشاء نافذة التطبيق
window = tk.Tk()
window.title("Virtual Personal Trainer")
window.geometry("400x400")

# العنوان الرئيسي
tk.Label(window, text="Input Type Selection", font=("Arial", 14)).pack(pady=10)

# قائمة التمارين
tk.Label(window, text="Select Exercise", font=("Arial", 12)).pack(pady=10)
selected_exercise = tk.StringVar(value="Select an exercise")
exercise_menu = tk.OptionMenu(window, selected_exercise, "Select an exercise", *exercises.keys())
exercise_menu.config(width=20, bg="lightgray")
exercise_menu.pack(pady=10)

# زر بدء التمرين
tk.Button(window, text="Start Exercise", command=start_exercise, width=20, bg="lightblue").pack(pady=10)

# تشغيل واجهة التطبيق
window.mainloop()
