import csv

filename = "monkeyeveryday TGAT-mock"

# Read the TXT file
with open(filename + ".txt", "r", encoding="utf-8") as file:
    txt_content = file.read()

# Split the text content into lines
lines = txt_content.splitlines()

# Extract data and save to CSV
data_list = []
current_question = None
for no_line, line in enumerate(lines):
    if line.startswith("เฉลย :"):
        current_question = lines[no_line - 1].strip()
        correct_answer = lines[no_line + 1].strip()
        my_answer = lines[no_line + 3].strip()

        data_list.append(
            (
                current_question,
                correct_answer,
                my_answer,
                "" if correct_answer == my_answer else "Incorrect",
            )
        )

# Save data to CSV file
csv_filename = filename + ".csv"

with open(csv_filename, "w", encoding="utf-8", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write header
    csv_writer.writerow(["Question Number", "Correct Answer", "My Answer", "Is correct"])
    # Write data
    csv_writer.writerows(data_list)

print(f"Data saved to {csv_filename}")
