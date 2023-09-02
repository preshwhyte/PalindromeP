
# class which returns palindrome of strings(words)

class Palindrome:
    def __init__(self, words):
        self.words=words
    
    def isPalindrome(self):
        # pass reverse function
        if self.words==self.words[::-1]:
            try:
                return 'palindrome'
            except TypeError:
                return 'Wrong Data Type'
        else:
            pass

        
wordList=['eye','eve', 'kate','0124210','Nigeria']
#worldlist= input(str("Enter your words here"))

PalindromeWorlds=[]

#iterating through List to get Palindrome words only
for word in wordList:
    # print(word)
    palindrome=Palindrome(word)
    a=palindrome.isPalindrome()
    # print(a)
    if a=="palindrome":
        try:
            PalindromeWorlds.append(word)
            # print(PalindromeWorlds)
        except TypeError:
            print('TypeError: Please insert a string value')

# converting the list to string words
words=' '.join(map(str,wordList))

result=' '.join(map(str,PalindromeWorlds))

# Final output of Palindrome words only
print(words, "  ---RETURNS--  " , result)
