# 📝 Django Blog Project

This is a simple blog application built using Django, designed for educational purposes. It demonstrates key Django features such as:

- Class-based and function-based views  
- Post publishing workflow  
- Comment system  
- Tagging (with django-taggit)  
- Full-text search (PostgreSQL or fallback)  
- Pagination  
- Email sharing  
- Admin interface customization  

---

## 🚀 Features

- List and detail views for blog posts  
- Comment form with moderation  
- Share posts via email  
- Tag filtering for posts  
- Similar posts recommendation  
- Full-text search support  
- Responsive templates using Bootstrap  

---

## ⚙️ Requirements

Make sure you have Python 3.8+ and pip installed.

Install dependencies with:

```bash
pip install -r requirements.txt
🛠 How to Run
Clone the repository or download the ZIP.

Install dependencies.

Run migrations:

bash
Copy
Edit
python manage.py migrate
Create a superuser:

bash
Copy
Edit
python manage.py createsuperuser
Run the development server:

bash
Copy
Edit
python manage.py runserver
Access the app at http://localhost:8000/

📦 Included Files
blog_data.json – Example blog data for importing into the database

db.sqlite3 – Sample SQLite database

.gitignore – To exclude unnecessary files from Git

🔍 Search Functionality
This project uses PostgreSQL full-text search (if available).
If you're using SQLite, the basic search functionality will still work using simple filters.

👨‍💻 Author
Developed by mehrdad .R.sahraei

Replace YOUR_USERNAME with your actual GitHub username!
