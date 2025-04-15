from asyncore import write
import re
import sys
import csv


def add(new_record):
    records = []
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            records.append(row)


# 1
# Sort the records based on a specific column (e.g., index 0)
# sorted_records = sorted(
#     records, key=lambda x: x[2])
# Replace `0` with the desired column index

# Write the sorted records to a new CSV file
# with open("data.csv", "w", newline="") as sorted_file:
#     writer = csv.writer(sorted_file)
#     writer.writerows(sorted_records)
# 2
# Find the position to insert the new record
# insert_position = 0
# field_to_sort = new_record[0]
# for i, record in enumerate(records):
#     if new_record[field_to_sort] < record[field_to_sort]:
#         insert_position = i
#         break
#     else:
#         insert_position = i + 1

# Insert the new record at the identified position
# records.insert(insert_position, new_record)

#  Write the updated records back to the CSV file

# with open("data.csv", "w", newline="") as csv_file:
#     csv_writer = csv.Writer(csv_file)
#     csv_writer.writerrows(records)


###


def view():
    data = []
    with open("data.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    sorted_records = sorted(data, key=lambda x: x[0])
    print(sorted_records)
    return sorted_records

    # view()


def remove(i):
    def save(j):
        with open("data.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(j)

    new_list = []
    telephone = i

    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element == telephone:
                    new_list.remove(row)
    save(new_list)


def update(i):
    def update_newlist(j):
        with open("data.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(j)

    new_list = []
    telephone = i[0]

    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element == telephone:
                    name = i[1]
                    gender = i[2]
                    telephone = i[3]
                    email = i[4]

                    data = [name, gender, telephone, email]
                    index = new_list.index(row)
                    new_list[index] = data

    update_newlist(new_list)


def search(i):
    data = []
    telephone = i
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            for element in row:
                if element == telephone:
                    data.append(row)

        print(data)
        return data


search("123")
