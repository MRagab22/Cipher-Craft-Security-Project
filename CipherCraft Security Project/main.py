from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import threading
import webbrowser
import uvicorn

app = FastAPI()

# Templates & static
templates = Jinja2Templates(directory=".")
app.mount("/static", StaticFiles(directory="."), name="static")

# ===================================================
# 1. Caesar Cipher
# ===================================================
def caesar_cipher(text: str, shift: int) -> str:
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result.upper()

def caesar_decipher(text: str, shift: int) -> str:
    return caesar_cipher(text, -shift).upper()

# ===================================================
# 2. Monoalphabetic Substitution
# ===================================================
def validate_mono_key(key: str) -> tuple[bool, str]:
    clean_key = ''.join(c for c in key.lower() if c.isalpha())
    if len(clean_key) != 26:
        return False, "Key must be exactly 26 letters."
    if len(set(clean_key)) != 26:
        return False, "Key must contain 26 unique letters."
    return True, clean_key

def monoalphabetic_cipher(text: str, key: str) -> str:
    is_valid, clean_key = validate_mono_key(key)
    if not is_valid:
        return clean_key.upper()  # Error message
    alpha = "abcdefghijklmnopqrstuvwxyz"
    mapping = {alpha[i]: clean_key[i] for i in range(26)}
    res = ""
    for ch in text:
        if ch.isalpha():
            mapped = mapping[ch.lower()]
            res += mapped.upper() if ch.isupper() else mapped
        else:
            res += ch
    return res.upper()

def monoalphabetic_decipher(text: str, key: str) -> str:
    is_valid, clean_key = validate_mono_key(key)
    if not is_valid:
        return clean_key.upper()  # Error message
    alpha = "abcdefghijklmnopqrstuvwxyz"
    inv = {clean_key[i]: alpha[i] for i in range(26)}
    res = ""
    for ch in text:
        if ch.isalpha():
            orig = inv[ch.lower()]
            res += orig.upper() if ch.isupper() else orig
        else:
            res += ch
    return res.upper()

# ===================================================
# 3. Playfair Cipher
# ===================================================
def _playfair_table(key: str):
    table_str = ""
    for c in key.lower().replace('j', 'i'):
        if c.isalpha() and c not in table_str:
            table_str += c
    for c in "abcdefghijklmnopqrstuvwxyz":
        if c == 'j': continue
        if c not in table_str:
            table_str += c
    return [list(table_str[i:i+5]) for i in range(0, 25, 5)]

def _find_pos(c: str, table):
    for r, row in enumerate(table):
        if c in row:
            return r, row.index(c)
    return None

def playfair_cipher(text: str, key: str) -> str:
    T = _playfair_table(key)
    clean = ''.join([c.lower() for c in text if c.isalpha()]).replace('j', 'i')
    digrams = []
    i = 0
    while i < len(clean):
        a = clean[i]
        b = clean[i+1] if i+1 < len(clean) else 'x'
        if a == b:
            b = 'x'
            i += 1
        else:
            i += 2
        digrams.append((a, b))
    out = ""
    for a, b in digrams:
        r1, c1 = _find_pos(a, T)
        r2, c2 = _find_pos(b, T)
        if r1 == r2:
            out += T[r1][(c1+1)%5] + T[r2][(c2+1)%5]
        elif c1 == c2:
            out += T[(r1+1)%5][c1] + T[(r2+1)%5][c2]
        else:
            out += T[r1][c2] + T[r2][c1]
    return out.upper()

def playfair_decipher(text: str, key: str) -> str:
    T = _playfair_table(key)
    clean = ''.join([c.lower() for c in text if c.isalpha()]).replace('j', 'i')
    pairs = [clean[i:i+2] for i in range(0, len(clean), 2)]
    out = ""
    for pair in pairs:
        a, b = pair[0], pair[1]
        r1, c1 = _find_pos(a, T)
        r2, c2 = _find_pos(b, T)
        if r1 == r2:
            out += T[r1][(c1-1)%5] + T[r2][(c2-1)%5]
        elif c1 == c2:
            out += T[(r1-1)%5][c1] + T[(r2-1)%5][c2]
        else:
            out += T[r1][c2] + T[r2][c1]
    return out.upper()

# ===================================================
# 4. Columnar Transposition Cipher
# ===================================================
def transposition_cipher(text: str, key: str) -> str:
    try:
        k = [int(x) for x in key.split()]
    except ValueError:
        return "Invalid key format. Use space-separated numbers.".upper()
    n = len(k)
    if sorted(k) != list(range(1, n+1)):
        return f"Invalid key: must be a permutation of 1..{n}.".upper()
    s = ''.join(text.split())
    rows = (len(s) + n - 1)//n
    padded = s.ljust(rows*n, 'x')
    M = [padded[i*n:(i+1)*n] for i in range(rows)]
    order = [idx for _, idx in sorted((val, idx) for idx, val in enumerate(k))]
    raw = ''.join(M[r][c] for c in order for r in range(rows))
    return ' '.join(raw.upper()[i:i+5] for i in range(0, len(raw), 5))

