def bfs(graph,start):
    visit=[]
    queue=[start]
    visit=[start]
    while(queue):
        ele=queue.pop(0)
        print(ele,end=' ')
        for i in graph[ele]:
            if i not in visit:
                queue.append(i)
                visit.append(i)

graph={"A":["B","C"],
       "B":["A","C","D"],
       "C":["A","B","E","F"],
       "D":["B","E"],
       "E":["C","D","G"],
       "F":["C","G"],
       "G":["E","F"]}
bfs(graph,"A")