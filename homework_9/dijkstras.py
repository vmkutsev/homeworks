import heapq
import math
import pytest

def dijkstra(graph, start):

    dist = {v: math.inf for v in graph}
    dist[start] = 0

    heap = [(0, start)]

    while heap:
        cur_dist, v = heapq.heappop(heap)

        if cur_dist > dist[v]:
            continue

        for neighbor, weight in graph[v]:
            new_dist = cur_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return dist

def test_disconnected():
    graph = {
        1: [(2, 1)],
        2: [],
        3: []
    }
    dist = dijkstra(graph, 1)
    assert dist[3] == math.inf

def test_oneway():
    graph = {
        1: [(2, 5)],
        2: [(3, 3)],
        3: []
    }
    dist = dijkstra(graph, 1)
    assert dist == {
        1: 0,
        2: 5,
        3: 8
    }

def test_crossroads():
    graph = {
        1: [(2, 1), (3, 5)],
        2: [(3, 1)],
        3: []
    }
    dist = dijkstra(graph, 1)
    assert dist[3] == 2