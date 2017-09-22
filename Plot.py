import matplotlib.pyplot as plt

def plot_graph(data_file,title):
    plt.xscale('linear')
    x_values=[]
    y_values=[]
    with open(data_file,'r') as fileRead:
        for line in fileRead:
            x_values.append(int(line.split(',')[0]))
            y_values.append((float(line.split(',')[2])))
    plt.plot(x_values,y_values)
    plt.title('Graph Coloring Plot')
    plt.xlabel('Input Size')
    plt.ylabel('Execution_time(In Seconds)')
    plt.savefig(title+'.png')
    plt.close()

if __name__ == '__main__':
    plot_graph('complete_graph.csv','Complete')
    plot_graph('tree_graph.csv','Tree')

