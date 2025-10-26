document.addEventListener("DOMContentLoaded", () => {
  const algorithmSelect = document.getElementById("algorithm");
  const paramContainer = document.getElementById("param-container");
  const paramLabel = document.getElementById("param-label");
  const paramInput = document.getElementById("param");
  const paramError = document.getElementById("param-error");
  const darkModeToggle = document.getElementById("darkModeToggle");
  const saveResultBtn = document.getElementById("saveResult");
  const showStepsCb = document.getElementById("showSteps");
  const stepsContainer = document.getElementById("stepsContainer");
  const stepsList = document.getElementById("stepsList");
  const hideStepsBtn = document.getElementById("hideSteps");
  const tabButtons = document.querySelectorAll(".tab-btn");
  const tabContents = document.querySelectorAll(".tab-content");
  const form = document.getElementById("cryptoForm");
  const resultDiv = document.getElementById("result");
  const textInput = document.getElementById("text");
  const examplesToggle = document.getElementById("examplesToggle");
  const examplesPanel = document.getElementById("examplesPanel");
  const closeExamples = document.getElementById("closeExamples");
  const copyExampleButtons = document.querySelectorAll(".copy-example-btn");

  // 1. Dynamic parameter field with validation
  function updateParamField() {
    const algo = algorithmSelect.value;
    paramContainer.style.display = "block";
    paramError.style.display = "none";
    paramInput.value = "";
    switch (algo) {
      case "caesar":
        paramLabel.textContent = "Enter Shift (for Caesar):";
        paramInput.placeholder = "e.g., 3";
        paramInput.type = "number";
        break;
      case "monoalphabetic":
        paramLabel.textContent = "Enter Key (26 unique letters):";
        paramInput.placeholder = "e.g., QWERTYUIOPASDFGHJKLZXCVBNM";
        paramInput.type = "text";
        break;
      case "playfair":
      case "vigenere":
        paramLabel.textContent = "Enter Key:";
        paramInput.placeholder = "e.g., SECRET";
        paramInput.type = "text";
        break;
      case "transposition":
        paramLabel.textContent = "Enter column order key (space-separated):";
        paramInput.placeholder = "e.g., 5 4 2 3 1 7 6";
        paramInput.type = "text";
        break;
      case "railfence":
        paramLabel.textContent = "Enter Number of Rails:";
        paramInput.placeholder = "e.g., 3";
        paramInput.type = "number";
        break;
      default:
        paramContainer.style.display = "none";
    }
  }

  // Validate Monoalphabetic key
  function validateMonoKey(key) {
    const cleanKey = key.toLowerCase().replace(/[^a-z]/g, '');
    if (cleanKey.length !== 26) {
      return `Key must be exactly 26 letters (provided ${cleanKey.length} letters).`;
    }
    const uniqueLetters = new Set(cleanKey);
    if (uniqueLetters.size !== 26) {
      return "Key must contain 26 unique letters (no duplicates).";
    }
    return "";
  }

  algorithmSelect.addEventListener("change", updateParamField);
  updateParamField();

  // 2. Dark-mode persistence
  if (localStorage.getItem("darkMode") === "true") {
    document.body.classList.add("dark");
    darkModeToggle.innerHTML = '<i class="fas fa-sun"></i>';
  }
  darkModeToggle.addEventListener("click", () => {
    const isDark = document.body.classList.toggle("dark");
    darkModeToggle.innerHTML = isDark
      ? '<i class="fas fa-sun"></i>'
      : '<i class="fas fa-moon"></i>';
    localStorage.setItem("darkMode", isDark);
  });

  // 3. Tab navigation
  tabButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      tabButtons.forEach(b => b.classList.remove("active"));
      tabContents.forEach(c => c.classList.remove("active"));
      btn.classList.add("active");
      document.getElementById(btn.dataset.tab).classList.add("active");
    });
  });

  // 4. Form submission with validation
  form.addEventListener("submit", async e => {
    e.preventDefault();
    paramError.style.display = "none";

    // Client-side validation for Monoalphabetic
    if (algorithmSelect.value === "monoalphabetic") {
      const error = validateMonoKey(paramInput.value);
      if (error) {
        paramError.textContent = error;
        paramError.style.display = "block";
        return;
      }
    }

    const formData = new FormData(form);
    try {
      const res = await fetch(form.action, { method: form.method, body: formData });
      const data = await res.json();
      resultDiv.style.opacity = 0;

      if (showStepsCb.checked) {
        stepsList.innerHTML = "";
        stepsContainer.style.display = "block";
        const steps = [
          "Step 1: Received input text.",
          `Step 2: Operation – ${formData.get("operation")} with ${formData.get("algorithm")}.`,
          "Step 3: Processing algorithm…",
          "Step 4: Generating final result…"
        ];
        let i = 0;
        (function next() {
          if (i < steps.length) {
            const li = document.createElement("li");
            li.textContent = steps[i++];
            stepsList.appendChild(li);
            setTimeout(next, 800);
          } else {
            resultDiv.textContent = data.result; // Backend already returns uppercase
            resultDiv.style.opacity = 1;
          }
        })();
      } else {
        stepsContainer.style.display = "none";
        resultDiv.textContent = data.result; // Backend already returns uppercase
        setTimeout(() => resultDiv.style.opacity = 1, 100);
      }
    } catch (error) {
      resultDiv.textContent = "ERROR: FAILED TO PROCESS REQUEST.";
      resultDiv.style.opacity = 1;
    }
  });

  hideStepsBtn.addEventListener("click", () => {
    stepsContainer.style.display = "none";
  });

  // 5. Save result
  saveResultBtn.addEventListener("click", () => {
    const txt = resultDiv.textContent.trim();
    if (!txt) return alert("No result to save!");
    const blob = new Blob([txt], { type: "text/plain;charset=utf-8" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "ciphercraft_result.txt";
    a.click();
  });

  // 6. Examples panel toggle
  examplesToggle.addEventListener("click", () => {
    examplesPanel.classList.toggle("open");
  });

  closeExamples.addEventListener("click", () => {
    examplesPanel.classList.remove("open");
  });

  // 7. Copy example to form
  copyExampleButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      const algo = btn.dataset.algo;
      const text = btn.dataset.text;
      const param = btn.dataset.param;

      algorithmSelect.value = algo;
      updateParamField();
      textInput.value = text;
      if (param) {
        paramInput.value = param;
      } else {
        paramInput.value = algo === "caesar" || algo === "railfence" ? "3" : "";
      }
      examplesPanel.classList.remove("open");
    });
  });
});