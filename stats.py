def count_words(input_string):
    word_list =[]
    word_list = input_string.split()
    word_count = len(word_list)
    return word_count
    # print(f"{word_count} words found in the document")

def char_count(input_string):
    number_dict ={}
    lower_string = input_string.lower()
    for i in lower_string:
        if i not in number_dict:
            number_dict[i]=0
        number_dict[i]+=1
    return number_dict

def count_label(input_dict):
    labeled_dict_list=[]
    temp_dict={}

    for s,c in input_dict.items():
        temp_dict = {"Char": s, "Count": c}
        labeled_dict_list.append(temp_dict)
    labeled_dict_list.sort(reverse=True, key=sort_on)
    return labeled_dict_list

def sort_on(dict):
    return dict["Count"]

