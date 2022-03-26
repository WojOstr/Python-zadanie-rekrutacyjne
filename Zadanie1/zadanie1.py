"""
Write a program that reads a text file and then makes a copy of it,
in which the order of the letters in each word is randomly changed except for
first and last letter of the word.
"""
import sys
import random

def randomize_letters(words: str) -> str:
    """
    Returns string with shuffled letters in it's interior.

    param: words - List of given words in readline of each iteration.
    """
    word_list = []
    words = words.split()
    for word in words:
        
        temp_word = list(word)
        if len(word) >= 1:
            """
            Make sure word is existing
            """
            if word[-1].isalpha():       
                """
                Check whether the last character is alphabetical
                """
                temp_word[1:-1] = random.sample(word[1:-1], len(word[1:-1]))
                word_list.append(''.join(temp_word))
            else:
                temp_word[1:-2] = random.sample(word[1:-2], len(word[1:-2]))
                word_list.append(''.join(temp_word))
                """
                Randomize letter from given string with range (1, -1) or (1, -2) if last character
                of string is not in alphabet e.g. [, ! .]
                """

    return ' '.join(word_list)


def main(argv):
    if len(argv) == 1:
        argv.append('Sample')
        """
        Defined Sample name if user doesn't include save location
        """
    try:
        if argv[0][-4:-1] + argv[0][-1] == '.txt':
            argv[0] = argv[0][0:-4]
        
        if argv[1][-4:-1] + argv[1][-1] == '.txt':
            argv[1] = argv[1][0:-4]

        """
        If parameters contains extension of file, it is deleted as it's already stated below
        """
       
        with open(f'./{argv[0]}.txt', 'r') as r, open(f'./{argv[1]}.txt', 'w') as w:
            for x in r.readlines():
                w.write(f"{randomize_letters(x)} \n")
    except:
        print("""Insert script arguments!\n
        First parameter - Name of txt file within same folder as python script\n
        Second parameter - txt file within same folder as python script where you want to save result *Optional
        """)

if __name__ == "__main__":
    main(sys.argv[1:])