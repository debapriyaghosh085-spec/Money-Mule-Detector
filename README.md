# Money-Mule-Detector
A Python project to detect suspicious bank accounts (money mule accounts) using transaction data and simple fraud detection rules.
## Money Mule Detection System

##  Project Overview

This project is a Python-based system to detect suspicious bank accounts (money mule accounts) using transaction data.

Money mule accounts are used to transfer illegally obtained money. This project identifies such accounts using simple rule-based analysis.

---

##  Objective

* Analyze transaction data from a CSV file
* Identify suspicious activities
* Flag accounts based on predefined rules

---

##  Detection Rules

1. **Large Transactions**

   * Any transaction greater than 50,000 is considered suspicious

2. **Too Many Transactions**

   * If a sender performs more than 5 transactions

---

##  Technologies Used

* Python
* CSV File Handling

---

##  Project Structure

```
money-mule-detector/
│── main.py
│── transactions.csv
│── README.md
```

---

##  How to Run

1. Clone the repository:

```
git clone <your-repository-link>
```

2. Go to the folder:

```
cd money-mule-detector
```

3. Run the program:

```
python main.py
```

---

##  Sample Input (transactions.csv)

```
sender,receiver,amount
A,B,60000
A,C,70000
A,D,80000
A,E,90000
A,F,100000
A,G,110000
B,A,1000
C,A,2000
D,A,1500
```

---

##  Sample Output

```
Suspicious Accounts:
A → Large transaction, Too many transactions
```

---

##  Features

* Detects suspicious accounts automatically
* Simple and efficient logic
* Clean and readable output
* Easy to modify and extend

---

##  Future Improvements

* Add more fraud detection rules
* Build a GUI
* Use real-time data
* Save output to a file

---

##  Learning Outcomes

* File handling in Python
* Working with CSV data
* Using dictionaries and sets
* Applying real-world logic

---

## 👤 Author

Debapriya Ghosh

