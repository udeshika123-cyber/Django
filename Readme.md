# Django Project Workspace

This workspace contains a Django project with a virtual environment and several dependencies. Below is an index of the main files and directories:

## Root Directory

- `.gitignore`
- `.txt`
- `pyvenv.cfg`
- `Readme.md` (this file)
- `Include/`
- `Lib/`
  - `site-packages/`
    - `asgiref/`
    - `asgiref-3.8.1.dist-info/`
    - `django/`
    - `django-5.2.1.dist-info/`
    - `pip/`
    - `pip-25.1.1.dist-info/`
    - `sqlparse/`
    - `sqlparse-0.5.3.dist-info/`
    - `tzdata/`
    - `tzdata-2025.2.dist-info/`
- `my_first_project/`
  - `db.sqlite3`
  - `manage.py`
  - `my_first_project/`
    - `__init__.py`
    - ...
  - `myFirstApp/`
    - `templates/`
      - [`myfirst.html`](my_first_project/myFirstApp/templates/myfirst.html)
    - ...
- `Scripts/`
  - `activate`
  - `activate.bat`
  - `Activate.ps1`
  - `deactivate.bat`
  - `django-admin.exe`
  - `pip.exe`
  - `pip3.12.exe`
  - `pip3.exe`
  - `python.exe`
  - `pythonw.exe`
  - `sqlformat.exe`

## Notable Files

- [`my_first_project/manage.py`](my_first_project/manage.py): Django management script.
- [`my_first_project/db.sqlite3`](my_first_project/db.sqlite3): SQLite database file.
- [`my_first_project/myFirstApp/templates/myfirst.html`](my_first_project/myFirstApp/templates/myfirst.html): Main HTML template for your app.

## How to Run

1. **Activate the virtual environment**  
   On Windows:
   ```sh
   Scripts\activate
   ```
2. **Run the Django development server**

   ```sh
   cd my_first_project
   python manage.py runserver
   ```

3. **Access your app**  
   Open your browser and go to `http://127.0.0.1:8000/`

---

_This project uses Django and includes common dependencies such as `asgiref`, `sqlparse`, and `tzdata`._
