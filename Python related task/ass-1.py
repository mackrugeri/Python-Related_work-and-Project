class node:             ## node
    def __init__ (self, data=None):
        self.val = data
        self.next = None
        self.pre = None
        self.up = None
        self.down = None
        
class linklist:         ## Kind of linklist but have four directions
    def __init__ (self):
        self.head = None

final_goal = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        
def puzzel (self):      ## create puzzel moves
    temp = self.head
    assin = temp.next.next.next.next
    n=0
    while n is not 12:
        temp.down = assin
        if n is not 11:
            temp = temp.next
            assin = assin.next
        n=n+1
    
    n=0
    while n is not 12:
        assin.up = temp
        temp = temp.pre
        assin = assin.pre
        n=n+1
    
    temp = self.head
    assin = temp.next
    n=0
    m=0
    while n is not 12:
        if m is 3:
            assin.pre = temp.next = None
            temp = assin
            assin = assin.next
            m=0
        else:
            temp = assin
            assin = assin.next
            m=m+1
        n=n+1
    return

linklist.puzzel = puzzel

def push(self,value):
    new_node = node(value)
    
    if self.head is None:
        self.head = new_node
        return
    
    nex = self.head
    while nex.next is not None:
        nex = nex.next
    
    new_node.pre = nex
    nex.next =new_node

linklist.push = push

def __str__ (self):
    red_str = ''
    temp = self.head
    n=0
    m=0
    while m is not 4:
        red_str += ' | '
        while n is not 4:
            red_str += str(temp.val)
            if temp.val <= 9 :
                red_str +=' '
            red_str +=' | '
            temp = temp.next
            n=n+1
        m=m+1
        n=0
        if m is 1:
            temp = self.head.down
        if m is 2:
            temp = self.head.down.down
        if m is 3:
            temp = self.head.down.down.down
        red_str+= "\n"
    red_str = red_str.rstrip(' | ')
    return red_str
linklist.__str__ = __str__

def search_blank(self):
    n=m=0
    temp = self.head
    while m is not 4:
        while n is not 4:
            if temp.val is 0:
                return temp
            temp = temp.next
            n=n+1
        m=m+1
        n=0
        if m is 1:
            temp = self.head.down
        if m is 2:
            temp = self.head.down.down
        if m is 3:
            temp = self.head.down.down.down
    return None
linklist.search_blank = search_blank

def comparing (self):
    n=m=k=0
    temp = self.head
    count = 0
    while m is not 4:
        while n is not 4:
            if temp.val is final_goal[k]:
                count +=1
            temp = temp.next
            n=n+1
            k=k+1
        m=m+1
        n=0
        if m is 1:
            temp = self.head.down
        if m is 2:
            temp = self.head.down.down
        if m is 3:
            temp = self.head.down.down.down
    return count
linklist.comparing = comparing

def store_puzzel (self):
    n=m=k=0
    ary=[]
    temp = self.head
    while m is not 4:
        while n is not 4:
            ary.append(temp.val)
            temp = temp.next
            n=n+1
            k=k+1
        m=m+1
        n=0
        if m is 1:
            temp = self.head.down
        if m is 2:
            temp = self.head.down.down
        if m is 3:
            temp = self.head.down.down.down
    return ary
linklist.store_puzzel = store_puzzel

def ary_puzzel(self,ary):
    n=m=k=0
    temp = self.head
    while m is not 4:
        while n is not 4:
            if temp.val is not ary[k]:
                temp.val = ary[k]
            temp = temp.next
            n=n+1
            k=k+1
        m=m+1
        n=0
        if m is 1:
            temp = self.head.down
        if m is 2:
            temp = self.head.down.down
        if m is 3:
            temp = self.head.down.down.down
    return None
linklist.ary_puzzel = ary_puzzel

def tree (self,blank , last, deep , current):
    print("       deep = ", current)
    print("")
    ary = store_puzzel(self)
    small = [20,20,20,20]
    
    if "next" is  not last and blank.next is not None:
        blank.val = blank.next.val
        blank.next.val = 0
        small[0] = 16-l.comparing()
        
    if "pre" is not last and blank.pre is not None:
        l.ary_puzzel(ary)
        blank.val = blank.pre.val
        blank.pre.val = 0
        small[1] = 16-l.comparing()
            
    if "up" is not last and blank.up is not None:
        l.ary_puzzel(ary)
        blank.val = blank.up.val
        blank.up.val = 0
        small[2] = 16-l.comparing()
         
    if "down" is not last and blank.down is not None:
        l.ary_puzzel(ary)
        blank.val = blank.down.val
        blank.down.val = 0
        small[3] = 16-l.comparing()
  
    mim = min(small)
    count = 0
    for i in small:
        if mim is i:
            count +=1
    if count < 2:
        if small[0] is mim:
            l.ary_puzzel(ary)
            blank.val = blank.next.val
            blank.next.val = 0
            if mim is 0:
                print(l)
                print("Reached the goal")
                return 1
            elif deep is current:
                print("return")
                return 0
            else:
                print(l)
                print("   -----------------")
                tree(self,blank.next,"pre",deep,current+1)
        if small[1] is mim:
            l.ary_puzzel(ary)
            blank.val = blank.pre.val
            blank.pre.val = 0
            if mim is 0:
                print(l)
                print("Reached the goal")
                return 1
            elif deep is current:
                print("return")
                return 0
            else:
                print(l)
                print("   -----------------")
                tree(self,blank.pre,"next",deep,current+1)
        if small[2] is mim:
            l.ary_puzzel(ary)
            blank.val = blank.up.val
            blank.up.val = 0
            if mim is 0:
                print(l)
                print("Reached the goal")
                return 1
            elif deep is current:
                print("return")
                return 0
            else:
                print(l)
                print("   -----------------")
                tree(self,blank.up,"down",deep,current+1)
        if small[3] is mim:
            l.ary_puzzel(ary)
            blank.val = blank.down.val
            blank.down.val = 0
            if mim is 0:
                print(l)
                print("Reached the goal")
                return 1
            elif deep is current:
                print("return")
                return 0
            else:
                print(l)
                print("   -----------------")
                tree(self,blank.down,"up",deep,current+1)

    else:
        print ("More than 2")
linklist.tree = tree

##################  function to identify reachable to goal or not #### 
def value_of_X(lst):
    for i in range (0,16):
        if lst[i] is 0:
            i+=1
            if i is 5 or i is 13 or i%2 is 0:
                return 1
            else:
                return 0
def even_or_odd(lst):
    epsilon = 0
    for i in range (0,16):
        for j in range (i+1,16):
            if lst[i] > lst[j]:
                epsilon +=1
    
    return epsilon + value_of_X(lst)

################ end of Function ##################

l = linklist ()
def main():
    lst = [1,5,2,3,4,6,10,7,8,9,0,11,12,13,14,15]
    if even_or_odd(lst)%2 is 0:
        #for i in range(0, 16): 
        #    ele = int(input()) 
        #    lst.append(ele)
        for i in range(0,16):
            l.push(lst[i])
        l.puzzel()
        print(l)
        if l.comparing() is 16:
            print("Reached the goal")
        else:
            for i in range (1,4):
                if i is not 1:
                    l.ary_puzzel(lst)
                print("    itratively = ", i)
                n=0
                n = l.tree(l.search_blank(),"no",i ,1)
                print(" n = ",n)
                if n is 1:
                    print(" n = ",n)
                    return None
    else:
        print("Unreachable")

main()