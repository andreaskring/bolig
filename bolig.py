# PRIS = 3000000
# R_REAL = 0.0202
# R_BIDRAG = 0.0074
# REAL_PROCENT = 0.80
# N_REAL = 121
# KURS = 98.98

PRIS = 3000000
R_REAL = -0.0013
R_BIDRAG = 0.0111
REAL_PROCENT = 0.80
N_REAL = 119
KURS = 102.88

G = PRIS*REAL_PROCENT/(KURS/100)


def rn(r, n):
    a = 1 + r
    return a**(1/n) - 1


def r4(r):
    return rn(r, 4)


def r12(r):
    return rn(r, 12)


def y(G, r, n):
    return G*r/(1 - (1 + r)**(-n))


y4_real = y(G, r4(R_REAL), N_REAL)
y_bidrag = G*R_BIDRAG
Y = 4*y4_real + y_bidrag


