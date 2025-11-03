# CipherCraft Website

## 🔐 Overview
CipherCraft Website is a web-based application designed to perform encryption and decryption using classical cryptographic algorithms. It provides an intuitive and interactive interface supported by a FastAPI backend, making it ideal for both educational and practical use in learning about cryptography.

The project includes six classical cipher techniques: **Caesar, Monoalphabetic, Playfair, Transposition, Vigenère,** and **Rail Fence.**

---

## ✨ Features

### 1. Cryptographic Algorithms
* **Caesar Cipher:** Shifts letters by a fixed number of positions
* **Monoalphabetic Cipher:** Substitutes letters using a custom 26-letter key
* **Playfair Cipher:** Encrypts letter pairs using a 5×5 matrix grid
* **Transposition Cipher:** Rearranges letters according to a numeric key
* **Vigenère Cipher:** Uses a keyword for polyalphabetic substitution
* **Rail Fence Cipher:** Writes text in a zigzag pattern across multiple rails

### 2. User Interface
* Tabbed navigation for **Tool**, **Tutorial**, and **Guide** sections
* Responsive layout with **Light/Dark Mode** (saved in `localStorage`)
* Ready-to-use example panel for quick testing
* Step-by-step explanation toggle for detailed encryption visualization
* **Save Result** feature to download results as `.txt` files

### 3. Interactivity
* Dynamic input fields that adjust based on the selected algorithm
* Real-time validation (e.g., ensuring unique 26-letter keys for Monoalphabetic)
* Smooth animations and hover effects for an enhanced user experience

### 4. Accessibility
* Clear error messages for incorrect or invalid input
* Mobile-friendly design with adaptive icons and layout scaling

---

## 🛠️ Technologies Used

### Frontend
| Technology | Purpose |
|------------|---------|
| **HTML** | Layout and navigation structure |
| **CSS** | Responsive design, colors, and animations |
| **JavaScript** | Input validation, tab switching, and API requests |
| **Font Awesome** | Icons |
| **Google Fonts** | Poppins typography |

### Backend
| Technology | Purpose |
|------------|---------|
| **Python** | Main programming language |
| **FastAPI** | Web framework |
| **Uvicorn** | ASGI server |
| **Jinja2** | Template rendering |

---

## ⚙️ System Requirements
* **Browser:** Chrome, Firefox, Safari, or Edge
* **Python:** 3.8 or higher
* **Internet:** Optional (for Font Awesome and Google Fonts)

---

## 📥 Installation & Setup

### 1. Clone the repository
```bash
git clone <repository-url>
cd CipherCraft-Website
```

### 2. Install dependencies
```bash
pip install fastapi uvicorn jinja2
```

### 3. Run the application
```bash
python main.py
```

### 4. Access the website
Open your browser and navigate to:
```
http://localhost:8000
```

---

## 🚀 Usage Guide

### Encrypting or Decrypting Text
1. Select **Encrypt** or **Decrypt**
2. Choose one of the six cipher algorithms
3. Enter the text you want to process
4. Provide the corresponding key (e.g., shift = 3 for Caesar)
5. (Optional) Enable **Show step-by-step explanation** for detailed process
6. Click **Submit** to run encryption/decryption
7. Click **Save Result** to download the output

### Exploring Examples
* Select a predefined example (e.g., Monoalphabetic Cipher)
* Click **Copy** to auto-fill the fields
* Click **Submit** to view the result

### Switching Tabs
* **Tool:** Main encryption/decryption workspace
* **Tutorial:** Detailed explanation of each cipher's logic
* **Guide:** Step-by-step guide and helpful resources

### Dark Mode
* Click the sun/moon icon in the top-right corner to toggle between themes
* Your selected mode is stored in `localStorage` for persistence

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Serves the main website |
| POST | `/process` | Handles encryption/decryption logic |

---

## 💡 Example Usage

**Scenario:** Encrypt text using Monoalphabetic Cipher

**Inputs:**
* Operation: Encrypt
* Algorithm: Monoalphabetic Cipher
* Text: `if we wish to buy a car`
* Key: `DKVQFIBJWPESCXHTMYAUOLRGNZ`

**Output:** `WIGFGWJOHKLZDVDA`

---

## 📚 Resources
* [Wikipedia: Cryptography](https://en.wikipedia.org/wiki/Cryptography)
* [Khan Academy: Cryptography](https://www.khanacademy.org/computing/computer-science/cryptography)
* [FastAPI Documentation](https://fastapi.tiangolo.com)
* [Font Awesome](https://fontawesome.com)
* [Google Fonts](https://fonts.google.com)

---

## 👨‍💻 Author
**[MRagab22](https://github.com/MRagab22)**

---

> 🔒 *Educational cryptography tool demonstrating classical encryption algorithms with an interactive web interface.*
