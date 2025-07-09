class MemoryNode:
    def __init__(self, memory_id, title, details, emotion):
        self.id = memory_id
        self.title = title
        self.details = details
        self.emotion = emotion
        self.connections = set()

    def connection(self, other_node_id):
        self.connections.add(other_node_id)

    def __str__(self):
        return f"[{self.emotion.upper()}]{self.title}: {self.details}"


class MemoryGraph:
    def __init__(self):
        self.memories = {}

    def add_memory(self, memory_id, title, details, emotion):
        if memory_id in self.memories:
            raise ValueError("Memory ID already exists.")
        self.memories[memory_id] = MemoryNode(memory_id, title, details, emotion)

    def connect_memories(self, id1, id2):
        if id1 in self.memories and id2 in self.memories:
            self.memories[id1].connection(id2)  # Fixed method name
            self.memories[id2].connection(id1)  # Fixed method name
        else:
            raise ValueError("One or both memory IDs do not exist.")

    def get_memory(self, memory_id):
        return self.memories.get(memory_id)

    def list_memories(self):
        return list(self.memories.values())


# Main function should be outside the class
def main():
    graph = MemoryGraph()
    graph.add_memory(1, "First Day", "I felt anxious about starting.", "anxiety")
    graph.add_memory(2, "Second Day", "I started working on a project.", "determined")
    graph.add_memory(3, "Third Day", "I succeeded in completing the project.", "happy")
    graph.connect_memories(1, 2)
    graph.connect_memories(1, 3)

    for mem in graph.list_memories():
        print(mem)


if __name__ == "__main__":
    main()