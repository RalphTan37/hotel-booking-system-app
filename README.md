# **Urban Oasis Hotel Management System**

---

## **Table of Contents**
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [CI/CD Workflow](#cicd-workflow)
- [Architecture Overview](#architecture-overview)

---

## **Features**
- **Admin Panel**: 
  - View, manage, and modify user accounts.
  - View and manage all customer bookings.
  - Oversee room availability, pricing, and booking history.
  
- **Customer Panel**: 
  - View available rooms and book them in real time.
  - View, manage, and modify personal bookings.
  - Make payments for bookings via the secure payment system.

- **Authentication**: 
  - Separate login for **Admins** and **Customers**.
  - Users log in with a **username** and **password**.
  - Admin usernames are prefixed with **admin_**.

- **Payments**:
  - Payments are securely processed through an interactive payment dialog.
  
- **Database Management**:
  - **SQLite** database is automatically created with default data for users, bookings, and rooms.

- **Security and Validation**:
  - Input validation is implemented for user data.
  - Room booking dates are validated to prevent double booking.

---

## **Installation**
Follow these instructions to set up and run the **Urban Oasis Hotel Management System** on your local machine.

### **Prerequisites**
- **Python 3.11.4** (Ensure it is installed and added to your system PATH)
- **pip** (Comes pre-installed with Python 3)
- **SQLite** (No additional setup required as it is included with Python)

### **Clone the Repository**
```bash
git clone https://github.com/yourusername/urban-oasis-hotel-management.git
cd urban-oasis-hotel-management
```

### **Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

### **Install Project Dependencies**
```bash
pip install -r requirements.txt
```

### **Create the Database**
```bash
python3 create_database.py
```

This step creates the `hotel_management.db` file with pre-defined users, rooms, and booking data.

---

## **Usage**
To start the application, run:
```bash
python3 main.py
```

You will see a **login screen**. Use one of the following credentials to log in.

### **Admin Login**
- **Username**: admin_johndoe
- **Password**: Any value (password is not validated in this version)

### **Customer Login**
- **Username**: ralph@slu.edu
- **Password**: Any value (password is not validated in this version)

Once logged in, you will have access to either the **Admin Panel** or **Customer Panel** depending on your user role.

---

## **Testing**
To run all **unit tests**, use:
```bash
python3 -m unittest unit_tests.py -v
```

### **How the Tests Work**
- Tests run on a **fresh database** every time.
- Before running the tests, the system **deletes the old hotel_management.db** and **recreates it** using the `create_database.py` script.
- **Unit Tests** ensure that all core functions like user creation, booking, and payment work as expected.

---

## **CI/CD Workflow**
The project includes an automated CI/CD workflow using **GitHub Actions**. The following jobs are included in the pipeline:

- **Setup**: Installs Python 3.11.4 and sets up the environment.
- **Run Tests**: Deletes the old database, creates a new one, and runs unit tests.
- **Lint Check**: Runs **pylint** on all `*.py` files and logs the results.
- **Security Check**: Runs **bandit** to detect security issues in `*.py` files.
- **Build**: Uses **PyInstaller** to build the application into an executable.

---

## **Architecture Overview**

### **High-Level System Design**
This diagram outlines the core components and interactions of the **Urban Oasis Hotel Management System**.

![Screenshot 2024-10-08 153142](https://github.com/user-attachments/assets/fd4d9177-b32f-4dd6-a6f1-6234c9c97e3d)

---

### **Database Design**
The following diagram illustrates the database structure, including the key tables and relationships.

![Screenshot 2024-10-08 154019](https://github.com/user-attachments/assets/6e628204-d9b6-4c39-b50c-2b87abc4b761)

---

### **Application Flow**
This diagram visualizes the application's logical flow, from login to booking and payments.

![Screenshot 2024-10-08 154859](https://github.com/user-attachments/assets/a7d6a149-ce5a-4eee-ab6f-b25849e1940f)
```
