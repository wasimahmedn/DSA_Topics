class AdjMatrix:
    def __init__(self,num_vertices:int)->None:
        """This class will create,remove, and print the nodes in adjucency matrix

        Args:
            num_vertices (int): number of vertices.
        """
        self.num_vertices=num_vertices
        self.matrix=[[0 for _ in range(self.num_vertices)] for _ in range(self.num_vertices)]
    
    def add_node(self,v:int,u:int)->None:
        """adds the node to the adjucency matrix

        Args:
            v (int): node_1
            u (int): node_2
        """
        if u<self.num_vertices and v<self.num_vertices:
            self.matrix[v][u]=1
            self.matrix[u][v]=1
    
    def remove_node(self,v:int,u:int)->None:
        """removes the node the adjucency matrix

        Args:
            v (int): node_1
            u (int): node_2
        """ 
        if u<self.num_vertices and v<=self.num_vertices:
            self.matrix[v][u]=0
            self.matrix[u][v]=0
    
    def print_adj_matrix(self):
        for row in self.matrix:
            print(row)

def main():
    graph=AdjMatrix(5)
    graph.add_node(0,1)
    graph.add_node(0,2)
    graph.add_node(1,2)
    graph.add_node(2,0)
    graph.add_node(2,3)
    graph.remove_node(2,3)
    graph.print_adj_matrix()

if __name__=="__main__":
    main()