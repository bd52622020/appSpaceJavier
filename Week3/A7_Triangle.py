def check_edge(c1, c2):
    min_c = min(c1,c2)
    max_c = max(c1, c2)
    
    print("The maximun longitude of the edge is ", max_c + min_c)
    print("The minimun longitude of the edge is ", max_c - min_c)
    
    
check_edge(4, 8)