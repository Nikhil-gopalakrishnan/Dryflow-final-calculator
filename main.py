from formu_17_coeff import peakwidth2drynessNL
from formu_33_coeff import measured2x
from formu_53_coeff import measured2x2
from calc_theor_dryness import get_x_theor
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
# ['time (hr)', 'T','P','v','a0','a1','a2','lph']
# 1.598987 151.140353 4.005765 49.940852 595620982.601204 1169.890614 80.335131 96.186082

# constants
font_small = ("Ariel", 13)
font_large = ("Ariel", 20, "bold")

screen = Tk()
screen.title("FM calculator")
screen.minsize(1800, 1000)
screen.config(padx=20, pady=20)

# PART A

title_part_A = Label(text="Calculating dryness from coefficients", font=font_large)
title_part_A.grid(row=0, column=0, pady=20, columnspan=2)
pressure_part_A = Label(text="Pressure(bar g):", font=font_small)
pressure_part_A.grid(row=1, column=0, pady=10)
pipe_size_part_A = Label(text="Pipe Size(NB):", font=font_small)
pipe_size_part_A.grid(row=2, column=0, pady=10)
velocity_part_A = Label(text="Velocity(m/s):", font=font_small)
velocity_part_A.grid(row=3, column=0, pady=10)
peak_freq_part_A = Label(text="Peak frequency(Hz):", font=font_small)
peak_freq_part_A.grid(row=4, column=0, pady=10)
peak_width_part_A = Label(text="Peak width(Hz):", font=font_small)
peak_width_part_A.grid(row=5, column=0, pady=10)
sigmaf_part_A = Label(text="Sigmaf(peak width/peak freq):", font=font_small)
sigmaf_part_A.grid(row=6, column=0, pady=10)
sigmaf_val_part_A = Label(text="NA", font=font_small)
sigmaf_val_part_A.grid(row=6, column=1)
dryness17_part_A = Label(text="Dryness17:", font=font_small)
dryness17_part_A.grid(row=7, column=0, pady=10)
dryness17_val_part_A = Label(text="NA", font=font_small)
dryness17_val_part_A.grid(row=7, column=1)
dryness33_part_A = Label(text="Dryness33:", font=font_small)
dryness33_part_A.grid(row=8, column=0, pady=10)
dryness33_val_part_A = Label(text="NA", font=font_small)
dryness33_val_part_A.grid(row=8, column=1)
dryness53_part_A = Label(text="Dryness53:", font=font_small)
dryness53_part_A.grid(row=9, column=0, pady=10)
dryness53_val_part_A = Label(text="NA", font=font_small)
dryness53_val_part_A.grid(row=9, column=1)

# PART B

title_part_B = Label(text="Theoretical calculated values", font=font_large)
title_part_B.grid(row=0, column=2, columnspan=2, pady=20, padx=150)
superheated_t2bar = Label(text="Superheated temp at 2 bar(deg C):", font=font_small)
superheated_t2bar.grid(row=1, column=2, pady=10)
superheated_t3bar = Label(text="Superheated temp at 3 bar(deg C):", font=font_small)
superheated_t3bar.grid(row=2, column=2, pady=10)
pipe_size_part_B = Label(text="Pipe size(NB):", font=font_small)
pipe_size_part_B.grid(row=3, column=2, pady=10)
temperature_part_B = Label(text="Temperature(deg C):", font=font_small)
temperature_part_B.grid(row=6, column=2, pady=10)
pressure_part_B = Label(text="Pressure(bar g):", font=font_small)
pressure_part_B.grid(row=5, column=2, pady=10)
pressure_val_part_B = Label(text="NA", font=font_small)
pressure_val_part_B.grid(row=5, column=3)
meter_constant_part_B = Label(text="Meter constant:", font=font_small)
meter_constant_part_B.grid(row=4, column=2, pady=10)
peak_freq_part_B = Label(text="Peak frequency(Hz):", font=font_small)
peak_freq_part_B.grid(row=7, column=2, pady=10)
water_inj_rate = Label(text="Water injection rate(lph):", font=font_small)
water_inj_rate.grid(row=8, column=2, pady=10)
current_part_B = Label(text="Current(mA):", font=font_small)
current_part_B.grid(row=9, column=2, pady=10)

