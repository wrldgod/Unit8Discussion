from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    # Return an empty list if the starting node does not exist.
    if start not in graph:
        return []

    visited = set()
    queue = deque([start])
    traversal_order = []

    # A queue keeps nodes in the order they were discovered.
    while queue:
        current = queue.popleft()

        if current not in visited:
            visited.add(current)
            traversal_order.append(current)

            # Neighbors are added so BFS can visit them level by level.
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

    # BFS explores nearby nodes first, while DFS follows one path deeper first.
    return traversal_order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    # Each node represents a streaming category.
    # Each edge represents a relationship between similar content categories.
    graph = {
        "Action": ["Sci-Fi", "Thriller"],
        "Sci-Fi": ["Action", "Fantasy"],
        "Thriller": ["Action", "Crime"],
        "Fantasy": ["Sci-Fi", "Animation"],
        "Crime": ["Thriller", "Drama"],
        "Animation": ["Fantasy"],
        "Drama": ["Crime"]
    }

    print("\n=== GRAPH STRUCTURE ===")
    for node, neighbors in graph.items():
        print(node, "->", neighbors)

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")

    # BFS starts at Action and visits the closest connected categories first.
    start_node = "Action"
    print("Starting from Action:", bfs(graph, start_node))

    # Add a new category and connect it to Drama.
    graph["Comedy"] = ["Drama"]
    graph["Drama"].append("Comedy")

    print("After adding Comedy:", bfs(graph, start_node))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: Missing start node returns an empty list safely.
    print("Missing node:", bfs(graph, "Sports"))

    # Edge case 2: A graph with one node returns only that node.
    single_node_graph = {
        "Documentary": []
    }

    print("Single node graph:", bfs(single_node_graph, "Documentary"))


if __name__ == "__main__":
    main()