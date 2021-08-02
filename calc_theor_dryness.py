import numpy as np
import math


def get_cs_area(pipe_size):
    schedule_40 = {25: (33.4, 3.38),  # (OD, wall_thickness), mm
                   40: (48.3, 3.68),
                   50: (60.3, 3.91),
                   80: (88.9, 5.49),
                   100: (114.3, 6.02)
                   }

    assert pipe_size in schedule_40.keys()
    inner_dia = schedule_40[pipe_size][0] - 2 * schedule_40[pipe_size][1]
    cs_area = np.pi * (inner_dia * 1.e-3) ** 2 * 0.25
    return cs_area


def tsuper2hg(t2, t3):
    def saturated_pressure(temp_inlet):
        sat_pres = math.exp((11.721 * temp_inlet - 1167.1229) / (temp_inlet + 228.74)) - 1.013
        return sat_pres

    def saturated_temperature(pres):
        if pres <= 130:
            f = 0
        elif pres <= 150:
            f = 1.4
        elif pres <= 190:
            f = 2.5
        else:
            f = 4.0
        sat_temp = (3892.7 / (9.48654 - math.log((pres + 1.013) / 10))) - 230.4724 - f
        return sat_temp

    def calc_init(temp_inlet, pres):
        if temp_inlet > saturated_temperature(pres):
            calc_temp = temp_inlet
        else:
            calc_temp = saturated_temperature(pres)

        red_pre = (pres + 1.013) / 220.64
        red_temp = (calc_temp + 273.5) / 647.097
        f1 = (0.4409392 / red_temp) - (1.386596 / red_temp ** 2) + (1.380501 / red_temp ** 3) - (0.7644377 / red_temp ** 4)
        f2 = (56.40548 / red_temp) - (297.0161 / red_temp ** 2) + (617.8258 / red_temp ** 3) - (634.747 / red_temp ** 4) + \
                 (322.8009 / red_temp ** 5) - (65.45004 / red_temp ** 6)
        f3 = (149.3651 / red_temp) - (895.0375 / red_temp ** 2) + (2123.035 / red_temp ** 3) - \
                 (2488.625 / red_temp ** 4) + (1439.213 / red_temp ** 5) - (327.7709 / red_temp ** 6)
        f4 = 151.1386 - (967.3387 / red_temp) + (2478.739 / red_temp ** 2) - (3178.106 / red_temp ** 3) + \
                 (2038.512 / red_temp ** 4) - (523.2041 / red_temp ** 5)

        z = 1 + (red_pre * f1) + (red_pre ** 2 * f2) + (red_pre ** 3 * f3) + (red_pre ** 4 * f4)

        density = round(73.874969 * red_pre / (red_temp * z), 2)

        f5 = 10258.8 - (20231.3 / red_temp) + (24702.8 / red_temp**2) - (16307.3 / red_temp**3) + (5579.31 / red_temp**4) - (777.285 / red_temp**5)
        f6 = (-355.878 / red_temp) + (817.288 / red_temp**2) - (845.841 / red_temp**3)
        f7 = 160.276 / red_temp**3
        f8 = (-95607.5 / red_temp) + (443740 / red_temp**2) - (767668 / red_temp**3) + (587261 / red_temp**4) - (167657 / red_temp**5)
        f9 = (22542.8/red_temp**2) - (84140.2/red_temp**3) + (104198/red_temp**4) - (42886.7/red_temp**5)

        specific_enthalpy = round(f5 + (red_pre * f6) - (red_pre**2 * f7) + (red_pre**3 * f8) + (red_pre**4 * f9), 2)

        return specific_enthalpy

    enthalpy1 = calc_init(t2, 2)
    enthalpy2 = calc_init(t3, 3)
    mean_enthalpy = ((enthalpy1+enthalpy2)/2) * 1000  # for Kilo joules to joules conversion
    return mean_enthalpy, enthalpy1, enthalpy2


def P2Tsat(P):
    tsat = 228.74 * (math.log(P) + 5.1054) / (11.721 - math.log(P))
    return tsat


def T2Psat(T):
    sat_pres = math.exp((11.721 * T - 1167.1229) / (T + 228.74)) - 1.013
    return sat_pres


