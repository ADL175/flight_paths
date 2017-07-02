"""Creates a Graph data structure"""


class Graph(object):
    """Define the Link_List class structure"""
    def __init__(self):
        """Make an empty dictionary."""
        self.graph_dict = {}

    def add_node(self, value):
        """Check if node of given value exists in dictionary.
        If not, add it with an empty list."""
        try:
            self.graph_dict[value]
        except KeyError:
            self.graph_dict[value] = []

    def add_edge(self, val1, val2, weight=0):
        """Ensure that nodes of val1 and val2 exist (creating them if they don't.
        Then make an edge connecting val1 to val2."""
        if [val1, val2, weight] not in self.edges():
            self.add_node(val1)
            self.add_node(val2)
            self.graph_dict[val1].append([val2, weight])
        else:
            raise KeyError("Can't add edge, edge already exists.")

    def nodes(self):
        """Return a list of all keys in dictionary."""
        to_return = []
        for keys, values in self.graph_dict.items():
            to_return.append(keys)
        return to_return

    def edges(self):
        """Return a list of all edges in dictionary."""
        to_return = []
        for keys, values in self.graph_dict.items():
            for i in values:
                to_return.append([keys, i[0], i[1]])
        return to_return

    def del_node(self, val):
        """Deletes a node from the graph, and from all edge pointers."""
        try:
            del self.graph_dict[val]
            for keys, values in self.graph_dict.items():
                for i in values:
                    if i[0] == val:
                        values.remove(i)
        except KeyError:
            raise KeyError("No such node exists.")

    def del_edge(self, val1, val2):
        """Deletes an edge from graph."""
        try:
            for node in self.graph_dict[val1]:
                if node[0] == val2:
                    self.graph_dict[val1].remove(node)
        except ValueError:
            raise ValueError("No such edge exists.")
        except KeyError:
            raise KeyError("No such node exists.")

    def has_node(self, val):
        """Checks if graph has a given node in it."""
        try:
            self.graph_dict[val]
            return True
        except KeyError:
            return False

    def neighbors(self, val):
        """Return all nodes connected to given node."""
        try:
            return self.graph_dict[val]
        except KeyError:
            raise KeyError("No such node exists.")

    def adjacent(self, val1, val2):
        """Return True if edge exists, else return false."""
        try:
            self.graph_dict[val2]
            for node in self.graph_dict[val1]:
                if node[0] == val2:
                    return True
            else:
                return False
        except KeyError:
            raise KeyError("Value given not in graph.")

    def depth(self, val):
        from stack import Stack
        seen = []
        next_up = Stack()
        try:
            while True:
                if val not in seen:
                    seen.append(val)
                    for i in self.graph_dict[val][::-1]:
                        next_up.push(i)
                if len(next_up) == 0:
                    break
                val = next_up.pop().value[0]
            return seen
        except KeyError:
            raise KeyError('Given value does not exist.')

    def breadth(self, val):
        from que_ import Queue
        seen = []
        next_up = Queue()
        try:
            while True:
                if val not in seen:
                    seen.append(val)
                    for i in self.graph_dict[val]:
                        next_up.enqueue(i)
                if next_up.size() == 0:
                    break
                val = next_up.dequeue().value[0]
            return seen
        except KeyError:
            raise KeyError('Given value does not exist.')

    def dijkstra(self, val1):
        from priorityq import Priority_Q
        the_list = self.breadth(val1)
        the_queue = Priority_Q()
        to_return = []
        for i in the_list:
            if i == val1:
                the_queue.insert(i, self.graph_dict[i], 0)
            else:
                the_queue.insert(i, self.graph_dict[i])
        while len(the_queue.heap.heap) > 0:
            current = the_queue.pop()
            for neighbor in current['neighbors']:
                alt = current['dist'] + neighbor[1]
                print('at node ', current['value'])
                print(alt, neighbor[0])
                the_queue.decrease_priority(neighbor[0], alt, current['value'])
            to_return.append(current)
        return to_return

    def bellman_ford(self, vertices, list_edges, vertex_source):
        print(list_edges)
        distance = {}
        predecessor = {}
        for vertex_v in vertices:
            # print(vertex_v)
            distance[vertex_v] = float('inf')
            predecessor[vertex_v] = None
        distance[vertex_source] = 0
        for i in range(len(vertices)):
            for ji in list_edges:
                if distance[ji[0]] + ji[2] < distance[ji[1]]:
                    distance[ji[1]] = distance[ji[0]] + ji[2]
                    predecessor[ji[1]] = ji[0]
        for i in list_edges:
            if distance[i[0]] + i[2] < distance[i[1]]:
                raise ValueError('Graph contains a negative-weight cycle')
        return distance, predecessor

if __name__ == '__main__':
