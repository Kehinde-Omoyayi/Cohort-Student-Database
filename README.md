Cohort Student Database System
 
A structured backend system designed for managing student cohort records using a relational database architecture. The system provides efficient CRUD operations, modular routing, and scalable backend logic for handling student data in an organized and maintainable way.

Project Overview:
The Cohort Student Database System is a backend-focused application built to simulate real-world student record management. It demonstrates how structured database design and API-driven workflows can be used to manage, retrieve, and manipulate student information efficiently.

This project emphasizes:
- Clean backend architecture
- Database-driven design
- Modular code structure
- Scalable data handling logic
  
Tech Stack:
- Backend: Python
- Framework: Django 
- Database: SQLite / SQL
- Version Control: Git & GitHub
- Architecture Style: Modular backend structure

Features:
- Student Management (CRUD Operations)
Create new student records
Retrieve student details
Update existing student information
Delete student records

- Database Integration
Structured relational database design
SQL-based queries for data operations
Efficient data retrieval and filtering

- Backend Architecture
Modular routing system
Separation of concerns (routes, logic, database layer)
Scalable project structure

- Data Validation
Input validation before database insertion
Error handling for invalid requests

📂 Project Structure:
Cohort-Student-Database/
│
├── app/
│   ├── routes/          # API endpoints
│   ├── models/         # Database models / schema logic
│   ├── services/       # Business logic layer
│
├── database/
│   └── schema.sql      # Database structure
│
├── config.py           # App configuration
├── run.py              # Application entry point
├── requirements.txt    # Dependencies
│
└── README.md

API Endpoints:

Method.    Endpoint.        Description
GET.       /students.       Retrieve all students
GET.       /students/<id>.  Retrieve a single student
POST.      /students.       Create new student
PUT.       /students/<id>.  Update student details
DELETE.    /students/<id>.  Delete student record

Example Request:

Create Student
Json

POST /students
Content-Type: application/json

Json

{
  "name": "John Doe",
  "matric_number": "FUNAAB/CSC/2023/001",
  "department": "Computer Science",
  "level": 200
}

Author:
Omoyayi Kehinde
Backend Software Engineer (Transitioning)
GitHub: https://github.com/Kehinde-Omoyayi
LinkedIn: https://www.linkedin.com/in/kehinde-omoyayi-8b8513356
