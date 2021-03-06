from copy import deepcopy
class Puzzle:
    def __init__(self,l,level=0,l_move=None):
        
        
        self.level=level
        self.board=l
        self.explored=False

        self.up=self.down=self.left=self.right=None
        self.l_move=l_move

def path_finding(Puzzle):
    Path=""

    for value in Puzzle[1:]:
        if value.l_move=='u':
            action="moving up"
        if value.l_move=='d':
            action="moving down"
        if value.l_move=='r':
            action="moving right"
        else:
           	action="moving Left"
        print(action)
    print("--------------------------------------------------")
    print("Final Result")
    printing(value.board)
    print("--------------------------------------------------")

def Start_function():
	Problem=[
    [ 4,  1 , 2  ,3 ],
    [ 5,  6,  10,  7 ],
    [ 8, 13, 9 , 11],
    [12, 0, 14, 15] 
                    ]
	puzzle=Puzzle(Problem)
	puzzle=Solution_problem(puzzle)
	print("\nPath of Solution to its Puzzle : \n")
	path_finding(puzzle)

def make_move(puzzle,move,last_move=None):
    
    col=row=0
    for i in puzzle:
        row+=1
        if 0 in i:
            col= i.index(0)
            break
    
    row-=1
    return possipuzzle_arraylities(col,row,puzzle,move,last_move)

def table(xyz):
    listing = []
    for i in xyz:
        for j in i:
            listing.append(j)
    return listing 
    


def inversions(a):
    count=0
    a=table(a)
    
    for i in range(len(a)-1):
        for j in a[i+1:]:
            if a[i] > j and j !=0:
                count+=1
    return count


def printing(table): 
    for value in table:
        print(value)

 
# Solving of the Problem
def Condition_problem(queue_list,level_limit):
    if inversions(queue_list[-1].board)==0 and (queue_list[-1].board[0][0]==0 or queue_list[-1].board[3][3]==0):
        queue_list[-1].explored=True
        return queue_list
    if queue_list[-1].level<level_limit and queue_list[-1].explored==False:
        parent(queue_list)
    else:
        k=  queue_list.pop(-1)
        del k
def parent_converting(queue_list):
    queue_list[-1].explored=True
    parent=queue_list[-1]        
    flag , temp = make_move(deepcopy(parent.board),'l',parent.l_move)
    if flag:
        node = Puzzle(temp,parent.level+1,'l')
        queue_list.append(node)                      
    flag , temp = make_move(deepcopy(parent.board),'u',parent.l_move)
    if flag:
        node = Puzzle(temp,parent.level+1,'u')
        queue_list.append(node)
    flag , temp = make_move(deepcopy(parent.board),'d',parent.l_move)
    if flag:
        node = Puzzle(temp,parent.level+1,'d')
        queue_list.append(node)
    flag , temp = make_move(deepcopy(parent.board),'r',parent.l_move)
    if flag: 
        node = Puzzle(temp,parent.level+1,'r')
        queue_list.append(node)

def Solution_problem(tree,level_limit=0):
    queue_list=[]
    queue_list.append(deepcopy(tree))

    while(len(queue_list)>0):
        if inversions(queue_list[-1].board)==0 and (queue_list[-1].board[0][0]==0 or queue_list[-1].board[3][3]==0):
            queue_list[-1].explored=True
            return queue_list
        if queue_list[-1].level<level_limit and queue_list[-1].explored==False:
            parent_converting(queue_list)
        else:
            k=  queue_list.pop(-1)
            del k
    return Solution_problem(tree,level_limit+1)
def parent(queue_list):

    queue_list[-1].explored=True
    parent=queue_list[-1]        
    flag , temp = make_move(deepcopy(parent.board),'l',parent.l_move)
    if flag:
        node = Puzzle(temp,parent.level+1,'l')
        queue_list.append(node)                      
    flag , temp = make_move(deepcopy(parent.board),'u',parent.l_move)
    if flag:
        node = Puzzle(temp,parent.level+1,'u')
        queue_list.append(node)
    flag , temp = make_move(deepcopy(parent.board),'d',parent.l_move)
    if flag:
        node = Puzzle(temp,parent.level+1,'d')
        queue_list.append(node)
    flag , temp = make_move(deepcopy(parent.board),'r',parent.l_move)
    if flag: 
        node = Puzzle(temp,parent.level+1,'r')
        queue_list.append(node)

def Solution(tree,level_limit=0):
    
    queue_list=[]
    queue_list.append(deepcopy(tree))

    while(len(queue_list)>0):
        Condition_problem(queue_list,level_limit)
    return Solution(tree,level_limit+1)
            
def possipuzzle_arraylities(col,row,puzzle_array,move,last_move):
    if move=='u':
        if row==0 or last_move=='d':
            return False, puzzle_array
        else:
            puzzle_array[row][col],puzzle_array[row-1][col] = puzzle_array[row-1][col] , puzzle_array[row][col]
            return True, puzzle_array 

    elif move=='l':
        if col==0 or last_move=='r':
            return False, puzzle_array
        else:
            puzzle_array[row][col],puzzle_array[row][col-1] = puzzle_array[row][col-1] , puzzle_array[row][col]
            return True, puzzle_array 

    elif move=='r':
        if col==3 or last_move=='l':
            return False, puzzle_array
        else:

            puzzle_array[row][col],puzzle_array[row][col+1] = puzzle_array[row][col+1] , puzzle_array[row][col]
            return True, puzzle_array
    else:
        if row==3 or last_move=='u':
            return False, puzzle_array
        else:
            puzzle_array[row][col],puzzle_array[row+1][col] = puzzle_array[row+1][col] , puzzle_array[row][col]
            return True, puzzle_array 



Start_function()

