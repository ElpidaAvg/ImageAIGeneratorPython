# ImageAIGeneratorPython

PolyGenix is a desktop AI-powered idea and image generation tool built with Tkinter.  
It generates creative 3D-printable design prompts and automatically produces AI-generated preview images.

---

## 🖼️ Application Preview

<p align="center">
<img width="542" height="872" alt="Print Screen" src="https://github.com/user-attachments/assets/e1a818b7-f0f3-43b0-b2bc-6e987cb5afd8" />
</p>

---

## 🚀 Features

- 🎨 AI prompt generation based on user input
- 🖼️ Automatic AI image generation (1024x1024)
- 📂 Saves generated images locally
- ⬅️➡️ Navigate between generated images
- 🌙 Modern dark UI using ttkthemes (Equilux)
- 🧠 Designed for 3D printable concept ideation

---

## 🛠 Technologies Used

- Python
- Tkinter / ttk
- ttkthemes
- Pillow (PIL)
- OpenAI API (Chat + Image generation)
- Base64 & OS modules

---

## 📦 Installation

1. Clone the repository:

   git clone https://github.com/yourusername/polygenix.git
   cd polygenix

2. Install dependencies:

   pip install openai pillow ttkthemes

3. Add your OpenAI API key inside the script:

   client = openai.OpenAI(api_key="YOUR_API_KEY")

4. Run the application:

   python main.py

---

## 🧩 How It Works

1. Enter a design idea in the input field.
2. Choose the number of prompt variations.
3. Click Create.
4. The app:
   - Generates AI prompts
   - Creates images from those prompts
   - Saves them inside the outputs/ folder
5. Use arrow keys to browse the results.

---

## 📁 Project Structure

PolyGenix/
│
├── main.py
├── outputs/
└── README.md

---

## ⚠️ Important

Never upload your real OpenAI API key to GitHub.  
Use environment variables instead for production use.

---

## 📌 Future Improvements

- Add loading animation
- Add image export options
- Add prompt history
- Improve UI responsiveness
- Add settings panel

---

## 📜 License

MIT License

---

Made using Python and OpenAI.
