# 🌐 Aryan Kumar Saha - Portfolio Website

Interactive portfolio website for **Aryan Kumar Saha**, AI/ML & Computer Vision Engineer deploying real-time production systems at **Maruti Suzuki India Limited (MSIL)**. Built with **FastAPI, Jinja2, and Vanilla CSS** with an interactive **Role/Persona Switcher**.

🔗 **Live Deployment:** [https://aryankumarsaha-porfolia.vercel.app](https://aryankumarsaha-porfolia.vercel.app)

---

## 🚀 Key Highlights & New Updates

- 🏭 **Industrial Experience Added:** Computer Vision Ops Intern / Engineer at **Eternal Robotics deployed on-site at Maruti Suzuki India Limited (MSIL)** in Gurugram, building inspection pipelines across **100+ checkpoints** and tuning **50+ models**.
- 🧠 **GenAI & VLM Internship:** AI/ML Intern at **Infutrix Technologies**, fine-tuning **Qwen-VL models** for noisy OCR and two-stage YOLO + VLM processing across 1,000+ answer sheets.
- 🛠️ **Flagship Project:** **CV Workbench** — Local-first computer vision & MLOps platform (active learning, Laplacian blur & dHash/aHash curation, PyTorch CUDA training with live SSE streaming, ONNX/TensorRT edge export).
- 🎨 **Dynamic Persona Switcher:** Allows recruiters to toggle dynamically between:
  - **Computer Vision & AI** (YOLO, PyTorch, CUDA, TensorRT, 15+ live systems)
  - **Data Scientist & GenAI** (VLMs, Qwen, DistilBERT NLP, predictive modeling)
  - **Data Analytics & MLOps** (Production logs across 100+ checkpoints, SQL, Streamlit, BI)
- 📄 **Embedded & Downloadable Resume:** Up-to-date resume (`Aryan_Kumar_Saha_Resume.pdf`) with one-click viewing and download.
- 🎓 **Academic & Leadership Record:** IIIT Tiruchirappalli (CGPA: 8.14), 400+ DSA problems solved, E-Cell Sub-Coordinator & Campus Executive (IIT Bombay).

---

## 🛠️ Tech Stack

- **Backend:** FastAPI, Pydantic, Python 3
- **Frontend & Styling:** HTML5, Modern Vanilla CSS (Glassmorphism, CSS Custom Properties, Responsive Grid & Flexbox)
- **Templating Engine:** Jinja2
- **Deployment:** Vercel / Render
- **Version Control:** Git & GitHub

---

## 📁 Project Structure

```
portfolio_website/
├── static/
│   ├── Aryan_Kumar_Saha_Resume.pdf  # Latest Resume PDF
│   ├── profile.jpeg                 # Profile picture
│   ├── work.jpeg                    # Technical presentation photo
│   ├── style.css                    # Modern CSS stylesheet with themes & animations
│   └── certificate.pdf              # Internship certificate
├── templates/
│   └── index.html                   # Interactive portfolio template with persona switcher
├── main.py                          # FastAPI backend & contact API
├── requirements.txt                 # Python dependencies
├── vercel.json                      # Vercel deployment configuration
└── README.md
```

---

## 📌 Featured Projects

1. **[CV Workbench: Full-Lifecycle Computer Vision MLOps Workstation](https://github.com/aryankumarsaha/CV_assistant)**
   - Architected local-first computer vision platform across 6 vision tasks (detection, segmentation, oriented bounding boxes, pose, masks, classification).
   - Engineered data-quality engine (Laplacian blur + dHash/aHash perceptual hashing) removing 50% duplicate frames.
   - Built active-learning loop and PyTorch CUDA training with live SSE log streaming and ONNX/TensorRT edge export.

2. **[E-Commerce Sentiment Analysis Web Scraper (Myntra)](https://github.com/aryankumarsaha/myntra-review-scrapper)**
   - End-to-end NLP sentiment pipeline with Selenium, BeautifulSoup, Pandas, SQLite, and DistilBERT (90%+ accuracy).
   - Streamlit dashboard and Flask REST API delivering real-time Buy/Not Buy recommendations with sub-2s latency.
   - [Live Demo](https://myntra-review-scrapper-aryankumarsaha.streamlit.app/)

3. **[Insurance Premium Category Predictor & Risk Analytics](https://github.com/aryankumarsaha/Insurannce-prediction-API)**
   - Predictive machine learning platform with Scikit-learn Random Forest model (90%+ accuracy).
   - FastAPI + Pydantic validation reducing input errors by 40%, containerized with Docker.
   - Streamlit dashboard with interactive Plotly gauges and Tableau embeds.
   - [Live Demo](https://insurannce-prediction-api.onrender.com/)

4. **[Lung Disease Diagnostic System](https://github.com/aryankumarsaha/lungs-disease-diagnosis)**
   - PyTorch CNN image classification pipeline to triage pulmonary conditions from chest X-ray scans.

---

## ⚙️ Setup & Run Locally

```bash
# 1. Clone repository
git clone https://github.com/aryankumarsaha/portfolio.git
cd portfolio

# 2. Create and activate virtual environment
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start local development server
uvicorn main:app --reload --port 8000
```
Open [http://localhost:8000](http://localhost:8000) in your browser.

---

## 📬 Contact

- **Email:** [aryansahawork@gmail.com](mailto:aryansahawork@gmail.com)
- **Phone:** +91 7294056597
- **LinkedIn:** [linkedin.com/in/aryankumarsaha](https://www.linkedin.com/in/aryankumarsaha/)
- **GitHub:** [github.com/aryankumarsaha](https://github.com/aryankumarsaha)
