import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    NUMS = [int(line.strip()) for line in f.readlines() if line.strip()]

ans = 0
for secret in NUMS:
    for _ in range(2000):
        secret = (secret<<6 ^ secret) % 16777216
        secret = (secret>>5 ^ secret) % 16777216
        secret = (secret<<11 ^ secret) % 16777216
    ans += secret
print(ans)
