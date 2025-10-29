# Restaurant Management System (OOP Edition)

A modular, menu-driven Python application for managing restaurant operations — built with clean architecture, object-oriented design, and real-world constraints.

## Features

- Staff Sign-Up and Sign-In.
- Admin Login (preloaded)
- Menu Display (from JSON)
- Order Placement, Update, Cancel
- Menu update,add items in menu
- Invoice-Style Billing with Tax
- Table Booking and Viewing
- Role-Based Dashboards (Admin/Staff)
- Centralized Input Validation
- Dynamic File Paths (cross-platform compatible)

## Folder Structure
src/ ├── main.py ├── Authentication/ │   └── auth_ops.py ├── Validation/ │   └── validators.py ├── Domain/ │   ├── menu_ops.py │   ├── order_ops.py │   ├── bill_gen.py │   └── booking_ops.py ├── Report/ │   └── dashboards/ │       ├── staff_dashboard.py │       └── admin_dashboard.py ├── Model/ │   ├── user_model.py │   └── menu_data.py ├── Database/ │   ├── users.json │   ├── menu.json │   ├── orders.json │   ├── bills.json │   └── bookings.json ├── logs/ │   └── activity.log ├── readme.md └── requirements.txt


## Admin Credentials

- **Email**: `admin@vfcpremium.com`
- **Password**: `VFCadmin@123`

## How to Run

1. Open terminal or VS Code
2. Navigate to `src/` folder
3. Run:

```bash
python main.py

Data Files :
Stored in Database/ as .json:
- users.json → Registered users
- menu.json → Menu items
- orders.json → Placed orders
- bills.json → Generated bills
- bookings.json → Table reservations
  Validation Rules :
- Email format
- Mobile: 10 digits
- Name: letters only
- Password: ≥ 6 characters
- Table: starts with "T" + number
- Date: YYYY-MM-DD
- Time: HH:MM


