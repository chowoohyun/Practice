T = int(input())

for tc in range(1, T+1):
    L, U, X = map(int, input().split())
    if X < L:
        print(f'#{tc} {L-X}')
    elif X > U:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} 0')

