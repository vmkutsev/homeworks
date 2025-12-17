import pytest

def analyze_dag(graph):
    # делаем раскраску (люблю светофоры)
    GREEN, ORANGE, RED = 0, 1, 2

    color = {v: GREEN for v in graph}
    parent = {}
    topo = []
    cycle = []

    def dfs(v):
        nonlocal cycle
        color[v] = ORANGE

        for u in graph[v]:
            if color[u] == GREEN:
                parent[u] = v
                if dfs(u):
                    return True
            elif color[u] == ORANGE:
                cur = v
                cycle.append(u)
                while cur != u:
                    cycle.append(cur)
                    cur = parent[cur]
                cycle.append(u)
                cycle.reverse()
                return True

        color[v] = RED
        topo.append(v)
        return False

    for v in graph:
        if color[v] == GREEN:
            parent[v] = None
            if dfs(v):
                return 'yes cycle :)', cycle

    topo.reverse()
    return 'no cycle :(', topo

def test_empty():
    graph = {}
    kind, result = analyze_dag(graph)
    assert kind == 'no cycle :('
    assert result == []

def test_lonely():
    graph = {1: []}
    kind, result = analyze_dag(graph)
    assert kind == 'no cycle :('
    assert result == [1]

def test_selfish():
    graph = {1: [1]}
    kind, cycle = analyze_dag(graph)
    assert kind == 'yes cycle :)'
    assert cycle == [1, 1]

def test_horovod():
    graph = {
        1: [2],
        2: [3],
        3: [1]
    }
    kind, cycle = analyze_dag(graph)
    assert kind == 'yes cycle :)'
    assert cycle[0] == cycle[-1]

def test_casual():
    graph = {
        1: [2, 3],
        2: [4],
        3: [4],
        4: []
    }
    kind, result = analyze_dag(graph)
    assert kind == 'no cycle :('
    assert result == [1, 3, 2, 4]
