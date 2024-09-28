class Graph:
    #adjacency list
    def __init__(self) :
        #creating an empty dictionary
        self.graph={}
        self.directed= False
    def addVertex(self,vertex):
        #if a vertex is not present define with empty dictionary
        if vertex  not in self.graph:
            self.graph[vertex]=[]
    def addEdge(self,src,desti):
        #source and destination vertex to be defined
        self.addVertex(src)
        self.addVertex(desti)
        #adding destination vertex to the source vertex in the list 
        self.graph[src].append(desti)
        #if the graph is undirected add reverse node 
        if not self.directed:
            self.graph[desti].append(src)
    def printGraph(self):
            for vertex in self.graph:
                print(f"{vertex}: {self.graph[vertex]}")
    if __name__ =="__main__":
            
    
            #creating the graph
            G = Graph()

            G.addEdge('A','B')
            G.addEdge('A','C')
            G.addEdge('B','C')
            G.addEdge('B','G')
            G.addEdge('B','F')
            G.addEdge('C','B')
            G.addEdge('C','E')
            G.addEdge('C','D')
            #display the graph
            G.printGraph()
            
            
    
                

            

            

            


        


       
    