from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path
import re
from typing import Deque, FrozenSet


data = Path("input.txt").read_text()
names_to_node: dict[str, "Node"] = {}


@dataclass
class Node:
    PARSER_RE = re.compile(
        r"Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? (.*)"
    )

    flow_rate: int
    edges: list[str]
    name: str

    @staticmethod
    def parse(line: str) -> "Node":
        m = Node.PARSER_RE.match(line)
        assert m is not None, f"line didn't parse {line}"
        return Node(int(m[2]), m[3].split(", "), m[1])


for line in data.splitlines():
    if line:
        node = Node.parse(line)
        names_to_node[node.name] = node

distances = defaultdict(lambda: {})

for origin in names_to_node.keys():
    for destination in names_to_node.keys():
        queue: Deque[tuple[str, int]] = deque([("AA", 0)])
        visited = {}
        while queue:
            cur, distance = queue.popleft()
            if cur == destination:
                distances[origin][destination] = distance
                break
            for edge in names_to_node[cur].edges:
                queue.append((edge, distance + 1))


memo = {}


def search(pos: str, opened: FrozenSet[str], mins: int, others: int) -> int:
    if mins <= 0:
        return 0 if others <= 0 else search("AA", opened, 26, others - 1)

    key = (pos, opened, mins, others)
    if key in memo:
        return memo[key]

    ans = 0

    if pos not in opened and (fr := names_to_node[pos].flow_rate) > 0:
        new_opened = set(opened)
        new_opened.add(pos)
        new_mins = mins - 1
        ans = max(
            ans, search(pos, frozenset(new_opened), new_mins, others) + (fr * new_mins)
        )

    for edge in names_to_node[pos].edges:
        ans = max(ans, search(edge, opened, mins - 1, others))

    memo[key] = ans

    return ans


print(search("AA", frozenset(), 26, 1))
