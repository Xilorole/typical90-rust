N,K = list(map(int,input().split()))
S = [ord(s)-ord("a") for s in input().rstrip()]

# ある文字が次にどの位置に出現するかの配列を計算
C = [[-1 for i in range(26)] for j in range(N+1)]
for i,s in enumerate(S):
    C[i][s] = i

for j in range(N-2,-1,-1):
    for i in range(26):
        if C[j][i] == -1 and C[j+1][i] != -1:
            C[j][i] = C[j+1][i]

# 貪欲法でa-zの文字を採用していいかを確認する
out = ""
pos = 0
for k in range(K):
    for a in range(26):
        nextPos = C[pos][a]
        if nextPos == -1:
          continue

        # 残りの文字をそのまま採用してK文字を構成できるかどうか
        if len(out) + (N-nextPos) >=K:
            pos = nextPos + 1
            out += chr(a + ord("a"))
            break
print(out)