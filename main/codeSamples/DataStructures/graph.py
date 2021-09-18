class Graph:
    
    graph_dict={}
    
    def addEdge(self,node,neighbour):  
        if node not in self.graph_dict:
            self.graph_dict[node]=[neighbour]
        else:
            self.graph_dict[node].append(neighbour)
            
    def show_edges(self):
        for node in self.graph_dict:
            neighbours = ""
            for neighbour in self.graph_dict[node]:
                neighbours += "{} ".format(neighbour)
            print("{} --> {}".format(node, neighbours))
    
    def find_path(self,start,end,path=[]):
        path = path + [start]    
        if start==end:
            return path
        for node in self.graph_dict[start]:
            if node not in path:
                newPath=self.find_path(node,end,path)
                if newPath:
                    return newPath
                return None
            

g= Graph()
g.addEdge('1', '2')
g.addEdge('1', '3')
g.addEdge('1', '4')
g.addEdge('2', '1')
g.addEdge('2', '4')
g.addEdge('3', '1')
g.addEdge('3', '4')
g.addEdge('4', '1')
g.addEdge('4', '2')
g.addEdge('4', '3')
g.show_edges()
print(g.find_path('3', '2'))
