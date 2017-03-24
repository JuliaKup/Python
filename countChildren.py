import json

"""input format: [{"name": "A", "parents": []},
                  {"name": "B", "parents": ["A", "C"]},
                  {"name": "C", "parents": ["A"]}]"""

s = json.loads(input())

# {name: parents}
parents = {row['name']: row['parents'] for row in s}

# {name: number of children}
counts = {}

for key in parents:
    queue = [key]  # queue of parents to be cheered, one is a parent of oneself
    cheered = []  # cheered parents, immediate or distant
    while queue:
        if queue[0] not in counts:  # if you not in counts, you didn't have children before
            counts[queue[0]] = 0
        if queue[0] not in cheered:  # if you haven't been cheered, let us cheer you
            counts[queue[0]] += 1    # Congratulations! You have a child!
            cheered.append(queue[0])  # Let's note that we have already cheered you
            queue.extend(parents[queue[0]])  # Let's add to the queue your parents, they would want to be cheered too
        queue.pop(0)  # Bye!

for key in sorted(counts.keys()):
    print(key, ':', counts[key])