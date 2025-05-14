# Input result matrix
N, C = map(int, input().split())
results = []
for _ in range(N):
    results.append(list(map(int, input().split())))

# Tournament
this_round = []
for i in range(1, N + 1):
    this_round.append(i)

while(N > 0):
    next_round = []
    for i in range(len(this_round) // 2):
        # Find a winner
        teamA = this_round[2 * i]
        teamB = this_round[(2 * i) + 1]
        winner = results[teamA - 1][teamB - 1]
        
        # Team has the special card
        if(teamA == C and teamA != winner):
            winner = teamA
            C = 0
        if(teamB == C and teamB != winner):
            winner = teamB
            C = 0
        next_round.append(winner)
    
    # Output
    if(len(next_round) == 1):
        print(winner)
        break
    this_round = next_round
    N //= 2