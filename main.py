import csv
import datetime
import os
from reader import read_and_process_file

VERSION = "1.2.0"


def record_exam_performance():
    # Get input for exam set information
    exam_set_name = input("Enter the name of the exam set: ")
    num_questions = int(input("Enter the number of questions: "))

    # Get the current date and time for the filename
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create the CSV filename
    output_path = f".\\output_{VERSION}"
    csv_filename = f"{exam_set_name}_{current_datetime}.csv"

    # Initialize data list to store exam performance
    exam_performance_data = []

    # Initialize a list to store user answers for the current section
    user_answers = []
    start_time = datetime.datetime.now()
    end_time_list = []

    # Initialize section counter and scores dictionary
    section_number = 1
    scores = []
    section_time_list = []
    question_number = 1
    question_number_correct = 1

    # Input user answers for each section
    while question_number < num_questions + 1:
        print(f"\nSection {section_number}")
        section_user_answers = []
        section_end_time_list = []
        while question_number < num_questions + 1:
            user_answer = input(f"{question_number}. Your answer: ")
            if user_answer == ".":
                section_number += 1
                user_answers.append(section_user_answers)
                end_time_list.append(section_end_time_list)
                break
            section_user_answers.append(user_answer)
            section_end_time_list.append(datetime.datetime.now())
            question_number += 1

            time_range = abs(datetime.datetime.now() - start_time)

            # Convert the total seconds into hours, minutes, and seconds
            hours, remainder = divmod(time_range.total_seconds(), 3600)
            minutes, seconds = divmod(remainder, 60)

            # Print the result
            print(f"Time passed: {int(hours)}h {int(minutes)}m {int(seconds)}s")

    user_answers.append(section_user_answers)
    end_time_list.append(section_end_time_list)

    # Input correct answers for each section
    last_time = start_time

    # Get correct answers or path of it
    print(f"\nInput correct answers")
    correct_answers = input(f"{question_number_correct}. Enter correct answer: ")

    if correct_answers.startswith("read "):
        correct_answers = [
            str(ord(x[1]) - 64) for x in read_and_process_file(correct_answers[5:])
        ]
    else:
        correct_answers = [x for x in correct_answers]

    if len(correct_answers) != num_questions:
        raise Exception("Amount of questions and correct answers are mismatch.")

    for section, answers_in_section in enumerate(user_answers, start=1):
        exam_performance_data.append((f"Section {section}", "", "", "", ""))
        score = 0
        section_time = datetime.timedelta(0)

        # Update the correct answers in the exam performance data
        for i, answer in enumerate(answers_in_section, start=1):
            correct_answer = correct_answers[question_number_correct - 1]
            end_time = end_time_list[section - 1][i - 1]
            time_used = end_time - last_time
            last_time = end_time

            section_time += time_used

            if answer == correct_answer:
                score += 1

            # Append data to the list
            exam_performance_data.append(
                (
                    str(end_time - start_time),
                    question_number_correct,
                    answer,
                    correct_answer,
                    str(time_used),
                )
            )
            question_number_correct += 1

        scores.append(score)
        section_time_list.append(section_time)

    # Append section scores to the last row
    exam_performance_data.append(
        ("Sections", "Amount", "Correct", "Percentage", "Time used")
    )

    all_section_amount = 0

    for section, score in enumerate(scores, start=1):
        section_amount = len(user_answers[section - 1])
        all_section_amount += section_amount
        exam_performance_data.append(
            (
                f"Section {section}",
                section_amount,
                score,
                f"{score / section_amount * 100:.2f}%",
                section_time_list[section - 1],
            )
        )

    sum_score = sum(scores)

    exam_performance_data.append(
        (
            f"Total",
            all_section_amount,
            sum_score,
            f"{sum_score / all_section_amount * 100:.2f}%",
            sum(section_time_list, datetime.timedelta(0)),
        )
    )

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Save data to CSV file
    with open(
        output_path + "\\" + csv_filename, "w", encoding="utf-8", newline=""
    ) as csv_file:
        csv_writer = csv.writer(csv_file)

        metadata = [
            f"Title: {exam_set_name} Results",
            "Date: " + current_datetime,
            "Description: This CSV file contains exam results.",
            f"Generated by: Exam Recorder version {VERSION} created by TGOD",
        ]

        for item in metadata:
            csv_file.write(f"# {item}\n")

        # Add an empty line as a separator between metadata and data
        csv_file.write("\n")

        # Write header
        csv_writer.writerow(
            [
                "Total Time",
                "Question Number",
                "Your Answer",
                "Correct Answer",
                "Time Used",
            ]
        )
        # Write data
        csv_writer.writerows(exam_performance_data)

    print(f"Exam performance saved to {csv_filename}")


# Run the function to record exam performance
try:
    record_exam_performance()
except Exception as error:
    print(error)
finally:
    input("Press Enter to exit")
