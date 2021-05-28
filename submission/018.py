T = int(input())
L, X, Y = list(map(int,input().split()))
Q = int(input())

from math import sin, cos, pi, atan2

for E in [int(input()) for _ in range(Q)]:
  E %= T
  y = - L / 2 * sin(2*pi*E/T)
  z = L / 2 * (1 - cos(2*pi*E/T))
  l = ((y-Y)**2 + X**2)**.5
  print(atan2(z,l)*180/pi)