# PART C
title_part_C = Label(text="Computed values of steam properties", font=font_large)
title_part_C.grid(row=0, column=4, columnspan=2, pady=20, padx=50)
pipe_area_part_C = Label(text="Pipe area(m2):", font=font_small)
pipe_area_part_C.grid(row=1, column=4, pady=10)
pipe_area_val_part_C = Label(text="NA", font=font_small)
pipe_area_val_part_C.grid(row=1, column=5)
superheated_enthalpy_2bar = Label(text="Superheated enthalpy at 2 bar(kJ/kg):", font=font_small)
superheated_enthalpy_2bar.grid(row=2, column=4, pady=10)
superheated_enthalpy_2bar_val = Label(text="NA", font=font_small)
superheated_enthalpy_2bar_val.grid(row=2, column=5)
superheated_enthalpy_3bar = Label(text="Superheated enthalpy at 3 bar(kJ/kg):", font=font_small)
superheated_enthalpy_3bar.grid(row=3, column=4, pady=10)
superheated_enthalpy_3bar_val = Label(text="NA", font=font_small)
superheated_enthalpy_3bar_val.grid(row=3, column=5)
superheated_enthalpy_avg = Label(text="Average enthalpy of superheating(kJ/kg):", font=font_small)
superheated_enthalpy_avg.grid(row=4, column=4, pady=10)
superheated_enthalpy_avg_val = Label(text="NA", font=font_small)
superheated_enthalpy_avg_val.grid(row=4, column=5)
hf_part_C = Label(text="hf(kJ/kg) :", font=font_small)
hf_part_C.grid(row=5, column=4, pady=10)
hf_val_part_C = Label(text="NA", font=font_small)
hf_val_part_C.grid(row=5, column=5)
hfg_part_C = Label(text="hfg(kJ/kg) :", font=font_small)
hfg_part_C.grid(row=6, column=4, pady=10)
hfg_val_part_C = Label(text="NA", font=font_small)
hfg_val_part_C.grid(row=6, column=5)
velocity_part_C = Label(text="Velocity(m/s)[flowrate/area]:", font=font_small)
velocity_part_C.grid(row=7, column=4, pady=10)
velocity_val_part_C = Label(text="NA", font=font_small)
velocity_val_part_C.grid(row=7, column=5)
density_part_C = Label(text="Density of saturated steam(kg/m3):", font=font_small)
density_part_C.grid(row=8, column=4, pady=10)
density_val_part_C = Label(text="NA", font=font_small)
density_val_part_C.grid(row=8, column=5)
vol_flow_rate_part_C = Label(text="Volume flow rate(m3/hr):", font=font_small)
vol_flow_rate_part_C.grid(row=9, column=4, pady=10)
vol_flow_val_rate_part_C = Label(text="NA", font=font_small)
vol_flow_val_rate_part_C.grid(row=9, column=5)

# PART 4
pre_water_inj = Label(text="Properties before water injection", font=font_large)
pre_water_inj.grid(row=12, column=2, columnspan=2, pady=10)
post_water_inj = Label(text="Properties after water injection", font=font_large)
post_water_inj.grid(row=12, column=4, columnspan=2, pady=10)

dryness_pre = Label(text="Dryness(from enthalpy):", font=font_small)
dryness_pre.grid(row=13, column=2, pady=10)
dryness_pre_val = Label(text="NA", font=font_small)
dryness_pre_val.grid(row=13, column=3)
dryness_post = Label(text="Dryness(from enthalpy):", font=font_small)
dryness_post.grid(row=13, column=4, pady=10)
dryness_post_val = Label(text="NA", font=font_small)
dryness_post_val.grid(row=13, column=5)

mass_flow_rate_drysteam_pre = Label(text="mass flow rate of drysteam(mdot_i*dryness)(kg/hr):", font=font_small)
mass_flow_rate_drysteam_pre.grid(row=14, column=2, pady=10)
mass_flow_rate_drysteam_pre_val = Label(text="NA", font=font_small)
mass_flow_rate_drysteam_pre_val.grid(row=14, column=3)
mass_flow_rate_drysteam_post = Label(text="mass flow rate of drysteam(Dryflow)(kg/hr):", font=font_small)
mass_flow_rate_drysteam_post.grid(row=14, column=4, pady=10)
mass_flow_rate_drysteam_post_val = Label(text="NA", font=font_small)
mass_flow_rate_drysteam_post_val.grid(row=14, column=5)

