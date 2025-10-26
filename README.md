# 🏡 FindYourDomicile.com — Real Estate Management System (Python CLI Project) (2023)

A command-line real estate management system built in Python to demonstrate **while loops, for loops, conditional statements, break, pass, file handling, and the `getpass` library**.  
The project simulates a property management platform for **users** and **admins**, featuring both **residential** and **commercial** listings across all seven emirates of the UAE.

---

## 💡 Project Overview

**FindYourDomicile.com** is a menu-driven Python application that helps users explore and book properties while allowing admins to manage listings.  
The project focuses on **control flow and file operations**, without using user-defined functions, to clearly demonstrate understanding of Python’s procedural logic.

---

## 🧠 Concepts Demonstrated

| Concept | Demonstrated Through |
|----------|----------------------|
| `while` loops | Menus and navigation |
| `for` loops | Iterating through listings |
| `if`, `elif`, `else` | User choice handling |
| `break`, `continue`, `pass` | Loop control and menu flow |
| **File Handling** | Reading `aboutus.txt`, writing to `data.txt` and `bookings.txt` |
| **`getpass` Library** | Hidden password input for admin login |
| **Dictionaries & Lists** | Storage of property data |
| **External Library (`tabulate`)** | Displaying formatted tables in the terminal |

---

## 🗂️ Files Used

| File Name | Description | Created Automatically |
|------------|--------------|------------------------|
| **`main.py`** | Main Python program containing menus, property data, and logic | ❌ |
| **`aboutus.txt`** | Displays information about the company in the User section | ❌ |
| **`data.txt`** | Stores new properties added by the admin | ✅ |
| **`bookings.txt`** | Records all user bookings (residential & commercial) | ✅ |

---

## 🧾 File Details

### 📄 `aboutus.txt`
Contains the company introduction displayed when the user selects “About Us”.

Example:
```

WELCOME TO FINDYOURDOMICILE.COM

At FindYourDomicile, we connect you with the best homes and commercial spaces across the UAE.
Our mission is to make real estate transparent, accessible, and easy to explore.

```

---

### 🏠 `data.txt`
Appends data each time an admin adds a new property.

Example entries:
```

Residential - DXB - Barsha - 2BHK - 75000
Commercial - AD - Al Wahda - Office - 140000

```

---

### 🧾 `bookings.txt`
Stores records of all property bookings made by users.

Example entries:
```

Residential Booking - Code: 14111
Commercial Booking - Code: 401

````

---

## 🔐 Admin Login

- **Username:** (any name)  
- **Password:** `11SCB`  
  *(entered securely using the `getpass` library — input remains hidden)*

---

## ⚙️ How to Run the Program

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/FindYourDomicile.git
   cd FindYourDomicile
````

2. **Install dependencies**

   ```bash
   pip install tabulate
   ```

3. **Ensure the following files exist in the same directory:**

   * `main.py`
   * `aboutus.txt`

4. **Run the program**

   ```bash
   python main.py
   ```

---

## 📋 Features

### 👩‍💻 User Side

* View **About Us** information (read from file)
* Browse **Residential** or **Commercial** properties by emirate
* Filter residential listings by apartment type
* Book a property (booking stored in `bookings.txt`)

### 🧑‍💼 Admin Side

* Secure login using hidden password input
* Add new property listings (saved to `data.txt`)
* Remove existing listings
* View all available residential & commercial properties

---

## 🧱 Data Structure

The program uses two main dictionaries:

```python
dresi = { "AD": [...], "DXB": [...], "SHJ": [...], "AJ": [...], "UAQ": [...], "RAK": [...], "FJ": [...] }
dcomm = { "AD": [...], "DXB": [...], "SHJ": [...], "AJ": [...], "UAQ": [...], "RAK": [...], "FJ": [...] }
```

Each list entry follows this structure:

**Residential:**

```
['Area Name', 'Type', 'Size (sqft)', 'Rent (AED)', 'Facilities', 'Code']
```

**Commercial:**

```
['Area Name', 'Type', 'Size (sqft)', 'Rent (AED)', 'Facilities', 'Code']
```

---

## 🧑‍🏫 Learning Objectives

This project was created to:

* Practice **nested loops** and **conditional logic**
* Learn how to **read from and write to text files**
* Use **getpass** for secure input
* Display data in tabular form using **tabulate**
* Build a simple, **menu-driven application** without functions or OOP

---

## 🔮 Future Enhancements:

* Implement user login system
* Add search filters by rent or area
* Store data in CSV or JSON instead of plain text
* Add booking timestamps
* Build a GUI version with Tkinter or PyQt

---

## 👨‍💻 Author

**Name:** Mariam Fatima, Shresti Subahar, Grehna Geo Marian
**Email:** mariam37009@gmail.com
**GitHub:** https://github.com/MariamF35/

---
## 🙏 Acknowledgements
A huge thank you to **Vinitha John**, for guiding me patiently, teaching the concepts clearly, and inspiring me to keep experimenting.  
Shoutout to my awesome teammates **Shresti Subahar** and **Grehna Marian** for collaborating, sharing ideas, and making this project way more fun and manageable.  
And of course, cheers to everyone who helped indirectly—through tips, tutorials, or just moral support—keeping the coding vibes alive! 🚀
---

## 🪪 License

This project is open-source under the [MIT License](LICENSE).

Real_Estate_Project_2023
