import numpy as np

p0 = -1.32e+05
p1 = 6.99e+04
p2 = -1.12e+05
p3 = 2.61e+04
p4 = 1.46e+03
p5 = -2.10e+02
p6 = -7.64e+05
p7 = -4.67e+05
p8 = 9.77e+04
p9 = 4.12e+05
p10 = 3.91e+05
p11 = -8.40e+04
p12 = 7.25e+03
p13 = 5.12e+03
p14 = -7.99e+02
p15 = -4.87e+03
p16 = -4.31e+03
p17 = 7.04e+02
p18 = -4.62e+04
p19 = 3.08e+04
p20 = -7.26e+03
p21 = 3.59e+06
p22 = -1.92e+06
p23 = 1.08e+03
p24 = -4.76e+05
p25 = 1.56e+05
p26 = -3.03e+04
p27 = -4.20e+02
p28 = -1.33e+02
p29 = 7.24e+03
p30 = 1.33e+02
p31 = 1.80e+01
p32 = 4.20e+00


def measured2x(P, v, d, sigmaf):
    s, r = sigmaf, np.sqrt(sigmaf)
    nr = p0 + p1 * P + p2 * v + p3 * P * v + p4 * P * d + p5 * P * v * d + p6 * P * s + p7 * v * s + p8 * P * v * s + p9 * P * r + p10 * v * r + p11 * P * v * r + p12 * P * d * s + p13 * v * d * s + p14 * P * v * d * s + p15 * P * d * r + p16 * v * d * r + p17 * P * v * d * r + p18 * d * s + p19 * d * r + p20 * d + p21 * s + p22 * r + p23 * v * d
    dr = p24 + p25 * P + p26 * v + p27 * P ** 2 + p28 * v ** 2 + p29 * P * v + p30 * P ** 2 * v + p31 * P * v ** 2 + p32 * P ** 2 * v ** 2
    return round(nr / dr, 2)



