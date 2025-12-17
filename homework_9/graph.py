import pytest
# изначально показалось, что речь об ориентированном графе,
# поэтому для верных условий код чучут избыточный
def roll_call(graph):
    gang = set(graph.keys())
    for neighbors in graph.values():
        for v in neighbors:
            gang.add(v)
    return gang

def dfs(start, graph, visited):
    stack = [start]
    component = []

    while stack:
        snitch = stack.pop()
        if snitch in visited:
            continue

        visited.add(snitch)
        component.append(snitch)

        for neighbor in graph.get(snitch, []):
            if neighbor not in visited:
                stack.append(neighbor)

    return component

def connected_components(graph):
    visited = set()
    components = []

    gang = roll_call(graph)
    for snitch in gang:
        if snitch not in visited:
            component = dfs(snitch, graph, visited)
            components.append(component)

    return components

def test_empty():
    graph = {}
    assert connected_components(graph) == []
def test_lonely():
    graph = {}
    assert connected_components(graph) == []
def test_isolated():
    graph = {
        1: [],
        2: [],
        3: []
    }
    assert connected_components(graph) == [[1], [2], [3]]
def test_repka():
    graph = {
        1: [2],
        2: [1, 3],
        3: [2]
    }
    assert connected_components(graph) == [[1, 2, 3]]
def test_selfish():
    graph = {
        1: [1]
    }
    assert connected_components(graph) == [[1]]
def test_casual():
    graph = {
        1: [2],
        2: [1],
        3: [],
        4: [5],
        5: [4]
    }
    assert connected_components(graph) == [[1, 2], [3], [4, 5]]
def test_casual2():
    graph = {
        1: [2],
        2: [1, 3],
        3: [2],
        4: [5],
        5: [4]
    }
    assert connected_components(graph) == [[1, 2, 3], [4, 5]]