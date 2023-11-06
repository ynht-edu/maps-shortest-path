from queue import PriorityQueue
import random
from rich import print
from rich.console import Console
from rich.table import Table
from rich.align import Align
from rich.live import Live
import os


inf = 99999999
N = int(input("Masukkan jumlah kota atau simpangan: "))
E = int(input("Masukkan jumlah jalan: "))
print()
index = {}
print("Masukkan kota atau simpangan:")
for i in range(1, N + 1):
    node = input()
    index[node] = i
    index[i] = node
print()
Start_input = input("Dimulai dari? ")
Start = index[Start_input]
End_input = input("Mau ke mana? ")
End = index[End_input]
V_avg = int(input("Masukkan kelajuan rata-rata (dalam km/jam): "))
print()
distance_adj_list = [[] for i in range(N + 1)]
time_adj_list = [[] for i in range(N + 1)]
dpred = [-1 for i in range(N + 1)]
tpred = [-1 for i in range(N + 1)]
q = PriorityQueue()


def print_dest_dist_route(distance):
    time_sum = 0.000000000
    node_counter = 1
    routes = [End]
    j = End
    while dpred[j] != -1:
        time_sum += weight_search(dpred[j], j, time_adj_list)
        node_counter += 1
        j = dpred[j]
        routes.append(j)
    hours = int(time_sum)
    minutes = int((time_sum - hours) * 60)
    seconds = int(((time_sum - hours) * 60 - minutes) * 60)
    routes_string = ""
    for i in range(node_counter - 1, 0, -1):
        routes_string += index[routes[i]] + " --> "
    routes_string += index[routes[0]]

    console = Console()
    table = Table(title="Rute Destinasi dengan Jarak Terdekat", show_footer=False)
    table_centered = Align.center(table)
    with Live(table_centered, console=console, screen=False):
        table.add_column("Tujuan", style="yellow1", no_wrap=True)
        table.add_column("Rute", style="light_goldenrod1", no_wrap=True)
        table.add_column("Jarak", style="khaki1", no_wrap=True)
        table.add_column("Waktu Tempuh", style="wheat1", no_wrap=True)
        table.add_row(
            f"{index[routes[0]]}",
            routes_string,
            f"{distance[End]} km",
            f"{hours} jam {minutes} menit {seconds} detik",
        )
        table_width = console.measure(table).maximum
        table.width = None


def print_dist_route(distance):
    console = Console()
    table = Table(title="Rute Lain dengan Jarak Terdekat:", show_footer=False)
    table.add_column("Tujuan", style="green1", no_wrap=True)
    table.add_column("Rute", style="spring_green2", no_wrap=True)
    table.add_column("Jarak", style="spring_green1", no_wrap=True)
    table.add_column("Waktu tempuh", style="cyan2", no_wrap=True)

    for i in range(1, N + 1):
        if i == Start or i == End:
            continue
        j = i
        time_sum = 0.000000000
        node_counter = 1
        routes = [i]
        while dpred[j] != -1:
            time_sum += weight_search(dpred[j], j, time_adj_list)
            node_counter += 1
            j = dpred[j]
            routes.append(j)
        route_string = ""
        time_string = ""
        dist_string = ""
        hours = int(time_sum)
        minutes = int((time_sum - hours) * 60)
        seconds = int(((time_sum - hours) * 60 - minutes) * 60)
        time_string = f"{hours} jam {minutes} menit {seconds} detik"
        dist_string = f"{distance[i]} km"
        for k in range(node_counter - 1, 0, -1):
            route_string += index[routes[k]] + " --> "
        route_string += index[routes[0]]
        table.add_row(index[routes[0]], route_string, dist_string, time_string)

    table_centered = Align.center(table)

    with Live(table_centered, console=console, screen=False):
        table_width = console.measure(table).maximum

        table.width = None


def print_dest_time_route(time):
    j = End
    distance_sum = 0
    node_counter = 1
    routes = [End]
    routes_string = ""
    hours = int(time[End])
    minutes = int((time[End] - hours) * 60)
    seconds = int(((time[End] - hours) * 60 - minutes) * 60)
    while tpred[j] != -1:
        distance_sum += weight_search(tpred[j], j, distance_adj_list)
        node_counter += 1
        j = tpred[j]
        routes.append(j)
    for k in range(node_counter - 1, 0, -1):
        routes_string += index[routes[k]] + " --> "
    routes_string += index[routes[0]]

    console = Console()
    table = Table(
        title="Rute Destinasi dengan Waktu Tempuh Tercepat", show_footer=False
    )
    table_centered = Align.center(table)
    with Live(table_centered, console=console, screen=False):
        table.add_column("Tujuan", style="yellow1", no_wrap=True)
        table.add_column("Rute", style="light_goldenrod1", no_wrap=True)
        table.add_column("Jarak", style="khaki1", no_wrap=True)
        table.add_column("Waktu Tempuh", style="wheat1", no_wrap=True)
        table.add_row(
            f"{index[routes[0]]}",
            routes_string,
            f"{distance_sum} km",
            f"{hours} jam {minutes} menit {seconds} detik",
        )

        table_width = console.measure(table).maximum

        table.width = None


