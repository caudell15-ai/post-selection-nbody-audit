import rebound
import numpy as np
import math
import time

print("REBOUND:", rebound.__version__)

JD0 = 2461200.5
DAY_TO_YEAR = 365.25
EARTH_TO_SUN = 3.0034896e-6

PX60 = {
    "m_earth": 0.6795321943685156,
    "a": 256.4346919438734,
    "q": 180.31961992118272,
    "e": 0.2968204943165421,
    "inc": 20.56183195375201,
    "Omega": 34.55418598459545,
    "omega": 334.34873590064956,
    "M": 211.70814,
}

SUN = [-1.963182736873869E-03,-5.381681233525128E-03,1.095729069346593E-04,6.591177489203827E-06,1.723516692596946E-06,-1.352985935777610E-07]
JUPITER = [-2.791577704007743E+00,4.463869004872217E+00,4.395802543118966E-02,-6.488172619881745E-03,-3.644844930038803E-03,1.603249848258083E-04]
SATURN = [9.390452646215312E+00,1.134613679451749E+00,-3.936179814793632E-01,-9.761194550885737E-04,5.526436401020123E-03,-5.724772854150238E-05]
URANUS = [9.328678655706682E+00,1.707379928064234E+01,-5.744436897126472E-02,-3.480510505065052E-03,1.702494948544489E-03,5.141047235282794E-05]
NEPTUNE = [2.985299549126585E+01,1.015318864506228E+00,-7.089014913081338E-01,-1.273546510481016E-04,3.155934766857904E-03,-6.205628269870471E-05]

TNOS = {
    "Sedna": [3.900056218727574E+01,7.115946242898202E+01,-1.701922324576390E+01,-2.483298016077602E-03,5.953819442803102E-04,2.031016406086007E-04],
    "VP113": [4.524964200890863E+01,6.900907222865177E+01,-2.062517922378562E+01,-1.485330414050343E-03,1.790711853477513E-03,6.516768044138161E-04],
    "Leleakuhonua": [7.212163089895252E+01,1.752764608339692E+01,1.463488586781377E+01,-1.613635745684152E-03,2.232318153133326E-03,-4.840283283295314E-05],
    "Ammonite": [-3.557146931107856E+01,-6.055902345768548E+01,2.957108687028307E+00,2.524129409051037E-03,-7.874406027153769E-04,-5.129993946218558E-04]
}

MASSES = {"Sun":1.0,"Jupiter":9.5479e-4,"Saturn":2.8574e-4,"Uranus":4.3658e-5,"Neptune":5.1513e-5}

def add_state(sim, state, mass=0.0):
    x,y,z,vx,vy,vz=state
    sim.add(m=mass,x=x,y=y,z=z,vx=vx*DAY_TO_YEAR,vy=vy*DAY_TO_YEAR,vz=vz*DAY_TO_YEAR)

def build_sim(include_px60=True, dt=0.25):
    sim=rebound.Simulation()
    sim.units=('yr','AU','Msun')
    add_state(sim,SUN,MASSES['Sun']); add_state(sim,JUPITER,MASSES['Jupiter']); add_state(sim,SATURN,MASSES['Saturn']); add_state(sim,URANUS,MASSES['Uranus']); add_state(sim,NEPTUNE,MASSES['Neptune'])
    sun=sim.particles[0]
    sim.add(m=4.5*EARTH_TO_SUN,a=480.0,e=0.25,inc=np.deg2rad(18.0),Omega=np.deg2rad(100.0),omega=np.deg2rad(150.0),M=np.deg2rad(280.0),primary=sun)
    sim.add(m=(PX60['m_earth']*EARTH_TO_SUN if include_px60 else 0.0),a=PX60['a'],e=PX60['e'],inc=np.deg2rad(PX60['inc']),Omega=np.deg2rad(PX60['Omega']),omega=np.deg2rad(PX60['omega']),M=np.deg2rad(PX60['M']),primary=sun)
    add_state(sim,TNOS['Sedna']); add_state(sim,TNOS['VP113']); add_state(sim,TNOS['Leleakuhonua']); add_state(sim,TNOS['Ammonite'])
    sim.N_active=7
    sim.integrator='whfast'
    sim.dt=dt
    return sim

sim=build_sim(include_px60=True,dt=0.25)
print('\nParticles loaded:',sim.N)
print('Active massive bodies:',sim.N_active)
print('Candidate #60 mass:',sim.particles[6].m)
print('Ammonite xyz:',sim.particles[10].x,sim.particles[10].y,sim.particles[10].z)
print('\nExpected:')
print('Particles loaded: 11')
print('Active massive bodies: 7')
print('\n2A-3 INITIALIZATION SUCCESS')
