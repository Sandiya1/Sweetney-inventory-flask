# Sweetney Inventory Flask

Sweetney Inventory Flask is a web-based inventory management application built with Flask, a lightweight Python web framework. This project aims to provide a simple, extensible, and user-friendly interface for managing products, stock levels, and other inventory-related tasks.

## Features

- Add, update, and delete products in your inventory
- Responsive design for desktop and mobile devices
- Built using Flask and other popular Python libraries

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)
- (Optional) [virtualenv](https://virtualenv.pypa.io/en/stable/) for isolated Python environments

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sandiya1/Sweetney-inventory-flask.git
   cd Sweetney-inventory-flask
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install project dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the root directory and add necessary environment variables (such as `SECRET_KEY`, database configuration, etc.).

5. **Initialize the database:**
   ```bash
   flask db upgrade
   ```
   (Or follow the specific instructions in the project for database setup.)

6. **Run the application:**
   ```bash
   flask run
   ```

7. **Open your browser and visit:**
   ```
   http://127.0.0.1:5000/
   ```

## Usage

- Add new products to your inventory.
- Edit or delete existing products.
- Monitor inventory levels via the report.



## Technologies Used

- Python
- Flask
- SQLAlchemy (ORM)
- Jinja2 (templating)
- HTML CSS (frontend)

## Pages
*Home Page*

<img width="1859" height="626" alt="Screenshot 2025-10-05 174714" src="https://github.com/user-attachments/assets/b3963f42-b336-4f6f-821f-d73b53277d9f" />

 *Product Page*
 
<img width="1425" height="563" alt="Screenshot 2025-10-05 174724" src="https://github.com/user-attachments/assets/c1247c32-35a3-426d-a2ad-85339aa46e9b" />

<img width="1481" height="584" alt="Screenshot 2025-10-05 174742" src="https://github.com/user-attachments/assets/e617d424-ba6a-4341-a56f-6c8fe0510183" />

 *Location Page*
 
 <img width="1521" height="732" alt="Screenshot 2025-10-05 174752" src="https://github.com/user-attachments/assets/2191beb8-e6fe-48b6-ae37-74462326b9d5" />

*Movement Page*

<img width="1409" height="871" alt="Screenshot 2025-10-05 174817" src="https://github.com/user-attachments/assets/52e61379-ad4a-4f11-923d-e9a5d3d81b4f" />

<img width="1287" height="730" alt="Screenshot 2025-10-05 174841" src="https://github.com/user-attachments/assets/1ca0dd51-fa5c-45dc-95cf-6eea08bc6751" />

*Report Page*

<img width="1531" height="931" alt="Screenshot 2025-10-05 174856" src="https://github.com/user-attachments/assets/e1df464f-69a7-4171-845f-234b04f6dcd9" />

## Contact

For questions or support, please open an issue or contact [@Sandiya1](https://github.com/Sandiya1).
