#methods
class book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def display(self):
        print(self.title,self.author)
b1 = book('python','snoopy')
print(b1.title,b1.author)
