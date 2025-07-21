# 🧠 Image Recognition

This is a basic image recognition/classification project using Python. It allows you to upload an image, compare it with a set of predefined images, and return matches or classifications using logic in `vision_match.py`.

---

## 🚀 Features

- Upload an image and compare it to existing ones
- Use pre-defined labels for identification
- Lightweight and easy to run locally
- Custom vision matching algorithm or external API support

---

## 🔧 Prerequisites

Make sure you have:

- Python 3.8 or higher
- Git installed
- pip installed

---

## 🛠️ Setup Instructions

### 1. **Clone the repository**

```bash
git clone https://github.com/<your-username>/image-recognition.git
cd image-recognition
```

> Replace `<your-username>` with your GitHub username.

---

### 2. **Create a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

---

### 3. **Install dependencies**

```bash
pip install --upgrade pip
pip install flask pillow
```

If you want to save the dependencies:

```bash
pip freeze > requirements.txt
```

---

### 4. **Add your credentials**

Create a `key.json` file (for APIs like Google Vision, etc.). This is ignored by git and should **not** be committed.

---

### 5. **Run the app**

```bash
python app.py
```

Visit: [http://localhost:5000](http://localhost:5000)

---

### 6. **Test the image recognition**

- Upload an image using the web interface (if built), or
- Use `test_image.jpg` to test locally via code

---

## 📁 Project Structure

```
Image Recognition/
├── app.py                  # Main app file
├── vision_match.py         # Image comparison logic
├── labels.json             # Class/label mappings
├── key.json                # API key (ignored in git)
├── test_image.jpg          # Sample test image
├── images/                 # Image dataset
├── uploads/                # Uploaded/processed images
├── venv/                   # Python virtual environment
└── __pycache__/            # Compiled Python cache
```

---

## 🧪 Example usage

Test with CURL:

```bash
curl -X POST -F "image=@test_image.jpg" http://localhost:5000/upload
```

Or use the form via the browser.

---

## ✅ .gitignore

Here’s the recommended `.gitignore`:

```gitignore
# Bytecode
__pycache__/
*.py[cod]

# Virtual environment
venv/

# Secrets
key.json

# Runtime files
uploads/
images/
test_image.jpg

# OS and editor files
.DS_Store
.vscode/
.idea/
```

---

## 🐛 Troubleshooting

| Issue | Fix |
|-------|-----|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| Permission denied | Use `sudo`, or check folder permissions |
| Flask not starting | Ensure you're in virtualenv and Flask is installed |
| API key error | Check if `key.json` exists and is valid |

---

## 🙌 Contributing

Feel free to fork this repo, create pull requests, or open issues for enhancements and bug fixes.

---

## 📄 License

This project is licensed under the MIT License.
