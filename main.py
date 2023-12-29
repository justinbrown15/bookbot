def main():
    file_contents = get_book()
    count_words(file_contents)
    
    #print(count_letters(file_contents))
    my_dict = count_letters(file_contents)
    print_report(my_dict)
def get_book():
    counter = 0
    with open("books/frankenstein.txt") as f:
       file_contents = f.read()
    return file_contents
def count_words(file_contents):
    word_count = len(file_contents.split())
    print(f"Word count: {word_count}")
         
def count_letters(file_contents):
    #make the file contents lower case
    lower_case = file_contents.lower()
    dict = {}
    for line in lower_case:
        for letter in line:
            if letter.isalpha():
                if letter in dict:
                    dict[letter] += 1
                else:
                    dict[letter] = 1

    return dict
             
def print_report(my_dict):
    dict_as_list = list(my_dict.items())
    dict_as_list.sort()
    for key, value in dict_as_list:
        print(f"The {key} character was found {value} times")


                





    
main()
   