total_mass_flow_rate_pre = Label(text="Total mass flow rate of wet steam(mdot_i)(kg/hr):", font=font_small)
total_mass_flow_rate_pre.grid(row=15, column=2, pady=10)
total_mass_flow_rate_pre_val = Label(text="NA", font=font_small)
total_mass_flow_rate_pre_val.grid(row=15, column=3)
total_mass_flow_rate_post = Label(text="Total mass flow rate of wet steam(including water)(kg/hr):", font=font_small)
total_mass_flow_rate_post.grid(row=15, column=4, pady=10)
total_mass_flow_rate_post_val = Label(text="NA", font=font_small)
total_mass_flow_rate_post_val.grid(row=15, column=5)

opening_no_part_D = Label(text="Valve Opening (NO) (percent):", font=font_small)
opening_no_part_D.grid(row=16, column=2, pady=10)
opening_no_part_D_val = Label(text="NA", font=font_small)
opening_no_part_D_val.grid(row=16, column=3)

steam_flow_no = Label(text="mass flow rate from e-valve (NO) (kg/hr):", font=font_small)
steam_flow_no.grid(row=16, column=4, pady=10)
steam_flow_no_val = Label(text="NA", font=font_small)
steam_flow_no_val.grid(row=16, column=5)


def button_1_clicked():
    if (input_1.get() == "") or (input_2.get() == "") or (input_3.get() == "") or (input_4.get() == ""):
        messagebox.showerror(title="Error", message="Enter all required values")
        input_1.delete(0, END)
        return

    user_input_pressure = float(input_1.get())
    user_input_pipesize = float(input_2.get())
    user_input_velocity = float(input_3.get())
    user_input_peakfreq = float(input_4.get())
    user_input_peakwidth = float(input_5.get())
    user_input_sigmaf = round((user_input_peakwidth / user_input_peakfreq), 4)

    dryness17 = round((peakwidth2drynessNL(user_input_sigmaf, user_input_pipesize, user_input_pressure,
                                           user_input_velocity))*100, 2)
    dryness33 = round((measured2x(user_input_pressure, user_input_velocity, user_input_pipesize, user_input_sigmaf))
                      * 100, 1)
    dryness53 = round((measured2x2(user_input_pressure, user_input_velocity, user_input_pipesize, user_input_sigmaf))
                      * 100, 1)
    dryness17_val_part_A.config(text=dryness17)
    dryness33_val_part_A.config(text=dryness33)
    dryness53_val_part_A.config(text=dryness53)
    sigmaf_val_part_A.config(text=user_input_sigmaf)


def button_2_clicked():
    if (input_9.get() == "") or (input_11.get() == "") or (input_12.get() == "") or (input_13.get() == ""):
        messagebox.showerror(title="Error", message="Enter all required values")
        input_1.delete(0, END)
        return
    super_heated_2bar = float(input_6.get())
    super_heated_3bar = float(input_7.get())
    pipe_size = float(pipe_size_val.get())
    temperature = float(input_9.get())
    met_const = float(input_10.get())
    peak_freq = float(input_11.get())
    water_rate = float(input_12.get())
    current = float(input_13.get())
    dryness_input_pre, dryflow_input_pre, dryness_input_post, wetflow_input_post, wetflow_input_pre, pressure, \
        dryflow_input_post, pipe_area, velocity, density_input, vol_input_flowrate, enth_input_avg, enth_hf, enth_hfg,\
        super_enthalpy_input_2bar, super_enthalpy_input_3bar, opening_no_percent, opening_flowrate = \
        get_x_theor(super_heated_2bar,
                    super_heated_3bar,
                    pipe_size,
                    temperature,
                    peak_freq,
                    water_rate,
                    met_const,
                    current)
    pressure_val_part_B.config(text=pressure)
    dryness_pre_val.config(text=dryness_input_pre)
    dryness_post_val.config(text=dryness_input_post)
    mass_flow_rate_drysteam_pre_val.config(text=dryflow_input_pre)
    mass_flow_rate_drysteam_post_val.config(text=dryflow_input_post)
    total_mass_flow_rate_pre_val.config(text=wetflow_input_pre)
    total_mass_flow_rate_post_val.config(text=wetflow_input_post)
    pipe_area_val_part_C.config(text=pipe_area)
    velocity_val_part_C.config(text=velocity)
    density_val_part_C.config(text=density_input)
    vol_flow_val_rate_part_C.config(text=vol_input_flowrate)
    superheated_enthalpy_avg_val.config(text=enth_input_avg)
    hf_val_part_C.config(text=enth_hf)
    hfg_val_part_C.config(text=enth_hfg)
    superheated_enthalpy_2bar_val.config(text=super_enthalpy_input_2bar)
    superheated_enthalpy_3bar_val.config(text=super_enthalpy_input_3bar)
    opening_no_part_D_val.config(text=opening_no_percent)
    steam_flow_no_val.config(text=opening_flowrate)
    input_1.delete(0, "end")
    input_1.insert(-1, pressure)
    input_3.delete(0, "end")
    input_3.insert(-1, velocity)
    input_4.delete(0, "end")
    input_4.insert(-1, peak_freq)
    input_5.delete(0, "end")


