import csv

# Store suspicious accounts with reasons (using set to avoid duplicates)
suspicious_account = {}
sender_count = {}

# Read CSV file
with open("transactions.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file)
    next(reader)  # skip header

    for row in reader:
        sender = row[0].strip()
        receiver = row[1].strip()
        amount = int(row[2].strip())

        # Count transactions
        sender_count[sender] = sender_count.get(sender, 0) + 1

        # Rule 1: Large transaction
        if amount > 50000:
            if sender not in suspicious_accounts:
                suspicious_accounts[sender] = set()
            suspicious_accounts[sender].add("Large transaction")

# Rule 2: Too many transactions
for sender, count in sender_count.items():
    if count > 5:
        if sender not in suspicious_accounts:
            suspicious_accounts[sender] = set()
        suspicious_accounts[sender].add("Too many transactions")

# Output
print("Suspicious Accounts:")
if suspicious_accounts:
    for acc, reasons in suspicious_accounts.items():
        print(f"{acc} → {', '.join(reasons)}")
else:
    print("No suspicious accounts found")
