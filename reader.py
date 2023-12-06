import csv


def alphabet_to_numeric(letter):
    letter_ord = ord(letter)
    if letter_ord > 64 and letter_ord < 70:
        numeric = ord(letter) - 64
    elif letter_ord > 48 and letter_ord < 54:
        numeric = ord(letter) - 48
    elif letter_ord > 96 and letter_ord < 102:
        numeric = ord(letter) - 96
    else:
        raise Exception(
            "alphabet_to_numeric: Fail to convert answer to numeric (invalid answer)"
        )

    return numeric


def read_and_process_file(file_path):
    # Read the TXT file
    with open(file_path, "r", encoding="utf-8") as file:
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

    return data_list


# Example usage:
filename = "monkeyeveryday TGAT-mock"
data_list = read_and_process_file(filename + ".txt")

# Save data to CSV file
csv_filename = filename + ".csv"
with open(csv_filename, "w", encoding="utf-8", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write header
    csv_writer.writerow(
        ["Question Number", "Correct Answer", "My Answer", "Is correct"]
    )
    # Write data
    csv_writer.writerows(data_list)

print(f"Data saved to {csv_filename}")
