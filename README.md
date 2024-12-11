# **Urban Oasis Hotel Management System**

Welcome to the **Urban Oasis Hotel Management System**. This project is a comprehensive hotel management solution that allows hotel administrators, staff, and guests to manage room bookings, view user information, and handle payments — all in one place. The system features both **Admin** and **Customer** panels with a focus on simplicity, efficiency, and ease of use.

---

## **Table of Contents**
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [CI/CD Workflow](#cicd-workflow)
- [Technologies Used](#technologies-used)
- [File Descriptions](#file-descriptions)
- [Contributing](#contributing)
- [License](#license)

---

## **Features**
- **Admin Panel**: 
  - View all users and manage user accounts.
  - View all bookings and manage bookings.
  - View and manage room availability and pricing.
  
- **Customer Panel**: 
  - View available rooms and book rooms.
  - View personal bookings and check out of rooms.

- **Authentication**: 
  - Users can log in with a **username** and **password**. 
  - Admins can log in using a username prefixed with **admin_**.
  
- **Payments**:
  - Customers can make payments via a secure payment dialog.
  
- **Database Management**:
  - Automatically creates and initializes the database with default users, rooms, and bookings.
  
- **Security and Validation**:
  - User inputs are validated for correct data formats.
  - Room booking dates are checked to avoid conflicts.

---

## **Installation**
Follow these instructions to get the **Urban Oasis Hotel Management System** running on your local machine.

### **Prerequisites**
- **Python 3.11.4** (Make sure it is installed and added to your system PATH)
- **pip** (comes pre-installed with Python 3)
- **SQLite** (No additional setup required since it is included with Python)

### **Clone the Repository**

```bash
git clone https://github.com/yourusername/urban-oasis-hotel-management.git
cd urban-oasis-hotel-management
```

## **Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

## **Install Project Dependencies**

```bash
pip install -r requirements.txt
```

## **Create the Database**

```bash
python3 create_database.py
```

## **Usage**

To start the application, run:

```bash
python3 main.py
```
  
## Architecture Overview:
The application follows a modular architecture, separating concerns between the user interface, business logic, and data management. This design ensures maintainability and scalability as new features can be added with minimal impact on existing code.

![Screenshot 2024-10-08 153142](https://github.com/user-attachments/assets/fd4d9177-b32f-4dd6-a6f1-6234c9c97e3d)

![Screenshot 2024-10-08 154019](https://github.com/user-attachments/assets/6e628204-d9b6-4c39-b50c-2b87abc4b761)

![Screenshot 2024-10-08 154859](https://github.com/user-attachments/assets/a7d6a149-ce5a-4eee-ab6f-b25849e1940f)
