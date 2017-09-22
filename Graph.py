# This class represents a directed graph using adjacency
# list representation
from collections import defaultdict
import timeit
class Graph:
    # Constructor
    def __init__(self,connections):

        # default dictionary to store graph
        self.graph_dic = defaultdict(list)
        self.addConnecion(connections)
    # function to add an edge to graph
    def addConnecion(self,connections):
        for item1,item2 in connections:
            self.addEdge(item1,item2)
    def addEdge(self, u, v):
        self.graph_dic[u].append(v)

def BFS_COLORING(graph,vertex_set):
    odd_set=[]
    even_set=[]
    # print("Subgraph Vertices:{value}").format(value=vertex_set)
    # visited = [False] * (len(graph.graph_dic))
    visited=[False]* (len(vertex_set))
    start_vertex=vertex_set[0]
    queue=[]
    queue.append(start_vertex)
    visited[vertex_set.index(start_vertex)]=True
    even_set.append(start_vertex)
    # print("Start vertex:{value}").format(value=start_vertex)
    level_counter=0
    while queue:
        s=queue.pop(0)
        level_counter=level_counter+1
        # print("Traversing vertex:{value1}, Adjacency List:{value2}").format(value1=s,value2=graph.graph_dic[s])
        if(len(graph.graph_dic[s])>0):
            for i in graph.graph_dic[s]:
                if i in vertex_set and visited[vertex_set.index(i)]==False:
                    if(level_counter%2==0):
                        even_set.append(i)
                    else:
                        odd_set.append(i)
                    queue.append(i)
                    visited[vertex_set.index(i)]=True
    # print("Odd Set:{value}").format(value=odd_set)
    # print("Even Set:{value}").format(value=even_set)
    if(len(odd_set)==0):
        return 1
    else:
        return BFS_COLORING(graph,odd_set)+BFS_COLORING(graph,even_set)

def comolete_graph(min_value,max_value,iteration_rate):
    output_file='complete_graph.csv'
    if (output_file):
        open(output_file, 'w').close();
    iterator_value = min_value
    with open(output_file,'a') as fileWrite:
        while(iterator_value<=max_value):
            connections=list()
            for i in range(0,iterator_value-1):
                for j in range(i+1,iterator_value):
                    connections.append((i,j))
            # print connections
            vertex_set=range(0,iterator_value)
            g=Graph(connections)
            start_time=timeit.default_timer()
            c_number=BFS_COLORING(g,vertex_set)
            end_time=timeit.default_timer()
            fileWrite.write(str(iterator_value)+','+str(c_number)+','+str(format(end_time-start_time,'.10f'))+'\n')
            print("For Complete graph of N={value1}, COLOR_R={value2}, Exection_time={value3}").format(value1=iterator_value,value2=c_number,value3=format(end_time-start_time,'.10f'))
            iterator_value=iterator_value+iteration_rate

def tree_graph(min_value, max_value,iteration_rate):
    # print('In graph function')
    iteration_value=min_value
    output_file='tree_graph.csv'
    if (output_file):
        open(output_file, 'w').close();
    with open(output_file,'a') as fileWrite:
        while(iteration_value<=max_value):
            connections=list()
            for i in range(0,iteration_value-1):
                connections.append((i,i+1))
            vertex_set=range(0,iteration_value)
            g = Graph(connections)
            start_time = timeit.default_timer()
            c_number = BFS_COLORING(g, vertex_set)
            end_time = timeit.default_timer()
            fileWrite.write(str(iteration_value) + ',' + str(c_number) + ',' + str(format(end_time - start_time, '.10f')) + '\n')
            print("For tree Graph of N={value1}, COLOR_R={value2}, Exection_time={value3}").format(value1=iteration_value,
                                                                                     value2=c_number, value3=format(
                    end_time - start_time, '.10f'))
            iteration_value=iteration_value+iteration_rate

def regular_graph(min_value,max_value_iteration_rate):
    pass
if __name__ == '__main__':

    vertex_set=[1,2,3,4,5,6]
    # print(g.graph_dic)
    # print BFS_COLORING(g,vertex_set)
    # comolete_graph(10,500,10)
    # connections=[(1,2),(1,3),(2,6),(6,5),(3,4),(4,5)]
    # g=Graph(connections)
    # print BFS_COLORING(g,vertex_set)
    tree_graph(100,10000,100)
