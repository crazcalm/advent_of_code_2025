import fileinput
from pprint import pprint

from copy import deepcopy

class Node:
    def __init__(self, x, y, z, id_):
        self.x = x
        self.y = y
        self.z = z
        self.id_ = id_
        self.connections = set()

    def add_connection(self, node_id):
        self.connections.add(node_id)
        
    def distance_from(self, other):
        return (self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2
        
    def __lt__(self, other):
        return self.x + self.y + self.x < other.x + other.y + other.z

    def __repr__(self):
        return f"Node({self.x}, {self.y}, {self.z} -- id ({self.id_}), connections: {self.connections})"


class Distance:
    def __init__(self, id_1, id_2, distance):
        self.id_1 = id_1
        self.id_2 = id_2
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance

    def __eq__(self, other):
        return set(self.id_1, self.id_2) == set(other.id_1, other.id_2)

    def __repr__(self):
        return f"Distance(node_id_1({self.id_1}), node_id_2({self.id_2}), distance({self.distance}))"


def is_connected(id_1, id_2, nodes, seen=None):
    result = False
    seen = set() if seen is None else seen
    
    if id_1 in nodes[id_2].connections:
        return True

    seen.add(id_2)
    for node_id in nodes[id_2].connections:
        if node_id in seen:
            continue
        if is_connected(id_1, node_id, nodes, seen):
            result = True
            break
        else:
            seen.add(node_id)

    return result

def count_connections(node_id, nodes, seen=None):
    node = nodes[node_id]
    seen = set() if seen is None else seen
    seen.add(node.id_)

    for node_id in node.connections:
        if node_id in seen:
            continue
        count_connections(node_id, nodes, seen)

    return len(seen)

def get_connections(node_id, nodes, seen=None):
    node = nodes[node_id]
    seen = set() if seen is None else seen
    seen.add(node.id_)

    for node_id in node.connections:
        if node_id in seen:
            continue
        count_connections(node_id, nodes, seen)

    return seen


def main():
    nodes = {}
    distances = []
    
    for index, line in enumerate(fileinput.input(), start=1):
        line = line.strip()
        if not line:
            break

        x, y, z = line.split(",")
        nodes[index] = Node(int(x), int(y), int(z), index)

    pprint(nodes)

    seen_dis = set()
    for id_1, node_1 in nodes.items():
        for id_2, node_2 in nodes.items():
            if id_1 == id_2:
                continue

            if (id_1, id_2) in seen_dis:
                continue
            distance_value = node_1.distance_from(node_2)
            distances.append(Distance(node_1.id_, node_2.id_, distance_value))
            seen_dis.add((id_1, id_2))
            seen_dis.add((id_2, id_1))
            
    distances.sort()
    pprint(distances)

    count = 0
    for dis in distances:
        if count >= 1000:
            break
        
        node_1 = nodes[dis.id_1]
        node_2 = nodes[dis.id_2]

        if not is_connected(dis.id_1, dis.id_2, nodes):
            node_1.add_connection(dis.id_2)
            node_2.add_connection(dis.id_1)

        count += 1
    pprint(nodes)

    print(count_connections(2, nodes))
    connections = [(count_connections(node_id, nodes), node) for node_id, node in nodes.items()]

    connections.sort()
    connections.reverse()
    print("top 10 connections")
    pprint(connections[:10])

    new_count = 0
    result = 1
    seen = set()
    for connection_count, node in connections:
        if new_count >= 3:
            break
        
        if node.id_ in seen:
            continue

        result *= connection_count
        #print(result)
        for node_id in get_connections(node.id_, nodes):
            seen.add(node_id)
        new_count += 1
    print(result)

if __name__ == "__main__":
    main()
    
