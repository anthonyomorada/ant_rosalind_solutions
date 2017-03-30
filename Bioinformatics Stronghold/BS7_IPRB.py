k, m, n = map(float,open('rosalind_iprb.txt', 'r').read().strip().split())
p = [
    k * (k - 1),  # AA, AA pairs
    k * m,  # AA, Aa pairs
    k * n,  # AA, aa pairs
    m * k,  # Aa, AA pairs
    m * (m - 1) * 0.75, # Aa, Aa pairs
    m * n * 0.5, # Aa, aa pairs
    n * k,  # aa, AA pairs
    n * m * 0.5,  # aa, Aa pairs
    0,  # aa, aa pairs
]
t = k + m + n

print sum(p) / t / (t - 1)

