from datetime import date


file_name = "word_list"
def get_word(date):
    current_date_str = date.strftime("%Y-%m-%d")
    with open(file_name, "r") as file:
        for line in file:
            parts = line.strip().split()
            if parts[0] == current_date_str:
                word_of_the_day = parts[1]
                return word_of_the_day
        else:
            return None
