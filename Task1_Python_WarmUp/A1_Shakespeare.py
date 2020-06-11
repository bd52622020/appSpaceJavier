'''
Created on 27 May 2020

@author: javi
How  many words ?
How  many lines?
How  many vowels ?
How many  numbers ? 
'''
import csv

def count_vowels(word):
    return sum(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' for char in word.lower())

def is_number(word):
    try:
        float(word)
        return True
    except ValueError:
        pass
    return False

def count():
    file = open("./Shakespeare.txt", "rt")
    num_words, num_lines, num_vowels, num_numbers = 0, 0, 0, 0
    
    for line in file:
        num_lines += 1
        words = line.split()

        for word in words:
            num_words += 1
            # COunt vowels and kno9w if it is a number
            vowels = count_vowels(word)
            if vowels != 0:
                num_vowels += vowels
            elif is_number(word):
                num_numbers += 1 
            
    
    print('Number of words :', num_words)
    print('Number of lines:', num_lines)
    print('Number of vowels :', num_vowels)
    print('Number of numbers :', num_numbers)
    
    with open('count_shakespeare.csv', mode='w') as csvfile:        
        s_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
        s_writer.writerow(['Words', 'Lines', 'Vowels', 'Numbers'])
        s_writer.writerow([num_words, num_lines, num_vowels, num_numbers])



if __name__ == "__main__":
    # execute only if run as a script
    #print(count_vowels('javier'))
    count()