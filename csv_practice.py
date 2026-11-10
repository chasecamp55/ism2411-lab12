# ISM2411 Lab 12 - Sales CSV Report
# Name: Chase Campbell

# Reflection 1:
# Python can automate cleaning and processing CSV files,
# making it useful for large datasets and repeated tasks.
# Excel is easier for manually editing data and creating
# quick charts, but Python is better for automating workflows.

# Reflection 2:
# A business could use an append-mode log to track daily
# sales reports and when they were generated. Append mode
# is useful because it adds new records without deleting
# previous entries.

# Exercise 1 - Get the File

import csv
from datetime import datetime

print("Exercise 1")

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)
    rows = list(reader)

print("CSV file opened successfully!")
print(f"Header: {rows[0]}")
print(f"Number of data rows: {len(rows) - 1}")

# Exercise 2 - Read and Print Raw Rows

print("\nExercise 2")

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# Exercise 3 - Skip the Header

print("\nExercise 3")

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)

        # Exercise 4 - Compute Totals

print("\nExercise 4")

total_revenue = 0

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total

        print(
            f"{product}: {quantity} units x "
            f"${price:.2f} = ${total:.2f}"
        )

print(f"Total Revenue: ${total_revenue:.2f}")

# Exercise 5 - Filter and Write

print("\nExercise 5")

original_count = 0
cleaned_count = 0

with open("data/sales.csv", "r", newline="") as infile:
    reader = csv.reader(infile)
    next(reader)

    with open("data/cleaned.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_count += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            total = price * quantity

            if total > 100:
                writer.writerow([
                    product,
                    f"{price:.2f}",
                    quantity,
                    f"{total:.2f}"
                ])
                cleaned_count += 1

print(f"Original rows: {original_count}")
print(f"Cleaned rows written: {cleaned_count}")

# Exercise 6 - DictReader

print("\nExercise 6")

# csv.reader is useful for simple files when column positions
# are known. DictReader is better when I want to access
# columns by name, making the code easier to understand.

dict_total_revenue = 0

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        dict_total_revenue += total

        print(f"{product}: ${total:.2f}")

print(f"Total Revenue: ${dict_total_revenue:.2f}")

# Exercise 7 - Sales Summary by Product

print("\nExercise 7")

sales_summary = {}

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity

        sales_summary[product] = (
            sales_summary.get(product, 0) + total
        )

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")

# Exercise 8 - Append Mode Log

print("\nExercise 8")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("data/run_log.txt", "a") as logfile:
    logfile.write(
        f"{timestamp} - Total Revenue: "
        f"${total_revenue:.2f}\n"
    )

print("Run log updated successfully!")
