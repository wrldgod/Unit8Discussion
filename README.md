# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare BFS and DFS conceptually and describe real-world applications and use cases.

## Implementation Summary

I created a graph using a Python dictionary as an adjacency list. The nodes represented streaming content categories, and the edges represented relationships between similar categories.

I implemented Breadth-First Search using a deque as a queue and a set to track visited nodes. The queue allowed the graph to be visited level by level, while the visited set prevented nodes from being processed more than once.

I also added a new Comedy node and connected it to Drama to demonstrate how the traversal changed. I tested two edge cases: a missing starting node and a graph containing only one node.

## Reflection

While completing this assignment, I learned how graphs can be represented using adjacency lists and how Breadth-First Search can move through connected nodes level by level. I also learned how a queue controls the traversal order and how a visited set prevents the same node from being processed repeatedly.

The part I had to think about the most was making sure nodes were not revisited, especially because several nodes in the graph had connections back to earlier nodes. Using a set for visited nodes made the traversal easier to manage and prevented an endless loop.

BFS and DFS both traverse graphs, but they explore them differently. BFS checks nearby nodes first, while DFS follows one path as far as possible before returning. BFS would be useful for finding nearby connections, such as recommendations based on closely related content or finding the shortest route in an unweighted graph. DFS could be better for exploring deeper relationships, such as following a chain of related genres or searching through a game map.