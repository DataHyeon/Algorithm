def solution(tickets):
    answer = []
    ticket_dict = {}
    
    tickets.sort(reverse=True)
    
    for to_, from_ in tickets:
        if to_ not in ticket_dict:
            ticket_dict[to_] = []
        ticket_dict[to_].append(from_)
    
    route, stack = [], ["ICN"]
    
    while stack:
        current = stack[-1]
        
        if current in ticket_dict and ticket_dict[current]:
            a = ticket_dict[current].pop()
            stack.append(a)
        else:
            b = stack.pop()
            route.append(b)

    return route[::-1]