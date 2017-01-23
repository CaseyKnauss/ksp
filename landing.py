import krpc, time, math
sleep = time.sleep
# conn = krpc.connect(name='Launding')
conn = krpc.connect('127.0.0.1', name = 'Landing', rpc_port=50000, stream_port=50001 )
vessel = conn.space_center.active_vessel

turn_altitude = 1000
target_altitude = 150000
stages = 2

#SETUP STREAMS
ut = conn.add_stream(getattr, conn.space_center, 'ut')
refframe = vessel.orbit.body.reference_frame
position = conn.add_stream(vessel.position, refframe)
altitude = conn.add_stream(getattr, vessel.flight(), 'surface_altitude')
elevation = conn.add_stream(getattr, vessel.flight(), 'elevation')
# speed = conn.add_stream(getattr, vessel.flight(refframe).speed)
# speed = position
velocity = conn.add_stream(getattr, vessel.flight(), 'velocity')
apoapsis = conn.add_stream(getattr, vessel.orbit, 'apoapsis_altitude')
periapsis = conn.add_stream(getattr, vessel.orbit, 'periapsis_altitude')
eccentricity = conn.add_stream(getattr, vessel.orbit, 'eccentricity')

# while vessel.flight().mean_altitude > 4000:
#     print(vessel.flight().mean_altitude)
#     sleep(1)
# vessel.auto_pilot.target_pitch_and_heading(90, 90)

altitudes = { 3: {'speed':0,
                  'throttle':0,
                 },
              5: {'speed':-3,
                  'throttle':.25,
                  },
              10: {'speed':-6,
                  'throttle':.75,
                  },
              50: {'speed':-10,
                  'throttle':1,
                  },
              200: {'speed':-20,
                    'throttle':1,
                  },
              500: {'speed':-25,
                    'throttle': 1,
                  },
              1000: {'speed': -35,
                     'throttle': 1,
                  },
              2000: {'speed': -50,
                     'throttle': 1,
                  },
              5000: {'speed': -150,
                     'throttle': 1,
                  },
              10000: {'speed': -250,
                      'throttle': 1,
                  },
              15000: {'speed': -500,
                      'throttle': 1,
                  },
              30000:{'speed': -500,
                      'throttle': 1,
                  },
              70000: {'speed': -700,
                      'throttle': 1,
                      },
            }
while vessel.situation == 'VesselSituation.orbiting':
    print('In Orbit')


while 1:
    # vessel.auto_pilot.sas = True
    # vessel.auto_pilot.sas_mode.reference_frame = refframe
    # vessel.auto_pilot.sas_mode.retrograde
    # vessel.auto_pilot.sas_mode.reference_frame = True
    # vessel.auto_pilot.sas_mode.reference_frame
    # vessel.auto_pilot.sas_mode.reference_frame()
    # print(vessel.auto_pilot.sas_mode)
    # vessel.auto_pilot.engage()
    # print(vessel.flight(vessel.orbit.body.reference_frame).velocity[2])
    try:
        surf_el = altitude()
        # print(surf_el)
        x = (min(filter(lambda x: x > surf_el, altitudes)))
        velocity = (vessel.flight(vessel.orbit.body.reference_frame).velocity[2])
        # print(velocity)
        if surf_el < 100:
            if surf_el < 1:
                vessel.control.throttle = 0
    except:
        x = (max(altitudes))
        print(Exception)
    # print(x)
    # if vessel.flight(vessel.orbit.body.reference_frame).speed > altitudes[x]['speed']:
    if velocity < altitudes[x]['speed']:
        # print(vessel.situation)
        throttle = altitudes[x]['throttle']
        vessel.control.throttle = throttle
        # print("altitude: ", round(altitude()), " m")
        # print("velocity: ", velocity())
        # print("speed:    ", round(vessel.flight(vessel.orbit.body.reference_frame).speed), " m/s")
        # print("velocity:    ", (vessel.flight(vessel.orbit.body.reference_frame).velocity), " m/s")
        # sleep(1)
    else:
        vessel.control.throttle = 0
        # print(min(filter(lambda x: x < vessel.flight().mean_altitude, altitudes)))









































    # if vessel.flight(vessel.orbit.body.reference_frame).speed > 200
