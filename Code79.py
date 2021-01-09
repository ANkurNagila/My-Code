class Classy(object):
    def __init__(self):
        self.items = []
        self.value=0
    def addItem(self,name):
        self.items.append(name)
        if name=="tophat":
            self.value+=2
        elif name=="bowtie":
            self.value+=4
        elif name=="monocle":
            self.value+=5
    def getClassiness(self):
        return self.value

# Test cases
me = Classy()

# Should be 0
print(me.getClassiness())

me.addItem("tophat")
# Should be 2
print(me.getClassiness())

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print(me.getClassiness())

me.addItem("bowtie")
# Should be 15
print(me.getClassiness())
