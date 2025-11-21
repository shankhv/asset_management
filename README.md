# Asset Management System

This project is a lightweight Asset Management System built using Python and FastAPI.  
The application focuses on organizing, maintaining, and tracking organizational assets in a structured and expandable way.  
It follows a clean modular design so that new asset types, validation logic, or storage mechanisms can be added without affecting the core application.

The backend exposes REST APIs for creating, listing, updating, and managing asset information.  
FastAPI is used as the framework due to its speed, clean structure, automatic documentation support, and type-hint-based validation.

The system can serve as a foundational model for real-world asset management software used in companies to track laptops, inventory, equipment, or digital resources.

---

## Project Structure

```
asset_management/
│
├─ .idea/               # IDE configuration files
├─ config/              # Application-wide configurations
├─ app/                 # Main application logic and API modules
│   ├─ routers/         # FastAPI routers that define endpoints
│   ├─ models/          # Pydantic models for request/response schemas
│   ├─ services/        # Business logic (asset operations)
│   └─ database/        # Optional database or storage layer
│
├─ main.py              # Application entry point (FastAPI instance)
├─ requirements.txt     # Project dependencies
└─ README.md            # Project documentation
```

---

## Application Overview

The Asset Management System operates by exposing API endpoints that allow clients to interact with asset records.  
Every asset follows a structured data model that contains identifiers, asset details, and status information.  
Validation is performed automatically using FastAPI and Pydantic, ensuring the data entering the system is clean and formatted correctly.

The application’s internal logic is separated into dedicated components:

### **Models**
These define the structure of an asset.  
They determine what information an asset must contain—such as name, type, purchase date, serial number, and condition.

### **Routers**
Routers define the API paths (for example `/assets/`) and connect them with the business logic.  
Each router responds with JSON output and follows REST patterns.

### **Services**
These handle the actual asset operations such as storing assets, updating them, or retrieving lists of existing assets.  
They abstract the business logic from the API layer, making the code cleaner and easier to maintain.

### **Config**
Holds static configuration values, reusable constants, or environment-specific settings.

---

## FastAPI Interactive API Documentation (Swagger UI)

One of the biggest advantages of using FastAPI is the **automatic documentation** it generates.

Once the application is running, FastAPI provides two documentation interfaces:

| Type | URL | Description |
|------|-----|-------------|
| **Swagger UI** | `http://localhost:8000/docs` | Interactive API testing dashboard |
| **ReDoc** | `http://localhost:8000/redoc` | API documentation in a structured layout |

Through Swagger UI, all available API endpoints appear automatically.  
Each endpoint displays:

- Request method (GET, POST, PUT, DELETE)  
- Input schema  
- Output schema  
- Sample responses  
- Parameter descriptions  
- A button to test the API directly in the browser  

This makes the system easy to demonstrate, test, and validate during evaluation.

## Purpose of This Assignment Submission

This project demonstrates:

- Ability to build modular backend applications  
- Understanding of FastAPI router design  
- Usage of Pydantic models for data validation  
- Clean separation of logic, configuration, and API layers  
- Practical implementation of CRUD operations  
- Ability to design readable, maintainable backend code  
- Use of automatically generated Swagger documentation for API testing  
