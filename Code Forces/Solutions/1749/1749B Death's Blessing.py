def death_blessing():
    t = int(input())
    for i in range(t):
        n = int(input())
        health = list(map(int, input().split()))
        spell = list(map(int, input().split()))
        if n == 1:
            print(sum(health))
        else:
            print(sum(health)+sum(spell)-max(spell))


death_blessing()
