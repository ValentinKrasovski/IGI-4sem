import utilities
import os

if __name__ == "__main__":
    path_for_folder = "/home/valentin/Studing/IGI/IGILab2/task1"
    file_name = "file.txt"
    full_path = os.path.join(path_for_folder, file_name)

    if (utilities.check_file(full_path)):
        file = open(full_path, encoding="UTF8")
        text = file.read()
        print(f"Total number of sentences {utilities.total_number_sentences(text)}")
        print(f"Total number of non declarative sentences {utilities.count_nondeclarative_sentences(text)}")
        print(f"Average length words {utilities.average_len_words(text)}")
        print(f"Average length sentensec {utilities.average_len_sentences(text)}")
        print(f"Top-k N-grams{utilities.top_repeted_grams(text)}")
