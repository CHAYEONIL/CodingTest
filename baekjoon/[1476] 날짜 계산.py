E, S, M = 1, 1, 1
count = 1

inputE, inputS, inputM = map(int, input().split())

while True:
    if inputE == E and inputS == S and inputM == M :
        break;
    E += 1
    S += 1
    M += 1
    count += 1

    if E >= 16:
        E -= 15
    if S >= 29:
        S -= 28
    if M >= 20:
        M -= 19

print(count)