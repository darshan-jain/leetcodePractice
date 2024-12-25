class Solution:
    def reverseVowels(self, s: str) -> str:

        letters = list(s)
        vowels = []
        for char in letters:
            if char == 'A' or char == 'a' or char == 'e' or char =='E' or char =='i' or char =='I' or char =='o' or char == 'O' or char =='u' or char=='U':
                vowels.append(char)
        i = 0
        revvol = vowels[::-1]
        for j in range(len(letters)):
            char = letters[j]
            if char == 'A' or char == 'a' or char == 'e' or char =='E' or char =='i' or char =='I' or char =='o' or char == 'O' or char =='u' or char=='U':
                letters[j] = revvol[i]
                i+=1
        
        return "".join(letters)



        