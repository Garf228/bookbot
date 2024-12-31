print("hello world")
def main():
    with open("books/frankenstein.txt") as f:
     file_contents=f.read()
    
    def word_count():
       words=file_contents.split()
       print(f"The number of words is {len(words)}")
    
    def character_count():
        book_string = file_contents.lower()
        letter_dictionary={}
        for char in book_string:
            if char in letter_dictionary:
                letter_dictionary[char]+=1
            else:
                letter_dictionary[char]=1

        for letter in letter_dictionary:
           print(f"The '{letter}' character was found {letter_dictionary[letter]} times")

    word_count()
    character_count()
main()
