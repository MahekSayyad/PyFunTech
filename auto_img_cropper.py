import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

start_x, start_y = 0, 0 
end_x, end_y = 0, 0
cropping = False

def select_image():
    global panelA
    
    path = filedialog.askopenfilename()
    if len(path) > 0:
        image = Image.open(path)
        image = image.resize((100, 100))
        image = ImageTk.PhotoImage(image)
        
        if panelA is None:
            panelA = tk.Label(image=image)
            panelA.image = image
            panelA.pack(side=tk.TOP, padx=10, pady=10)
        else:    
            panelA.configure(image=image)
            panelA.image = image
def start_crop(event):
    global start_x, start_y, cropping
    start_x, start_y = event.x, event.y 
    cropping = True

def end_crop(event):
    global end_x, end_y, cropping
    start_x, start_y = event.x, event.y 
    cropping = False     
    perform_crop()
    
def perform_crop():
    global start_x, start_y, end_x, end_y
    image_path = filedialog.askopenfilename()
    if image_path:
        Image = Image.open(image_path)
        cropped_image = image.crop((start_x, start_y))  
        cropped_image.show()
        cropped_image.save("cropped_image.png")   

root = tk.Tk()
root.title("Automatic Image Cropper")

panelA = None

canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)

canvas.bind("<ButtonPress-1>", start_crop)
canvas.bind("<B1-Motion>", lambda event: end_crop(event))

btn_select = tk.Button(root, text="Select Image", command=select_image)
btn_select.pack(side=tk.BOTTOM, padx=10, pady=10)

root.mainloop()
               