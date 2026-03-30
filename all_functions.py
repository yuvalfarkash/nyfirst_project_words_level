
def save_data(easy_word_list, hard_words_list :list, var_level:str, var_word:str, var_interpetasion:str):
    cureent_word={"word":var_word,
                  "translate":var_interpetasion,
                  }
    if var_level.lower()=='easy':
        easy_word_list.append(cureent_word)
    elif var_level.lower()=='hard':
        hard_words_list.append(cureent_word)
    else:
        print("invalid syntax in level, pls type again")
    print(easy_word_list)