
class AdjNode:
    def __init__(self, data,w):
        self.vertex = data
        self.weight = w
        self.next = None
class Graph:
    def __init__():
        print("I am called")
    def __init__(n,digraph):
        return False
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V
    def add_edge(self, src, dest,w):
        node = AdjNode(dest,w)
        node.next = self.graph[src]
        self.graph[src] = node
        node = AdjNode(src,w)
        node.next = self.graph[dest]
        self.graph[dest] = node
    def isDirect():
        return False
    def adjacent(self,v, u):
        temp = self.graph[v]
        while temp:
            if(temp.vertex == u):
                return True
            temp = temp.next
        return False
    def neighbors(self,v):
        temp = self.graph[v]
        while temp:
            print(" -> {}".format(temp.vertex),end="")
            temp=temp.next
    def addVertex(self,v):
        for i in range(self.V):
            temp = self.graph[i]
            if temp.vertex == v:
                return
        self.graph.append(v)
    def removeVertex(self,v):
        for i in range(Self.V):
            temp = self.graph[i]
            if temp.vertex == v:
                del self.graph[i]
                return
    def addEdge(self,v, u,w=0):
        add_edge(v, u,w)
    def addEdges(self,v, u,w):
        addEdge(v, u,w)
    def removeEdge(self,v, u):
        temp = self.graph[i]
        while temp:
            if (temp.next.value == u):
                if(temp.next.next !=null):
                    temp.next = temp.next.next
                temp.next = null
            temp = temp.next
    def getWeight(v, u):
        temp = self.graph[v]
        while temp:
            if(temp.value == u):
                return temp.weight
            temp = temp.next
        print("doesn't exit any edge between them")
    def setWeight(self,v, u,w):
        print(v)
        temp = self.graph[v]
        while temp:
            if(temp.vertex == u):
                temp.weight = w  ### setting weight 2 between v and u
            temp = temp.next
        print("doesn't exit any edge between them")
    def isEmpty(self):
        if (len(self.graph) == 0):
            return True
        return False
    def vertices(self):
        list_of_vertice =[]
        for i in range(self.V):
            list_of_vertice.append(self.graph[i].vertex)
        return list_of_vertice
    def edges(self):
        counter =0
        edges_of_list= []
        collection=[]
        for i in range(self.V):
            temp = self.graph[i]
            while temp:
                collection.append(temp.vertex)
                temp = temp.next
                counter = counter +1
            edges_of_list.append(collection)
        return edges_of_list   # list of list means 2D list
    def degree(self,v):
        temp = self.graph[v]
        counter =0
        while temp:
            counter = counter + 1
            temp = temp.next
        return counter
    def size(self):
        return (len(Self.graph))
    def nEdges(self):
        counter =0
        for i in range(self.V):
            temp = self.graph[i]
            while temp:
                temp = temp.next
                counter = counter +1
        return counter
    def clear(self):
        del self.graph
        graph = Graph(5)
    def vertexExists(self,v):
        for i in range(self.V):
            if i == v:
                return True
        return False
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex),end="")
                temp = temp.next
            print(" \n")
 
 
# Driver program to the above graph class
if __name__ == "__main__":
    V = 5
    # graph = Graph(V)
    # graph.add_edge(0, 1,2)
    # graph.add_edge(0, 4,2)
    # graph.add_edge(1, 2,2)
    # graph.add_edge(1, 3,2)
    # graph.add_edge(1, 4,2)
    # graph.add_edge(2, 3,2)
    # graph.add_edge(3, 4,2)
    # graph.print_graph()
    file = open('graph.txt', 'r')
    counter =0
    V =0
    listing =[]
    for each in file:
        if counter ==0:
            V = int(each)
        else:
            a = each.split(',')
            listing.append(a)
        counter = counter +1
    graph = Graph(V)
    for i in range(0,len(listing)):
        graph.add_edge(int (listing[i][0]),int (listing[i][1]),int(listing[i][2]))
    graph.print_graph()
    print(graph.nEdges())
    graph.adjacent("a","f")
    graph.getWeight,("b","h")
    print(graph.degree("c"))
    listing =graph.vertices()
    print(listing)
    graph.addVertex("k")
    graph.add_edge("k","a",5)
    graph.add_edge("g", "k", 2)
    graph.setWeight("a", "c", 7)
    graph.print_graph()