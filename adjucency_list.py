class adjList:
    def __init__(self,num_vertices:int)->None:
        self.num_vertices=num_vertices
        self.adjArray=[[] for _ in range(self.num_vertices)]
    
    def add_node(self,v:int,u:int)->None:
        """Adds the node to the adjucency list

        Args:
            v (int): node_1
            u (int): node_2
        """
        if v<self.num_vertices and u<self.num_vertices:
            # if u not in self.adjArray[v]:
            self.adjArray[v].append(u)
            # if v not in self.adjArray[u]:
            self.adjArray[u].append(v)
    
    def remove_node(self,v:int,u:int)->None:
        """removes the node from adjucency list

        Args:
            v (int): node_1
            u (int): none_2
        """
        if v<self.num_vertices and u<self.num_vertices:
            self.adjArray[v].remove(u)
            self.adjArray[u].remove(v)
    

    def print_adj_list(self)->None:
        """Prints the adjucency array
        """
        for id,node in enumerate(self.adjArray):
            if len(node):
                node.append('null')
            else:
                node=['null']
            print(f"{id}->{'->'.join(list(map(lambda x: str(x),node)))}")



def main():
    graph=adjList(5)
    graph.add_node(0,1)
    graph.add_node(0,2)
    graph.add_node(1,2)
    graph.add_node(2,0)
    graph.add_node(2,3)
    graph.remove_node(2,3)
    graph.print_adj_list()


if __name__=="__main__":
    main()