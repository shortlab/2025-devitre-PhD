# mystyle.py
import matplotlib.pyplot as plt
import seaborn as sns

palette_energy = sns.color_palette("magma", n_colors=4) #CMRmap_r, magma
colors_energies = {
    '150': palette_energy[0], 
    '800': palette_energy[1], 
    '1200': palette_energy[2], 
    '2400': palette_energy[3]
}

palette_tapes = sns.color_palette("viridis", n_colors=7) #CMRmap_r, magma
colors_tapes = {
    'f20': palette_tapes[0],
    'f23': palette_tapes[1],
    'f29': palette_tapes[2],
    'f33': palette_tapes[3],
    'f34': palette_tapes[4],
    'f28': palette_tapes[5],
    'f37': palette_tapes[6]
}

def set_style():
    plt.rcParams.update({
        "figure.figsize": (9, 9),       # default figure size
        "axes.titlesize": 24,           # axis title font size
        "axes.labelsize": 24,           # x/y axis label font size
        "xtick.labelsize": 24,          # x tick label size
        "ytick.labelsize": 24,          # y tick label size
        "legend.fontsize": 16,          # legend font size
        "axes.spines.right": False,     # remove right spine
        "axes.spines.top": False,       # remove top spine
        "figure.labelsize": 20,         # fontsize for supxlabel/supylabel
        "font.family": "serif",         # use serif fonts
        "font.serif": ["CMU Serif"],       # specifically Computer Modern
        "mathtext.fontset": "cm",          # ensure math uses Computer Modern
        "lines.markersize": 10,            # default marker size
        "lines.solid_capstyle": "round",   # rounded end caps for lines
        "axes.unicode_minus": False,
        "xtick.major.size": 8,   # length of major x-axis ticks
        "ytick.major.size": 8,   # length of major y-axis ticks
        "xtick.major.width": 2,  # width of major x-axis ticks
        "ytick.major.width": 2,  # width of major y-axis ticks
    })

# Automatically apply when imported
set_style()