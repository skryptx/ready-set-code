def check_count_in_name_by_word(name, word_for_count) -> int:
    count = 0
    for ch in word_for_count:
        count += name.count(ch)
    return count


def calculate_love_score(name1, name2) -> None:
    true = "TRUE"
    love = "LOVE"
    true_count = (check_count_in_name_by_word(name1.upper(), true)
                  + check_count_in_name_by_word(name2.upper(), true))


    love_count = (check_count_in_name_by_word(name1.upper(), love)
                  + check_count_in_name_by_word(name2.upper(), love))
    print(f"{true_count}{love_count}")

calculate_love_score("Kanye West", "Kim Kardashian")