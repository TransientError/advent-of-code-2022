from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import re


data = Path("input.txt").read_text()
names_to_node = {}


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


max_pressure = 0


@lru_cache(maxsize=None)
def search(minutes: int, opened: tuple[str], node: str) -> int:
    if minutes == 0:
        return 0

    max_possible = 0
    if node not in opened and (flow_rate := names_to_node[node].flow_rate) > 0:
        max_possible = max(
            (flow_rate * (minutes - 1))
            + search(
                minutes - 1,
                (*opened, node),
                node,
            ),
            max_possible,
        )

    for edge in names_to_node[node].edges:
        max_possible = max(search(minutes - 1, opened, edge), max_possible)

    return max_possible


result = search(30, (), "AA")
print(result)
