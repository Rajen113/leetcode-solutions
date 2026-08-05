class Solution(object):
    def remainingMethods(self, n, k, invocations):
        graph = [[] for _ in range(n)]

        # Step 1: Build graph
        for a, b in invocations:
            graph[a].append(b)

        # Step 2: Find all suspicious methods
        suspicious = set()
        stack = [k]

        while stack:
            node = stack.pop()

            if node in suspicious:
                continue

            suspicious.add(node)

            for nei in graph[node]:
                if nei not in suspicious:
                    stack.append(nei)

        # Step 3: Check outside -> suspicious edge
        for a, b in invocations:
            if a not in suspicious and b in suspicious:
                return list(range(n))

        # Step 4: Return non-suspicious methods
        result = []

        for i in range(n):
            if i not in suspicious:
                result.append(i)

        return result