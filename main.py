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
label = tk.Label(root, text="Type below and test your speed!", font=("Arial", 20))
label.pack(pady=10)

# Text box
text_box = tk.Text(root, height=8, width=50, font=("Arial", 12))
text_box.pack(pady=10)

# Timer label
timer_label = tk.Label(root, text="Time: 60", font=("Arial", 20))
timer_label.pack(pady=20)


# Result box
result_label = tk.Label(root, text="Result: 0 words", font=("Arial", 18))
result_label.pack(pady=10)


# --- Functions ---
def countdown(time_left):
    if time_left > 0:
        timer_label.config(text=f"Time: {time_left}")
        root.after(1000, countdown, time_left - 1)
    else:
        timer_label.config(text="Time's up!")
        user_text = text_box.get("1.0", "end-1c")
        word_count = len(user_text.split())
        result_label.config(text=f"Result: {word_count} words")

# Start button
start_button = tk.Button(root, text="Start", font=("Arial", 18), command=lambda: countdown(60))
start_button.pack()

# SStop button
stop_button = tk.Button(root, text="Stop", font=("Arial", 18), command=lambda: countdown(60))
stop_button.pack()


# --- Run App ---
root.mainloop()