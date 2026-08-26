GM_JPL = {
    "Sun":     132712440041.93938,
    "Jupiter": 126712764.100000,
    "Saturn":   37940584.841800,
    "Uranus":    5794556.400000,
    "Neptune":   6836527.100580,
}

MASSES_JPL = {
    "Sun": 1.0,
    "Jupiter": GM_JPL["Jupiter"] / GM_JPL["Sun"],
    "Saturn":  GM_JPL["Saturn"]  / GM_JPL["Sun"],
    "Uranus":  GM_JPL["Uranus"]  / GM_JPL["Sun"],
    "Neptune": GM_JPL["Neptune"] / GM_JPL["Sun"],
}

print(MASSES_JPL)