def print_time_route(time):
    console = Console()
    table = Table(title="Rute Lain dengan Waktu Tempuh Tercepat:", show_footer=False)
    table.add_column("Tujuan", style="green1", no_wrap=True)
    table.add_column("Rute", style="spring_green2", no_wrap=True)
    table.add_column("Jarak", style="spring_green1", no_wrap=True)
    table.add_column("Waktu tempuh", style="cyan2", no_wrap=True)

    for i in range(1, N + 1):
        j = i
        if i == Start or i == End:
            continue
        distance_sum = 0
        node_counter = 1
        routes = [i]
        routes_string = ""
        hours = int(time[i])
        minutes = int((time[i] - hours) * 60)
        seconds = int(((time[i] - hours) * 60 - minutes) * 60)
        while tpred[j] != -1:
            distance_sum += weight_search(tpred[j], j, distance_adj_list)
            node_counter += 1
            j = tpred[j]
            routes.append(j)
        dist_string = f"{distance_sum} km"
        time_string = f"{hours} jam {minutes} menit {seconds} detik"
        for k in range(node_counter - 1, 0, -1):
            routes_string += index[routes[k]] + " --> "
        routes_string += index[routes[0]]
        table.add_row(index[i], routes_string, dist_string, time_string)

    table_centered = Align.center(table)
    with Live(table_centered, console=console, screen=False):
        table_width = console.measure(table).maximum
        table.width = None


def weight_search(a, b, arr):
    for i in arr[a]:
        if b == i[0]:
            return i[1]


def add_distance_adj(a, b, w):
    distance_adj_list[index[a]].append([index[b], w])


def add_time_adj(a, b, s):
    t = float(float(s) / float(V_avg))
    time_adj_list[index[a]].append([index[b], t])


def add_traffic_jam(total_con):
    console = Console()
    table = Table(title="Data Kemacetan", show_footer=False)
    table.add_column("Dari", style="red1", no_wrap=True)
    table.add_column("ke", style="deep_pink2", no_wrap=True)
    table.add_column("Jarak", style="deep_pink1", no_wrap=True)
    table.add_column("Kelajuan Rata-Rata Kendaraan", style="magenta2", no_wrap=True)

    added = [[False for j in range(N + 1)] for i in range(N + 1)]
    for i in range(total_con):
        a = random.randint(1, N)
        if not distance_adj_list[a]:
            continue
        cont = random.choice(distance_adj_list[a])
        b = cont[0]
        b_index = -1
        dist = cont[1]
        if added[a][b]:
            continue
        counter = 0
        for j in distance_adj_list[a]:
            if b == j[0]:
                b_index = counter
            counter += 1
        added[a][b] = True
        v = random.randint(1, V_avg - 1)
        x = random.randint(1, dist)
        t = float((dist - x) / V_avg + x / v)
        time_adj_list[a][b_index][1] = t
        table.add_row(index[a], index[b], str(x) + " km", str(v) + " km/jam")

    table_centered = Align.center(table)
    with Live(table_centered, console=console, screen=False):
        table_width = console.measure(table).maximum

        table.width = None


def distance_dijkstra(N, S):
    distance = [inf for x in range(N + 1)]
    visited = [False for x in range(N + 1)]
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
    time = [inf for x in range(N + 1)]
    visited = [False for x in range(N + 1)]
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


print(
    "Masukkan rute dan jarak (dalam km): \n\[dari] \[ke] \[jarak] \nex: ciamis tasikmalaya [grey85]20[/grey85] \n"
)
for i in range(E):
    a, b, w = input().split()
    add_distance_adj(a, b, int(w))
    add_time_adj(a, b, int(w))

print()
global_distance = distance_dijkstra(N, Start)
response = input("Apakah ada kemacetan? \nKetik 1 untuk ya \nKetik 2 untuk tidak \n")
os.system("cls")
os.system("cls")
if response == "1":
    total = random.randint(1, E)
    add_traffic_jam(total)
    print("\n")
    print_dest_dist_route(global_distance)
    print()
    print_dist_route(global_distance)
    print()
    time = time_dijkstra(N, Start)
    print_dest_time_route(time)
    print()
    print_time_route(time)
    print()

elif response == "2":
    print_dest_dist_route(global_distance)
    print()
    print_dist_route(global_distance)