def transposition_decipher(text: str, key: str) -> str:
    s = ''.join(text.split())
    try:
        k = [int(x) for x in key.split()]
    except ValueError:
        return "Invalid key format. Use space-separated numbers.".upper()
    n = len(k)
    if sorted(k) != list(range(1, n+1)):
        return f"Invalid key: must be a permutation of 1..{n}.".upper()
    rows = len(s)//n
    M = [['']*n for _ in range(rows)]
    order = [idx for _, idx in sorted((val, idx) for idx, val in enumerate(k))]
    i = 0
    for c in order:
        for r in range(rows):
            M[r][c] = s[i]
            i += 1
    return ''.join(''.join(row) for row in M).rstrip('x').upper()

# ===================================================
# 5. Vigenère Cipher
# ===================================================
def vigenere_cipher(text: str, key: str) -> str:
    res = ""
    key = key.lower()
    j = 0
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = ord(key[j % len(key)]) - ord('a')
            res += chr((ord(ch) - base + shift) % 26 + base)
            j += 1
        else:
            res += ch
    return res.upper()

def vigenere_decipher(text: str, key: str) -> str:
    res = ""
    key = key.lower()
    j = 0
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = ord(key[j % len(key)]) - ord('a')
            res += chr((ord(ch) - base - shift) % 26 + base)
            j += 1
        else:
            res += ch
    return res.upper()

# ===================================================
# 6. Rail Fence Cipher
# ===================================================
def rail_fence_cipher(text: str, rails: int) -> str:
    s = ''.join(text.split())
    if rails < 2 or rails >= len(s):
        return s.upper()
    fence = [''] * rails
    idx, down = 0, True
    for ch in s:
        fence[idx] += ch
        if idx == 0:
            down = True
        elif idx == rails - 1:
            down = False
        idx += 1 if down else -1
    return ''.join(fence).upper()

def rail_fence_decipher(text: str, rails: int) -> str:
    if rails < 2 or rails >= len(text):
        return text.upper()
    pattern, idx, down = [], 0, True
    for _ in text:
        pattern.append(idx)
        if idx == 0:
            down = True
        elif idx == rails - 1:
            down = False
        idx += 1 if down else -1
    counts = [pattern.count(r) for r in range(rails)]
    segments, i = [], 0
    for cnt in counts:
        segments.append(list(text[i:i+cnt]))
        i += cnt
    out = ""
    for r in pattern:
        out += segments[r].pop(0)
    return out.upper()

# ===================================================
# Routes
# ===================================================
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/documentation", response_class=HTMLResponse)
async def documentation(request: Request):
    return templates.TemplateResponse("documentation.html", {"request": request})

@app.post("/process")
async def process(
    operation: str = Form(...),
    algorithm: str = Form(...),
    text: str = Form(...),
    param: str = Form("")
):
    try:
        if operation == "encrypt":
            if algorithm == "caesar":
                shift = int(param)
                result = caesar_cipher(text, shift)
            elif algorithm == "monoalphabetic":
                result = monoalphabetic_cipher(text, param)
            elif algorithm == "playfair":
                result = playfair_cipher(text, param)
            elif algorithm == "transposition":
                result = transposition_cipher(text, param)
            elif algorithm == "vigenere":
                result = vigenere_cipher(text, param)
            elif algorithm == "railfence":
                rails = int(param)
                result = rail_fence_cipher(text, rails)
            else:
                result = "Unknown algorithm"
        elif operation == "decrypt":
            if algorithm == "caesar":
                shift = int(param)
                result = caesar_decipher(text, shift)
            elif algorithm == "monoalphabetic":
                result = monoalphabetic_decipher(text, param)
            elif algorithm == "playfair":
                result = playfair_decipher(text, param)
            elif algorithm == "transposition":
                result = transposition_decipher(text, param)
            elif algorithm == "vigenere":
                result = vigenere_decipher(text, param)
            elif algorithm == "railfence":
                rails = int(param)
                result = rail_fence_decipher(text, rails)
            else:
                result = "Unknown algorithm"
        else:
            result = "Invalid operation"
    except ValueError as e:
        result = f"Error: Invalid parameter format - {str(e)}".upper()
    except Exception as e:
        result = f"Error: {str(e)}".upper()
    return JSONResponse(content={"result": result})

# ===================================================
# Auto-launch server
# ===================================================
if __name__ == "__main__":
    threading.Timer(1, lambda: webbrowser.open("http://localhost:8000")).start()
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)