def empty(A):
    from collections import deque, defaultdict

    adj = defaultdict(list)
    for src, dest, _ in A.transitions:
        adj[src].append(dest)

    reachable = set()
    q = deque(A.initial_states)
    while q:
        s = q.popleft()
        if s not in reachable:
            reachable.add(s)
            q.extend(adj[s])
    
    reachable_finals = [f for f in A.final_states if f in reachable]
    if not reachable_finals:
        print("Language is empty: No reachable final state.")
        return True
    
    def dfs(s, visited, stack):
        visited.add(s)
        stack.add(s)
        for nxt in adj[s]:
            if nxt not in reachable:
                continue
            if nxt not in visited and dfs(nxt, visited, stack):
                return True
            if nxt in stack:
                return True
        stack.remove(s)
        return False

    for f in A.final_states:
        if f in reachable and dfs(f, set(), set()):
            return "Language Not Empty"
    print("Language is empty: Final states do not lie on any reachable cycle.")    
    return "Empty Language Detected"
