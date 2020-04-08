import random
graph = {
    (1,2) : 1,
    (1,5) : 2,
    (1,6) : 9,
    (2,1) : 1,
    (2,6) : 4,
    (2,3) : 2,
    (2,4) : 6,
    (3,2) : 2,
    (3,4) : 3,
    (4,2) : 6,
    (4,3) : 3,
    (4,5) : 5,
    (5,1) : 2,
    (5,4) : 5,
    (5,6) : 7,
    (6,1) : 9,
    (6,2) : 4,
    (6,5) : 7
}
def find_weight(graph, set1, set2):
    weight = 0
    for s1 in set1:
        for s2 in set2:
            if (s1,s2) in graph:
                weight += graph[(s1,s2)]
    
    return weight

def heuristic1(set1, set2):
    node1 = random.randint(0, len(set1)-1)
    node2 = random.randint(0, len(set2)-1)

    temp = set1[node1]
    set1[node1] = set2[node2]
    set2[node2] = temp 

    return set1, set2 

def heuristic2(graph, set1, set2):
    heaviest_edge = -1
    i = 0
    j = 0
    ix = 0
    jx = 0
    for s1 in set1:
        j = 0
        for s2 in set2:
            if (s1,s2) in graph:
                if graph[(s1,s2)] > heaviest_edge:
                    heaviest_edge = graph[(s1,s2)]
                    ix = i
                    jx = j 
            j += 1
        i += 1
    jx = len(set2)-1-jx 
    temp = set1[ix]
    set1[ix] = set2[jx]
    set2[jx] = temp 

    return set1, set2 

def first_choice_hill_climbing(graph, limit):
    
    nodes = set()
    for key in graph:
        nodes.add(key[0])
        nodes.add(key[1])

    #generating initial states randomly 
    set_length = int(len(nodes)/2) 
    temp = set()
    temp = temp | nodes 
    set1 = [] #calling set but actually list
    set2 = []
    for i in range(0, set_length):
        set1.append(temp.pop())
    for i in range(set_length, len(nodes)):
        set2.append(temp.pop())

    count = 0
    neighbor_set1 = []
    neighbor_set2 = []
    i = 0
    while(True):
        for i in range(0, limit):
            toss = random.random()
            if toss < 0.5:
                neighbor_set1, neighbor_set2 = heuristic1(set1, set2)
            else:
                neighbor_set1, neighbor_set2 = heuristic2(graph, set1, set2)
            
            if find_weight(graph, neighbor_set1, neighbor_set2) < find_weight(graph, set1, set2):
                break

        if i == limit-1:
            return set1, set2 
        set1 = neighbor_set1
        set2 = neighbor_set2
        count += 1
               
if __name__ == "__main__":

    print(first_choice_hill_climbing(graph, 1000))

