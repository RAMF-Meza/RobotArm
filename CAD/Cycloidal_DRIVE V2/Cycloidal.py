# ratio 19:1 with 5010/5015 GYEMS Servo
R = 25
E = 1
Rr = 2.5
N = 16

# Definitions
# R : Radius of the roller's PCD (Pitch Circle Diameter)
# E : Eccentricity (or offset) from input shaft to cycloid disc
# Rr : Radius of the roller
# Ratio is N - 1:1

# Precalculation
R_EN = R / (E*N)
NmE = N - E
_N = 1 - N

X = "({}*cos(t)) - ({}*cos(t+arctan(sin({}*t) / ({} - cos({} * t)) ))) - ({} * cos({} * t))".format(R, Rr, _N, R_EN, _N, E, N)
Y = "(-{}*sin(t)) + ({}*sin(t+arctan(sin({}*t) / ({} - cos({} * t)) ))) + ({} * sin({} * t))".format(R, Rr, _N, R_EN, _N, E, N)

print(X)
print(Y)