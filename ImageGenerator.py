from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import openai
import os
import base64
from PIL import Image, ImageTk
OUTPUT_DIR = "outputs"

client = openai.OpenAI(api_key = 'your api key')
window = ThemedTk(theme="equilux")
window.configure(themebg="equilux")
window.geometry("500x800")
window.title("AI.Generator")
window.resizable(False, False)

image_paths = []
cIndex = 0

def generate_ideas(user_text, n):
    prompt = (f"Generate {n} a prompt that will be given to a image generator, make it straight forward, based on: {user_text}\n"
              f"Return ONLY a numbered list from 1 to {n}. One idea per line."
              )

    resp = client.chat.completions.create(
        model = "gpt-4-turbo",
        messages = [{"role": "user", "content": prompt}],
        temperature = 0.9
    )
    ideas = []
    for line in resp.choices[0].message.content.splitlines():
        print(line)
        line = line.strip()
        if line != "":
            ideas.append(line)
    return ideas[:n]

def generate_images_from_ideas(ideas):
    paths = []

    for i in range(len(ideas)):
        idea = ideas[i]

        img = client.images.generate(
            model = "dall-e-3",
            prompt = idea,
            size = "1024x1024",
            n = 1
        )

        url = img.data[0].url
        print(url)

def generate_images_from_ideas2(ideas):
    paths = []

    for i in range(len(ideas)):

        idea = ideas[i]

        img = client.images.generate(
            model = "gpt-image-1.5",
            prompt = ideas[i],
            size = "1024x1024",
            n = 1,
            output_format = "jpeg"
        )

        filepath = os.path.join(OUTPUT_DIR, f"request_{i+1}.jpg")

        b64 = img.data[0].b64_json
        print(b64)

        with open(filepath, "wb") as f:
            f.write(base64.b64decode(b64))

        paths.append(filepath)

    return paths

def showImage(ind):
    global imagePreview

    img = Image.open(image_paths[ind])
    img = img.resize((400, 400), Image.Resampling.LANCZOS)
    imagePreview = ImageTk.PhotoImage(img)
    image_label.configure(image = imagePreview)

def process(event = None):
    global image_paths
    user = text_widget.get()
    if rb.get() == "Choice15":
        n = 3
    else:
        n = 2

    ideas = generate_ideas(user, n)
    image_paths = generate_images_from_ideas2(ideas)

    cIntex = 0
    showImage(0)

def nextImg(event = None):
    global cIndex
    cIndex = (cIndex + 1) % len(image_paths)
    showImage(cIndex)

def prevImg():
    global cIndex
    if not image_paths:
        return
    cIndex = (cIndex - 1) % len(image_paths)
    showImage(cIndex)

def preview_first():
    if image_paths == True:
        os.startfile(image_paths[0])

window.bind("<Left>", prevImg)
window.bind("<Right>", nextImg)

title = ttk.Label(window, text = "PolyGenix", font = ("Agency FB Bold", 35))
title.place(x = 140, y = 30)

subTitle = ttk.Label(
    window, text = "Idea Generation Engine for 3D Printable Design", font = ("Agency FB", 15)
)
subTitle.place(x = 110, y = 89)

# Radiobutton:
rb = StringVar(value = "choices")

rad1 = ttk.Radiobutton(window,text = "Short [5 variants]", value = "Choice5", variable = rb)
rad1.place(x = 110, y = 135)

rad2 = ttk.Radiobutton(window, text = "Extended [15 variants]", value = "Choice15", variable = rb)
rad2.place(x = 260, y = 135)

text_widget = ttk.Entry(window, width = 35, font = ("Segue UI", 15))
text_widget.place(x = 50, y = 200)

enter_button = ttk.Button(window, text = "Create", command = process)
enter_button.place(x = 310, y = 290, height = 40, width = 140)

preview_button = ttk.Button(window, text = "Preview", command = preview_first)
preview_button.place(x = 50, y = 290, height = 40, width = 140)

image_label = ttk.Label(window)
image_label.place(x = 50, y = 330, height = 400, width = 400)

window.mainloop()