#
#
# while vessel.flight().mean_altitude > 17000:
#     if vessel.flight(vessel.orbit.body.reference_frame).speed > 600:
#         vessel.auto_pilot.target_pitch_and_heading(90, 90)
#         vessel.control.throttle = 1
#         print(altitude(), velocity())
#         print(round(vessel.flight(vessel.orbit.body.non_rotating_reference_frame).speed))
#     else:
#         vessel.control.throttle = 0
#
# while vessel.flight().mean_altitude > 10000:
#     if vessel.flight(vessel.orbit.body.reference_frame).speed > 250:
#         vessel.auto_pilot.target_pitch_and_heading(90, 90)
#         vessel.control.throttle = 1
#         print(altitude(), velocity())
#     else:
#         vessel.control.throttle = 0
#
#
# while vessel.flight().mean_altitude > 5000:
#     if vessel.flight(vessel.orbit.body.reference_frame).speed > 100:
#         vessel.auto_pilot.target_pitch_and_heading(90, 90)
#         vessel.control.throttle = 1
#         print(altitude(), velocity())
#     else:
#         vessel.control.throttle = 0
# while vessel.flight().mean_altitude > 1000:
#     vessel.auto_pilot.target_pitch_and_heading(90, 90)
#     velocity = vessel.flight(vessel.orbit.body.reference_frame).velocity
#     print('Surface velocity = (%.1f, %.1f, %.1f)' % velocity)
#     speed = vessel.flight(vessel.orbit.body.reference_frame).speed
#     print('Surface speed = %.1f m/s' % speed)
#     sleep(1)
#     if vessel.flight(vessel.orbit.body.reference_frame).speed > 60:
#         vessel.control.throttle = 1
#     else:
#         vessel.control.throttle = .1
#
#     while vessel.flight().mean_altitude < 1000:
#         vessel.auto_pilot.target_pitch_and_heading(90, 90)
#         if vessel.flight(vessel.orbit.body.reference_frame).speed > 50:
#             vessel.control.throttle = 1
#         else:
#             vessel.control.throttle = .05
#
#         while vessel.flight().mean_altitude < 200:
#             if vessel.flight(vessel.orbit.body.reference_frame).speed > 10:
#                 vessel.control.throttle = 1
#             else:
#                 vessel.control.throttle = 0
#
#             while vessel.flight().mean_altitude < 100:
#                 if vessel.flight(vessel.orbit.body.reference_frame).speed > 4:
#                     vessel.control.throttle = 1
#                 else:
#                     vessel.control.throttle = 0
#
#                 while vessel.flight().mean_altitude < 50:
#                     if vessel.flight(vessel.orbit.body.reference_frame).speed > 2:
#                         vessel.control.throttle = .5
#                     else:
#                         vessel.control.throttle = 0
# if stages > 1:
#     stage_2_resources = vessel.resources_in_decouple_stage(stage = 2, cumulative = False)
#     launcher_fuel = conn.add_stream(stage_2_resources.amount, 'LiquidFuel')
#
#
# #Pre-Launch Setup
# vessel.control.sas = False
# vessel.control.rcs = False
# vessel.control.throttle = 1
#
# # vessel = conn.add_stream()
# vessel.auto_pilot.target_pitch_and_heading(90,90)
# print('Launch!')
# vessel.control.activate_next_stage()
# vessel.auto_pilot.engage()
# # while altitude > 0:
# alt1 = vessel.flight().mean_altitude
# time.sleep(1)
# alt2 = vessel.flight().mean_altitude
#
# while alt1 < alt2:
#     print(vessel.flight().mean_altitude)
#     sleep(1)
#
# while 1:
#     if vessel.flight().mean_altitude < 2000:
#         vessel.control.activate_next_stage()
#         print("Ending and Breaking Loop PARACHUTE")
#         break
#
# while vessel.flight(vessel.orbit.body.reference_frame).vertical_speed < -0.1:
#     print('Altitude = %.1f meters' % vessel.flight().surface_altitude)
# time.sleep(1)
# print('Landed!')
# # if alt1 > alt2:
# #     if altitude < 1000:
# #         vessel.control.activate_next_stage()
