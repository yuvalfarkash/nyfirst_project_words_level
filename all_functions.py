


def save_data(easy_word_list, hard_words_list :list, var_level:str, var_word:str, var_interpetasion:str):
    cureent_word={"word":var_word,
                  "translate":var_interpetasion,
                  }
    if var_level.lower()=='easy':
        easy_word_list.append(cureent_word)
        print("word added to easy word list")
    elif var_level.lower()=='hard':
        hard_words_list.append(cureent_word)
        print("word added to hard word list")

    else:
        print("invalid syntax in level, pls type again")
    print(easy_word_list)
    
def show_easy_list(easy_word_list):
    for i in easy_word_list:
        print(f"word: {i["word"]}")
        print(f"defenition: {i["translate"]}")
    
    
    
def show_hard_list(hard_word_list):
    for i in hard_word_list:
        print(f'word: {i["word"]} defenition: {i["translate"]}')
    
def add_word():
    pass
# def remove_word(remove_word_name:str, one_of_the_lists):
#     for i in one_of_the_lists:
#         # one_of_the_lists.remove(i)
        
    