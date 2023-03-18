import csv
print("CSV Relations Replacer")
print("The csv files must be in the same directory as the script and must be inserted without extension.")

to_replace = input("Enter the name of the file to replace: ")
to_replace_ext = to_replace + ".csv"

with open(to_replace_ext, newline='') as csvfile1:
    reader1 = csv.DictReader(csvfile1)
    to_replace_dict = [row for row in reader1]

print("Keys in file to replace:", to_replace_dict[0].keys())

replace_from = input("Enter the name of the file to insert from: ")
replace_from_ext = replace_from + ".csv"

with open(replace_from_ext, newline='') as csvfile2:
    reader2 = csv.DictReader(csvfile2)
    replace_from_dict = [row for row in reader2]

print("Keys in file to insert from:", replace_from_dict[0].keys())

col_to_replace = input(f"Enter the key to replace in {to_replace_ext}: ")
col_corresponding = input(f"Enter the corresponding key from {replace_from_ext}. The two columns MUST have the same type of values: ")
col_replaced = input(f"Enter the key to replace in {to_replace_ext} from {replace_from_ext}: ")

for key_to_replace in to_replace_dict:
    for key_replaced in replace_from_dict:
        if key_to_replace[col_to_replace] == key_replaced[col_corresponding]:
            key_to_replace[col_to_replace] = key_replaced[col_replaced]

with open('output.csv', mode='w', newline='') as csvfile3:
    fieldnames = to_replace_dict[0].keys()
    writer = csv.DictWriter(csvfile3, fieldnames=fieldnames)

    writer.writeheader()
    for row in to_replace_dict:
        print(row)
        writer.writerow(row)
