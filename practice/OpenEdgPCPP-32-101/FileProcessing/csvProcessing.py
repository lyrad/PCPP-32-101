import csv

## Parsing CSV.
# csv.reader().
with open('contacts.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(row)  # List of values.
    print()

# csv.DictReader().
with open('contacts.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # reader.fieldnames: list (or tuple?) containing the first line values.

    for row in reader:
        print(row)  # Dictionary: 'row name (first line)' => 'row value'.
    print()

# csv.DictReader(), advanced.
with open('contacts.csv', newline='') as csvfile:
    # Select fields (change order, field must exist in first line or line will be seen as data).
    fieldnames = ['Name']
    reader = csv.DictReader(csvfile, fieldnames=fieldnames)
    for row in reader:
        # None when field name not in fieldname list.
        print(row)
    print()


## Writing CSV.
# csv.writer().
with open('exported_contacts.csv', 'w', newline='') as csvfile:
    # quoting: QUOTE_ALL, QUOTE_NONNUMERIC, QUOTE_NONE
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    # writer.writerow(<valueList>)
    writer.writerow(['Name', 'Phone'])
    writer.writerow(['mother', '222-555-101'])
    writer.writerow(['father', '222-555-102'])
    writer.writerow(['wife', '222-555-103'])
    writer.writerow(['mother-in-law', '222-555-104'])
    writer.writerow(['grandmother, grandfather', '222-555-105'])

# csv.DictWriter().
with open('exported_contacts.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Phone']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # writer.writeheader(): write fieldnames.
    writer.writeheader()
    # writer.writerow(<valueList>)
    writer.writerow({'Name': 'mother', 'Phone': '222-555-101'})
    writer.writerow({'Name': 'father', 'Phone': '222-555-102'})
    writer.writerow({'Name': 'wife', 'Phone': '222-555-103'})
    writer.writerow({'Name': 'mother-in-law', 'Phone': '222-555-104'})
    writer.writerow({'Name': 'grandmother, grandfather and auntie', 'Phone': '222-555-105'})