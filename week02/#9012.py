for _ in range(int(input())):
    stk = []
    is_vps = True
    for char in input():
        if char == "(":
            stk.append(char)
        else:   # )
            if stk: # 스택이 비어있지 않으면
                stk.pop()
            else:   # 스택이 비어있으면
                is_vps = False
                break

    if stk: # 마지막으로 스택이 비어있는지 검사
        is_vps = False

    print("YES" if is_vps else "NO")
