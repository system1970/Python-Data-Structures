class List(object):
    def __init__(self,size):
        self.size = size
        if self.size==-1:
            self.size==None
        self.top = None
        self.length = 0
        self.list = []
        
    def push(self,value):
        if self.length<self.size or self.size==None:
            self.value = value
            self.list.append(self.value)
            self.top = self.value
            self.length+=1
            self.nextnode = None
        else:
            print("Max push limit reached, no more space available")

    def multipush(self,arr):
        self.arr = arr
        for i in range(len(arr)):
            self.list.append(arr[i])
        self.length+=len(arr)

    def peek(self):
        return self.top

    def isInt(self,val1,val2):
        try:
            val1-=1
            val2-=1
            return True
        except:
            return False

    def badsort(self):
        for i in range(self.length):
            for j in range(self.length):
                try:
                    self.list[i]+=0
                    self.list[j]+=0
                except:
                    continue
                if self.list[i]<self.list[j]:
                    temp = self.list[i]
                    self.list[i] = self.list[j]
                    self.list[j] = temp
        return self.list

    def smartsort(self):
        self.sorted_list = self.list
        position = 0
        for i in range(len(self.sorted_list)):
            try:
                self.sorted_list[position]+=1
                self.sorted_list[position]-=1
                position+=1
            except:
                self.sorted_list.pop(position)
        for i in range(len(self.sorted_list)):
            for j in range(len(self.sorted_list)):
                if self.sorted_list[i]<self.sorted_list[j]:
                    temp = self.sorted_list[i]
                    self.sorted_list[i] = self.sorted_list[j]
                    self.sorted_list[j] = temp
        return self.sorted_list

    def print(self):
        return self.list
        
a = List(11)
a.multipush(["sdfsdfsdf","sdghkshg","sfhgkh"])
a.multipush([45,23,56,23,34])
a.push(110)
a.push(110)
a.push(110)
a.multipush(["sdfsdfsdf","sdghkshg","sfhgkh"])
print(a.print())
print(a.peek())
print(a.badsort())
print(a.smartsort())

