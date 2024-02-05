from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
root = Tk()
root.title("Image Viewer")
root.geometry("600x600")
root.configure(bg="white")


image_label = Label(root, bg="white", highlightthickness=2, highlightbackground="white")
image_label.place(x=0, y=0, relwidth=1)


img_path = "earth.jpg"


def openFile():
    global img_path
    img_path = filedialog.askopenfilename(title="Open Image File", filetypes=(("Image files", "*.jpg *.gif *.png *.jpeg"),))
    print(img_path)
    img = Image.open(img_path)
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img
    img.close()


open_button = Button(root, text="Open Image", font=("Arial", 12, "bold"), bg="lightgrey", fg="black", relief="solid", padx=10, pady=5, command=openFile)
open_button.place(x=10, y=460)


def rotateImage():
    global img_path
    img = Image.open(img_path)
    img = img.rotate(180)
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img
    img.close()


rotate_button = Button(root, text="Rotate Image", font=("Arial", 12, "bold"), bg="lightgrey", fg="black", relief="solid", padx=10, pady=5, command=rotateImage)
rotate_button.place(x=120, y=460)

footer_label = Label(root, text="Created by: Your name", bg="white", fg="black")
footer_label.place(relx=0.5, rely=1, anchor=S)


root.mainloop()
