import csv
import datetime

def record_exam_performance():
    # Get input for exam set information
    exam_set_name = input("Enter the name of the exam set: ")
    num_sections = int(input("Enter the number of sections: "))
    num_questions_per_section = int(input("Enter the number of questions per section: "))

    # Get the current date and time for the filename
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Create the CSV filename
    csv_filename = f"{exam_set_name}_{current_datetime}.csv"

    # Initialize data list to store exam performance
    exam_performance_data = []

    # Initialize section counter and scores dictionary
    section_counter = 1
    scores = {section: 0 for section in range(1, num_sections + 1)}

    # Input user answers for each section
    for section in range(1, num_sections + 1):
        print(f"\nSection {section}")

        # Initialize a list to store user answers for the current section
        user_answers = []

        for question_number in range(1, num_questions_per_section + 1):
            user_answer = input(f"{question_number}. Your answer: ")
            user_answers.append(user_answer)

        # Record exam performance for each section
        total_time_start = datetime.datetime.now()
        for question_number, user_answer in enumerate(user_answers, start=1):
            start_time = datetime.datetime.now()

            # Get correct answer (input later)
            correct_answer = None

            end_time = datetime.datetime.now()
            time_used = end_time - start_time

            # Append data to the list
            exam_performance_data.append((
                str(end_time - total_time_start),
                f"Section {section}",
                question_number,
                user_answer,
                correct_answer,
                str(time_used)
            ))

    # Input correct answers for each section
    for section in range(1, num_sections + 1):
        print(f"\nInput correct answers for Section {section}")
        
        # Initialize a dictionary to store correct answers for the current section
        correct_answers = {}
        
        for question_number in range(1, num_questions_per_section + 1):
            correct_answer = input(f"{question_number}. Enter correct answer: ")
            correct_answers[question_number] = correct_answer

        # Update the correct answers in the exam performance data
        for i, data in enumerate(exam_performance_data):
            if data[1] == f"Section {section}":
                exam_performance_data[i] = (
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    correct_answers[int(data[2])],  # Update correct answer
                    data[5]
                )

        # Calculate the score for each section
        correct_count = sum(user_answer == correct_answers[int(data[2])] for data in exam_performance_data if data[1] == f"Section {section}")
        section_score = (correct_count / num_questions_per_section) * 100
        scores[section] = section_score

    # Append section scores to the last row
    exam_performance_data.append(("Total", "", "", "", "", ""))
    for section, score in scores.items():
        exam_performance_data.append(("Section Score", f"Section {section}", "", f"Score: {score:.2f}%", ""))

    # Save data to CSV file
    with open(csv_filename, "w", encoding="utf-8", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write header
        csv_writer.writerow(["Total Time", "Section", "Question Number", "Your Answer", "Correct Answer", "Time Used"])
        # Write data
        csv_writer.writerows(exam_performance_data)

    print(f"Exam performance saved to {csv_filename}")

# Run the function to record exam performance
record_exam_performance()
