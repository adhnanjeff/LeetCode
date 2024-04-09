#Problem 2073

def ticketTime(tickets, k):
    count = 0
    while tickets[k] != 0:
        for i in range(len(tickets)):
            if tickets[i] == 0:
                continue
            else:    
                tickets[i] -= 1
                count += 1
                if tickets[k] == 0:  # Check if tickets[k] becomes zero
                    return count
    return count 

tickets = [84, 49, 5, 24, 70, 77, 87, 8]
k = 3
ans = ticketTime(tickets, k)
print(ans)