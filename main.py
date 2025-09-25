#Countdown timer (60s): not just a timer window, but one that starts when you click Start.

#Accuracy check: instead of just counting words, compare what the user typed with a given sample text.

#Words per minute (WPM): words_typed / time_in_minutes.

#UI improvements: labels, font sizes, padding, so it looks cleaner.

#Disable input when time is up → so the user can’t keep typing after 60s.


import tkinter as tk

# --- Window Setup ---
root = tk.Tk()
root.title("Typing Speed Test")
root.geometry("600x400")

# --- Widgets ---
# Instructions
label = tk.Label(root, text="Type below and test your speed!", font=("Arial", 14))
label.pack(pady=10)

# Text box
text_box = tk.Text(root, height=8, width=50, font=("Arial", 12))
text_box.pack(pady=10)

# Timer label
timer_label = tk.Label(root, text="Time: 60", font=("Arial", 14))
timer_label.pack(pady=5)

# Start button
start_button = tk.Button(root, text="Start", font=("Arial", 12))
start_button.pack(pady=5)

# Result box
result_label = tk.Label(root, text="Result: 0 words", font=("Arial", 14))
result_label.pack(pady=10)

# --- Run App ---
root.mainloop()