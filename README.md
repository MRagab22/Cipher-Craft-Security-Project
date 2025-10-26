# CipherCraft Website

**CipherCraft Dashboard** is a web-based application designed to perform **encryption and decryption** using various classical cryptographic algorithms.
It provides an educational and interactive platform to understand and apply cipher techniques with a clean user interface and powerful backend.

---

## 🔹 Live Demo

> *(If hosted locally, open `http://localhost:8000` after running the app)*

---

## 1. Overview

CipherCraft is both a **learning tool** and a **practical encryption utility**.
It allows users to experiment with different ciphers, observe how algorithms work, and save the encrypted or decrypted results.

The project supports **six classical ciphers**:

1. **Caesar Cipher** – Shifts letters by a fixed number of positions.
2. **Monoalphabetic Cipher** – Substitutes letters using a 26-letter key.
3. **Playfair Cipher** – Encrypts pairs of letters using a 5x5 matrix.
4. **Transposition Cipher** – Rearranges letters based on a numeric key.
5. **Vigenère Cipher** – Uses a keyword for polyalphabetic substitution.
6. **Rail Fence Cipher** – Writes text in a zigzag pattern across rails.

---

## 2. Features

### 2.1 Cryptographic Algorithms

* Six supported ciphers with different key parameters.
* Step-by-step explanations available for each encryption or decryption process.
* Downloadable results as `.txt` files.

### 2.2 User Interface

* Tabbed navigation for **Tool**, **Tutorial**, and **Guide** sections.
* Responsive layout with **light and dark modes** (saved via localStorage).
* Example panel for instant testing.

### 2.3 Interactivity

* Dynamic parameter inputs depending on the selected cipher.
* Real-time validation for keys and text.
* Smooth animations and hover effects.

### 2.4 Accessibility

* Clear error messages for invalid input.
* Fully mobile-friendly layout.

---

## 3. System Requirements

* **Browser:** Chrome, Firefox, Edge, or Safari (latest versions).
* **Backend:** Python 3.8+
* **Internet (Optional):** For Font Awesome and Google Fonts.

---

## 4. Usage Guide

### 4.1 Accessing the Dashboard

1. Run the FastAPI backend.
2. Open [http://localhost:8000](http://localhost:8000) in your browser.
3. The **Tool** tab will appear by default.

### 4.2 Encrypting / Decrypting Text

1. Select **Operation:** Encrypt or Decrypt.
2. Choose **Algorithm:** one of the six ciphers.
3. Enter the **text** to process.
4. Enter the **key or parameter** required (e.g., numeric shift or alphabet key).
5. Optionally, check **Show step-by-step explanation**.
6. Click **Submit** to process the text.
7. Use **Save Result** to download the output as `ciphercraft_result.txt`.

### 4.3 Exploring Examples

* Choose a predefined example from the sidebar.
* Click **Copy** to autofill the form fields.

### 4.4 Switching Tabs

* **Tool:** Encryption/Decryption interface.
* **Tutorial:** Explains each algorithm.
* **Guide:** Extra documentation and resources.

### 4.5 Dark Mode

* Click the moon/sun icon in the top-right corner.
* Theme preference is stored in localStorage for persistence.

---

## 5. Technical Details

### 5.1 Frontend

* **HTML (index.html):** Structure with tabs, inputs, and examples panel.
* **CSS (style.css):** Responsive design using Poppins font and animations.
* **JavaScript (script.js):**

  * Handles dynamic fields, validation, tab switching, Fetch API requests, and saving results.

### 5.2 Backend

* **Framework:** FastAPI
* **Endpoints:**

  * `GET /` → Serves main page.
  * `POST /process` → Performs encryption/decryption.
* **Ciphers:** Implemented in Python with validation and error handling.

### 5.3 Dependencies

* **Frontend:**

  * Font Awesome (icons)
  * Google Fonts (Poppins)
* **Python:**

  * `fastapi` – Web framework
  * `uvicorn` – ASGI server
  * `jinja2` – Template rendering

---

## 6. Example Usage

**Scenario:** Encrypt text using the Monoalphabetic Cipher.

| Step | Action                                                             |
| ---- | ------------------------------------------------------------------ |
| 1    | Select *Encrypt* and *Monoalphabetic Cipher*                       |
| 2    | Enter text: `if we wish to buy a car`                              |
| 3    | Enter key: `DKVQFIBJWPESCXHTMYAUOLRGNZ`                            |
| 4    | Click *Submit*                                                     |
| 5    | Output: `WIGFGWJOHKLZDVDA`                                         |
| 6    | Optionally enable *Show step-by-step explanation* or *Save Result* |

---

## 7. Resources

* **Cryptography Basics:**

  * [Wikipedia: Cryptography](https://en.wikipedia.org/wiki/Cryptography)
  * [Khan Academy: Cryptography](https://www.khanacademy.org/computing/computer-science/cryptography)
* **FastAPI Documentation:** [fastapi.tiangolo.com](https://fastapi.tiangolo.com)
* **Font Awesome:** [fontawesome.com](https://fontawesome.com)
* **Google Fonts:** [fonts.google.com](https://fonts.google.com)