def steam_property(prpty, P=None, T=None):
    # P is absolute pressure, T is Celsius temperature
    assert not ((P is None and T is None) or (P is not None and T is not None))
    if T is not None and P is None:
        psat = T2Psat(T)
        P = psat
    elif T is None and P is not None:
        tsat = P2Tsat(P)
        T = tsat

    ent_satsteam = round(1000 * (2501.689845 + (1.806916015 * T) + (5.087717 * 10 ** -4 * T ** 2) - (1.1221 * 10 ** -5 * T ** 3)), 2)
    ent_satwater = round(1000 * (-0.033635409 + (4.207557011 * T) - (6.200339 * 10 ** -4 * T ** 2) + (4.459374 * 10 ** -6 * T ** 3)), 2)
    ent_hfg = ent_satsteam - ent_satwater
    dens_satsteam = round(1 / ((T + 273) / ((P * 1.0198) + 1.033) * 0.00471 - 9281752.756 / (T + 273) ** 3.3333 - 19000 * 100 ** 14 * ((P * 1.0198) + 1.033) ** 2 / (T + 273) ** 14), 2)
    dens_satwater = round(1000 * (1 - (T + 288.9414) / (508929.2 * (T + 68.12963)) * (T - 3.9863) ** 2), 2)
    prop_list = [P, T, ent_satwater, ent_satsteam, dens_satsteam, ent_hfg]
    prop_short_names = ('P', 'T', 'hf', 'hg', 'rho', 'hfg')
    prop_index = prop_short_names.index(prpty)
    return prop_list[prop_index]  # output units P bar (a) T is degC enthalpies is J/kg and density in kg/m3


def water_enthalpy(T):  # T in degrees C
    return 4.184e3 * T  # enthalpy in J/kg


def dryness_calc(Pres, m, T=None, x=None, h=None, H=None):
    P = Pres # bar a
    m = m # any unit
    assert m > 0. and P > 0.
    assert len(list(filter(lambda u:u is not None,(T,x,h,H)))) == 1
    Tsat = P2Tsat(Pres)
    if T is not None:
        assert T < Tsat
        h = water_enthalpy(T)
        H = h * m
    elif x is not None:
        assert 0 <= x <= 1
        T = Tsat
        h = steam_property('hf', T=T) + x * steam_property('hfg', T=T)
        H = h * m
    else:
        if h is not None:
            h = h
            H = h*m
        else:
            H = H
            h = H/m
    hf, hfg, hg = steam_property('hf', P=P), steam_property('hfg', P=P), steam_property('hg', P=P)
    assert h < hg
    if h > hf: # steam is saturated
        x = (h - hf)/hfg
        T = Tsat
    else: # liquid water
        T = h / 4.184e3
    return h


def get_x_theor(T2bar, T3bar, pipe_size, temp, freq, lph, meter_constant, current):
    pres = T2Psat(temp)
    opening_no = 100 - ((current-4)*100/16)
    factor_no = (opening_no/100 - 1)*1.60206
    kv = 36*(10**factor_no)
    steam_flow_no = 12*kv*(pres+1)
    area = get_cs_area(pipe_size)
    h_incoming, superenthalp_2, superenthalp_3 = tsuper2hg(T2bar, T3bar)
    hf = steam_property('hf', T=temp)
    hfg = steam_property('hfg', T=temp)
    s = dryness_calc(pres+1., 1., T=27.)
    hw = s  # specific enthalpy of injected water
    x_incoming = (h_incoming-hf)/hfg
    Ks = meter_constant
    flowrate = freq/Ks
    velocity = flowrate/area
    dens_satsteam = steam_property('rho', T=temp)
    mdot_dry = dens_satsteam * flowrate
    mdot_incoming = (lph/3600.*(hf-hw) + mdot_dry*hfg)/(x_incoming*hfg)
    m_total = (mdot_incoming + lph/3600.)
    x = mdot_dry / m_total
    return round(x_incoming*100, 1), round(mdot_incoming*3600*x_incoming, 1), round(x*100, 1), round(m_total*3600, 1), \
           round(mdot_incoming*3600, 1), round(pres, 1), round(mdot_dry*3600, 1), round(area, 5), round(velocity, 2), \
           round(dens_satsteam, 2), round(3600*flowrate, 2), int(h_incoming/1000), int(hf/1000), int(hfg/1000), \
           int(superenthalp_2), int(superenthalp_3), round(opening_no, 1), round(steam_flow_no, 1)

