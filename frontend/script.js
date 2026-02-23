const fileInput = document.getElementById("fileInput");
const uploadArea = document.getElementById("uploadArea");
const previewContainer = document.getElementById("previewContainer");
const imagePreview = document.getElementById("imagePreview");
const form = document.getElementById("uploadForm");

const initialState = document.getElementById("initialState");
const loadingState = document.getElementById("loadingState");
const resultContainer = document.getElementById("resultContainer");

const diseaseName = document.getElementById("diseaseName");
const confidenceScore = document.getElementById("confidenceScore");
const descriptionText = document.getElementById("descriptionText");

// Click upload area
uploadArea.addEventListener("click", () => fileInput.click());

// Preview image
fileInput.addEventListener("change", () => {
    const file = fileInput.files[0];
    if (!file) return;

    imagePreview.src = URL.createObjectURL(file);
    previewContainer.classList.remove("hidden");
});

// FORM SUBMIT (IMPORTANT FIX)
form.addEventListener("submit", async (e) => {
    e.preventDefault();

    initialState.classList.add("hidden");
    resultContainer.classList.add("hidden");
    loadingState.classList.remove("hidden");

    const formData = new FormData(form);

    try {
        const response = await fetch("http://127.0.0.1:5000/analyze", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        diseaseName.textContent = data.AI_Analysis.disease;
        confidenceScore.textContent = data.AI_Analysis.confidence + "%";
        descriptionText.textContent = data.Treatment_Recommendation;

        loadingState.classList.add("hidden");
        resultContainer.classList.remove("hidden");

    } catch (err) {
        alert("Backend not reachable");
        loadingState.classList.add("hidden");
    }
});