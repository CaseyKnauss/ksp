import krpc, time, math
conn = krpc.connect(name='Launch Into Orbit')
conn = krpc.connect('127.0.0.1', name = 'Sub Orb  Flight', rpc_port=50000, stream_port=50001 )
vessel = conn.space_center.active_vessel

turn_altitude = 1000
target_altitude = 150000

#SETUP STREAMS
ut = conn.add_stream(getattr, conn.space_center, 'ut')
altitude = conn.add_stream(getattr, vessel.flight(), 'mean_altitude')
apoapsis = conn.add_stream(getattr, vessel.orbit, 'apoapsis_altitude')
periapsis = conn.add_stream(getattr, vessel.orbit, 'periapsis_altitude')
eccentricity = conn.add_stream(getattr, vessel.orbit, 'eccentricity')
stage_2_resources = vessel.resources_in_decouple_stage(stage = 2, cumulative = False)
launcher_fuel = conn.add_stream(stage_2_resources.amount, 'LiquidFuel')


#Pre-Launch Setup
vessel.control.sas = False
vessel.control.rcs = False
vessel.control.throttle = 1

# vessel = conn.add_stream()
vessel.auto_pilot.target_pitch_and_heading(90,80)
vessel.auto_pilot.engage()
vessel.control.activate_next_stage()
