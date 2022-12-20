import tkinter as tk



def send():
    message = entry_field.get()
    entry_field.delete(0, tk.END)
    chat_box.insert(tk.END, message)



window = tk.Tk()
window.title("Chat GUI")
window.geometry("800x600")


messages_frame = tk.Frame(window)


scrollbar = tk.Scrollbar(messages_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


chat_box = tk.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.config(command=chat_box.yview)
chat_box.pack(side=tk.LEFT, fill=tk.BOTH)


messages_frame.pack()

entry_field = tk.Entry(window, width=50)
entry_field.pack()
send_button = tk.Button(window, text="Send")
send_button.pack()

send_button.config(command=send)
send_button.pack()


# Run the Tkinter event loop
window.mainloop()
