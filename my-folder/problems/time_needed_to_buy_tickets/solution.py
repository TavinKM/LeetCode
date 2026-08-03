class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        ans = 0
        while tickets:
            print("position " + str(k))
            tickets[0] -= 1
            ticket = tickets.pop(0)
            k -= 1
            if ticket == 0:
                if k == -1:
                    return ans + 1
            else:
                tickets.append(ticket)
            if k == -1:
                k = len(tickets) - 1
            ans += 1
        return ans