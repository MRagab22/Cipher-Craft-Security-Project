# CipherCraft Website

## Overview

CipherCraft Website is a web-based application designed to perform encryption and decryption using classical cryptographic algorithms. It provides an intuitive and interactive interface supported by a FastAPI backend, making it ideal for both educational and practical use in learning about cryptography.
The project includes six classical cipher techniques: **Caesar, Monoalphabetic, Playfair, Transposition, Vigenère,** and **Rail Fence.**

---

## Features

### 1. Cryptographic Algorithms

* **Caesar Cipher:** Shifts letters by a fixed number of positions.
* **Monoalphabetic Cipher:** Substitutes letters using a custom 26-letter key.
* **Playfair Cipher:** Encrypts letter pairs using a 5×5 matrix grid.
* **Transposition Cipher:** Rearranges letters according to a numeric key.
* **Vigenère Cipher:** Uses a keyword for polyalphabetic substitution.
* **Rail Fence Cipher:** Writes text in a zigzag pattern across multiple rails.

### 2. User Interface

* Tabbed navigation for **Tool**, **Tutorial**, and **Guide** sections.
* Responsive layout with **Light/Dark Mode** (saved in `localStorage`).
* Ready-to-use example panel for quick testing.
* Step-by-step explanation toggle for detailed encryption visualization.
* **Save Result** feature to download results as `.txt` files.

### 3. Interactivity

* Dynamic input fields that adjust based on the selected algorithm.
* Real-time validation (e.g., ensuring unique 26-letter keys for Monoalphabetic).
* Smooth animations and hover effects for an enhanced user experience.

### 4. Accessibility

* Clear error messages for incorrect or invalid input.
* Mobile-friendly design with adaptive icons and layout scaling.

---

## System Requirements

* **Browser:** Chrome, Firefox, Safari, or Edge
* **Backend:** Python 3.8 or higher
* **Internet:** Optional (for Font Awesome and Google Fonts)

---

## Usage

### 1. Run the Application

Before using the website, start the backend server by running the following command in your terminal from the project root directory:

```bash
python main.py
```

This command starts the FastAPI server with **Uvicorn**.
Once the server is running, open your browser and navigate to:

```
http://localhost:8000
```

You should now see the CipherCraft Website homepage with the **Tool** tab active.

---

### 2. Encrypting or Decrypting Text

1. Select **Encrypt** or **Decrypt**.
2. Choose one of the six cipher algorithms.
3. Enter the text you want to process.
4. Provide the corresponding key (e.g., shift = 3 for Caesar).
5. (Optional) Enable **Show step-by-step explanation** for a detailed process.
6. Click **Submit** to run encryption/decryption.
7. Click **Save Result** to download the output.

---

### 3. Exploring Examples

* Select a predefined example (e.g., Monoalphabetic Cipher).
* Click **Copy** to auto-fill the fields.
* Click **Submit** to view the result.

---

### 4. Switching Tabs

* **Tool:** Main encryption/decryption workspace.
* **Tutorial:** Detailed explanation of each cipher’s logic.
* **Guide:** Step-by-step guide and helpful resources.

---

### 5. Dark Mode

* Click the sun/moon icon in the top-right corner to toggle between themes.
* Your selected mode is stored in `localStorage` for persistence.

---

## Technical Details

### Frontend

* **HTML:** `index.html` defines layout and navigation structure.
* **CSS:** `style.css` manages responsive design, colors, and animations.
* **JavaScript:** `script.js` handles input validation, tab switching, Fetch API requests, and saving output.

### Backend

* **Framework:** FastAPI (`main.py`)
* **Endpoints:**

  * `GET /` – Serves the main website.
  * `POST /process` – Handles encryption/decryption logic.
* **Ciphers:** Implemented in Python with input validation and exception handling.

### Dependencies

* **Frontend:**

  * Font Awesome (icons)
  * Google Fonts (Poppins)
* **Backend:**

  * `fastapi` – Web framework
  * `uvicorn` – ASGI server
  * `jinja2` – Template rendering

---

## Example Usage

**Scenario:** Encrypt text using Monoalphabetic Cipher

* **Inputs:**

  * Operation: Encrypt
  * Algorithm: Monoalphabetic Cipher
  * Text: `if we wish to buy a car`
  * Key: `DKVQFIBJWPESCXHTMYAUOLRGNZ`

* **Output:** `WIGFGWJOHKLZDVDA`

---

## Resources

* [Wikipedia: Cryptography](https://en.wikipedia.org/wiki/Cryptography)
* [Khan Academy: Cryptography](https://www.khanacademy.org/computing/computer-science/cryptography)
* [FastAPI Documentation](https://fastapi.tiangolo.com)
* [Font Awesome](https://fontawesome.com)
* [Google Fonts](https://fonts.google.com)