def button_clear_part_a_clicked():
    input_1.delete(0, "end")
    input_2.delete(0, "end")
    input_2.current(1)
    input_3.delete(0, "end")
    input_4.delete(0, "end")
    input_5.delete(0, "end")


def button_clear_part_c_clicked():
    input_6.delete(0, "end")
    input_6.insert(-1, 135)
    input_7.delete(0, "end")
    input_7.insert(-1, 145)
    input_9.delete(0, "end")
    input_10.delete(0, "end")
    input_10.insert(-1, 20547)
    input_11.delete(0, "end")
    input_12.delete(0, "end")
    input_13.delete(0, "end")
    pipe_size_val.delete(0)
    pipe_size_val.current(1)
    pipe_area_val_part_C.config(text="NA")
    pressure_val_part_B.config(text="NA")
    superheated_enthalpy_2bar_val.config(text="NA")
    superheated_enthalpy_3bar_val.config(text="NA")
    superheated_enthalpy_avg_val.config(text="NA")
    hf_val_part_C.config(text="NA")
    hfg_val_part_C.config(text="NA")
    velocity_val_part_C.config(text="NA")
    density_val_part_C.config(text="NA")
    vol_flow_val_rate_part_C.config(text="NA")
    dryness_pre_val.config(text="NA")
    dryness_post_val.config(text="NA")
    mass_flow_rate_drysteam_pre_val.config(text="NA")
    mass_flow_rate_drysteam_post_val.config(text="NA")
    total_mass_flow_rate_pre_val.config(text="NA")
    total_mass_flow_rate_post_val.config(text="NA")
    opening_no_part_D_val.config(text="NA")
    steam_flow_no_val.config(text="NA")


button = Button(text="Calculate", command=button_1_clicked, font=font_large)
button.grid(row=10, column=0, columnspan=2, pady=10)

clear_button = Button(text="Clear", command=button_clear_part_a_clicked, font=font_large)
clear_button.grid(row=11, column=0, columnspan=2)

button = Button(text="Calculate", command=button_2_clicked, font=font_large)
button.grid(row=10, column=3, pady=10)

clear_button = Button(text="Clear", command=button_clear_part_c_clicked, font=font_large)
clear_button.grid(row=11, column=3, pady=10)

input_1 = Entry(width=10, font=font_small)
input_1.grid(row=1, column=1)

n = StringVar()
input_2 = ttk.Combobox(screen, width=8, textvariable=n, font=font_small)
input_2['values'] = ("25", "40", "50", "80", "100")
input_2.grid(column=1, row=2)

input_3 = Entry(width=10, font=font_small)
input_3.grid(row=3, column=1)

input_4 = Entry(width=10, font=font_small)
input_4.grid(row=4, column=1)

input_5 = Entry(width=10, font=font_small)
input_5.grid(row=5, column=1)

input_6 = Entry(width=10, font=font_small)
input_6.insert(-1, 135)
input_6.grid(row=1, column=3)

input_7 = Entry(width=10, font=font_small)
input_7.insert(-1, 145)
input_7.grid(row=2, column=3)

pipe_size_val = ttk.Combobox(screen, width=8, textvariable=n, font=font_small)
pipe_size_val['values'] = ("25", "40", "50", "80", "100")
pipe_size_val.grid(column=3, row=3)
pipe_size_val.current(1)

s = StringVar()
input_10 = ttk.Combobox(screen, width=8, textvariable=s, font=font_small)
# {25:81782.4, 40:20547, 50:9098.12, 80:2807.67, 100:1228.4}
input_10["values"] = ("81782.4", "20547", "9098.12", "2807.67", "1228.4")
input_10.grid(row=4, column=3)
input_10.current(1)

input_9 = Entry(width=10, font=font_small)
input_9.grid(row=6, column=3)

input_11 = Entry(width=10, font=font_small)
input_11.grid(row=7, column=3)

input_12 = Entry(width=10, font=font_small)
input_12.grid(row=8, column=3)

input_13 = Entry(width=10, font=font_small)
input_13.grid(row=9, column=3)

screen.mainloop()
