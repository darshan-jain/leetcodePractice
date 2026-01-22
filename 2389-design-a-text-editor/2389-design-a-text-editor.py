class TextEditor:

    def __init__(self):
        self.left = []
        self.right = []
        
    def addText(self, text: str) -> None:
        for c in text:
            self.left.append(c)
        

    def deleteText(self, k: int) -> int:
        cnt = 0 
        while self.left and cnt < k:
            self.left.pop()
            cnt+=1
        return cnt
    
    def _leftmax(self):
        l = min(10,len(self.left))
        return "".join(self.left[-l:])

    def cursorLeft(self, k: int) -> str:
        cnt = 0 
        while self.left and cnt<k:
            self.right.append(self.left.pop())
            cnt+=1
        
        return self._leftmax()
        

    def cursorRight(self, k: int) -> str:
        cnt = 0 
        while self.right and cnt<k:
            self.left.append(self.right.pop())
            cnt+=1
        return self._leftmax()
        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)