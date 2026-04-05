# 🌐 Aryan Kumar Saha - Portfolio Website

This is my personal portfolio website built using **FastAPI, HTML, and CSS**, showcasing my work in **AI/ML, Data Science, and Data Analytics**.

🔗 Live Demo: https://your-portfolio.onrender.com

---

## 🚀 Features

- 💼 Professional portfolio UI (dark theme)
- 🤖 Showcases AI/ML & Data Science projects
- 📊 Highlights Data Analytics skills (Power BI, SQL)
- 🧠 Includes real internship experience
- 📂 Project descriptions with tech stack
- 📞 Clickable contact (Email, Phone, LinkedIn, GitHub)
- 🌐 Deployed using Render

---

## 🛠️ Tech Stack

- **Backend:** FastAPI  
- **Frontend:** HTML, CSS  
- **Templating:** Jinja2  
- **Deployment:** Render  
- **Version Control:** Git & GitHub  

---

## 📁 Project Structure

portfolio/
│
├── static/
│ ├── profile.jpeg
│ ├── work.jpeg
│ ├── style.css
│ ├── certificate.pdf
│
├── templates/
│ └── index.html
│
├── main.py
├── requirements.txt
├── render.yaml




---

## ⚙️ Setup Locally

```bash
# Clone repo
git clone https://github.com/aryankumarsaha/portfolio.git

# Navigate
cd portfolio

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn main:app --reload
