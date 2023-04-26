import matplotlib.pyplot as plt


def plot_graph_label(T,bellow):
    plt.plot(list(range(len(T))),T,'k', linewidth=4)
    for x,y in zip(list(range(len(T))),T):
        off = 30
        if y in bellow:
            off = -40
        plt.annotate(str(y), (x,y),
                 textcoords="offset points", # how to position the text
                 xytext=(0,off), # distance from text to points (x,y)
                 ha='center',
                 fontsize=40)
    plt.axis('off')
    #plt.tight_layout()
    plt.show()


P = [1, 5, 3, 4, 6, 2]
T = [2, 7, 4, 5, 8, 3, 1, 20, 15, 16, 25, 6]
#plot_graph_label(T,{1,15,16,6})
plot_graph_label(P,{1,2})