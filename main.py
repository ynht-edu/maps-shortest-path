from queue import PriorityQueue
import random
from input1 import N, E
from input2 import index
from input3 import Start_input, End_input, V_avg
from input4 import dari, ke, jarak, response

inf = 99999999

print()
Start = index[Start_input]
End = index[End_input]
distance_adj_list = [[] for i in range (N+1)]
time_adj_list = [[] for i in range (N+1)]
dpred = [-1 for i in range(N+1)]
tpred = [-1 for i in range(N+1)]
q = PriorityQueue()

def print_dist_route(distance):
    for i in range(1, N+1):
        j=i
        if(i == Start):
            continue
        time_sum = 0.000000000
        node_counter = 1
        routes = [i]
        while dpred[j] != -1:
            time_sum += weight_search(dpred[j], j, time_adj_list)
            node_counter += 1
            j = dpred[j]
            routes.append(j)
        hours = int(time_sum)
        minutes = int((time_sum-hours)*60)
        seconds = int(((time_sum-hours)*60 - minutes)*60)
        print(f"Rute terpendek dari {Start_input} ke {index[i]}:")
        print(f"[{hours} jam {minutes} menit {seconds} detik][{distance[i]} km]")
        for i in range (node_counter-1, 0, -1):
            print(index[routes[i]], end= " --> ")
        print(index[routes[0]], end=" ")
        print()

def print_time_route(time):
    for i in range(1, N+1):
        j=i
        if(i == Start):
            continue
        distance_sum = 0
        node_counter = 1
        routes = [i]
        hours = int(time[i])
        minutes = int((time[i]-hours)*60)
        seconds = int(((time[i]-hours)*60 - minutes)*60)
        print(f"Rute tercepat dari {Start_input} ke {index[i]}:")
        while tpred[j] != -1:
            distance_sum += weight_search(tpred[j], j, distance_adj_list)
            node_counter += 1
            j = tpred[j]
            routes.append(j)
        print(f"[{hours} jam {minutes} menit {seconds} detik][{distance_sum} km]")
        for i in range (node_counter-1, 0, -1):
            print(index[routes[i]], end= " --> ")
        print(index[routes[0]], end=" ")
        print()

def weight_search(a, b, arr):
    for i in arr[a]:
        if(b == i[0]):
            return i[1]

def add_distance_adj(a, b, w):
    distance_adj_list[index[a]].append([index[b], w])

def add_time_adj(a, b, s):
    t = float(float(s)/float(V_avg))
    time_adj_list[index[a]].append([index[b], t])

def add_con(total_con): 
    added = [[False for j in range (N+1)] for i in range (N+1)]
    for i in range(total_con):
        a = random.randint(1, N)
        if(not distance_adj_list[a]):
            continue
        cont = random.choice(distance_adj_list[a])
        b = cont[0]
        b_index = -1
        dist = cont[1]
        if(added[a][b]):
            continue
        counter = 0
        for i in distance_adj_list[a]:
            if(b == i[0]):
                b_index = counter
            counter+=1
        added[a][b] = True
        v = random.randint(1, V_avg-1)
        x = random.randint(1, dist)
        t = float((dist-x)/V_avg + x/v)
        time_adj_list[a][b_index][1] = t
        print(f"Terjadi kemacetan dari {index[a]} ke {index[b]} sejauh {x} km dengan kelajuan rata-rata kendaraaan {v} km/jam")

def distance_dijkstra(N, S):
    distance = [inf for x in range(N+1)]
    visited = [False for x in range(N+1)]
    distance[S] = 0
    q.put([0, S])
    while not q.empty():
        a = q.queue[0][1]
        q.get()
        if visited[a]:
            continue
        visited[a] = True
        for i in distance_adj_list[a]:
            b = i[0]
            w = i[1]
            if distance[a] + w < distance[b]:
                dpred[b] = a
                distance[b] = distance[a] + w
                q.put([distance[b], b])
    return distance

def time_dijkstra(N, S):
    time = [inf for x in range(N+1)]
    visited = [False for x in range(N+1)]
    time[S] = 0
    q.put([0, S])
    while not q.empty():
        a = q.queue[0][1]
        q.get()
        if visited[a]:
            continue
        visited[a] = True
        for i in time_adj_list[a]:
            b = i[0]
            w = i[1]
            if time[a] + w < time[b]:
                tpred[b] = a
                time[b] = time[a] + w
                q.put([time[b], b])
    return time


for i in range(E):
    a, b, w = dari[i], ke[i], int(jarak[i])
    add_distance_adj(a, b, int(w))
    add_time_adj(a, b, int(w))

if response == 1:
    total = random.randint(1, E)
    print()
    add_con(total)
    global_distance = distance_dijkstra(N, Start)
    print()
    print_dist_route(global_distance)
    print()
    time = time_dijkstra(N, Start)
    print_time_route(time)
    
else:
    global_distance = distance_dijkstra(N, Start)
    print()
    print_dist_route(global_distance)
print()