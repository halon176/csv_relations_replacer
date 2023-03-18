import csv
import os

print("CSV Relations Replacer")
print("The csv files must be in the same directory as the script.")

# show the names of the files in the current directory
files = os.listdir()
csv_files = [f for f in files if f.endswith('.csv')]
print("CSV files in current directory:")
for i, f in enumerate(csv_files):
    print(f"{i+1}. {f}")

# ask the user to select the desired files
to_replace_num = int(input("Enter the number of the file to replace: "))
replace_from_num = int(input("Enter the number of the file to insert from: "))

to_replace_ext = csv_files[to_replace_num-1]
replace_from_ext = csv_files[replace_from_num-1]

with open(to_replace_ext, newline='') as csvfile1:
    reader1 = csv.DictReader(csvfile1)
    to_replace_dict = [row for row in reader1]

print("Keys in file to replace:")
for i, key in enumerate(to_replace_dict[0].keys()):
    print(f"{i+1}. {key}")
col_to_replace_num = int(input("Enter the number of the key to replace: "))
selected_key = list(to_replace_dict[0].keys())[col_to_replace_num - 1]
print(f"Selected key to replace: {selected_key}")

with open(replace_from_ext, newline='') as csvfile2:
    reader2 = csv.DictReader(csvfile2)
    replace_from_dict = [row for row in reader2]

print("Keys in file to insert from:")
for i, key in enumerate(replace_from_dict[0].keys()):
    print(f"{i+1}. {key}")
col_corresponding_num = int(input("Enter the number of the corresponding key from file to insert from. The two columns MUST have the same type of values: "))
col_corresponding = list(replace_from_dict[0].keys())[col_corresponding_num - 1]
print(f"Selected corresponding key: {col_corresponding}")

print(f"Enter the key to replace in {to_replace_ext} from {replace_from_ext}:")
for i, key in enumerate(replace_from_dict[0].keys()):
    print(f"{i+1}. {key}")
col_replaced_num = int(input("Enter the number of the key to replace in {to_replace_ext} from {replace_from_ext}: "))
col_replaced = list(replace_from_dict[0].keys())[col_replaced_num - 1]
print(f"Selected key to replace from file to insert from: {col_replaced}")

for key_to_replace in to_replace_dict:
    for key_replaced in replace_from_dict:
        if key_to_replace[selected_key] == key_replaced[col_corresponding]:
            key_to_replace[selected_key] = key_replaced[col_replaced]

with open('output.csv', mode='w', newline='') as csvfile3:
    fieldnames = to_replace_dict[0].keys()
    writer = csv.DictWriter(csvfile3, fieldnames=fieldnames)

    writer.writeheader()
    for row in to_replace_dict:
        print(row)
        writer.writerow(row)
