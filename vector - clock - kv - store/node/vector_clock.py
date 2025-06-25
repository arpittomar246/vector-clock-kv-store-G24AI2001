
class VectorClock:
    def __init__(self, node_id, nodes):
        self.clock = {n: 0 for n in nodes}
        self.node_id = node_id

    def increment(self):
        self.clock[self.node_id] += 1

    def update(self, received_clock):
        for node, timestamp in received_clock.items():
            self.clock[node] = max(self.clock[node], timestamp)

    def is_causally_ready(self, received_clock, sender):
        for node in self.clock:
            if node == sender:
                if received_clock[node] != self.clock[node] + 1:
                    return False
            else:
                if received_clock[node] > self.clock[node]:
                    return False
        return True

    def get(self):
        return dict(self.clock)
