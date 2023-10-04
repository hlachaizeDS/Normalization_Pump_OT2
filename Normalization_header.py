from opentrons import protocol_api,types
import serial
import time
import sys


metadata = {'apiLevel': '2.3'}

def run(protocol: protocol_api.ProtocolContext):

    if protocol.is_simulating() == False:
        sys.path.insert(0, "/data")
        import DispenseUnit_1161
        import pyTMCL
        serial_port = serial.Serial("/dev/ttyACM0", 9600)
        bus = pyTMCL.connect(serial_port)
        pump_1 = DispenseUnit_1161.DispenseUnit_1161("fakeparent", bus, 1, 0)

    # Pipets
    p300 = protocol.load_instrument('p300_multi_gen2', 'left')
    p20 = protocol.load_instrument('p20_multi_gen2', 'right')

    # Tips
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', 9)
    tiprack_20 = protocol.load_labware('opentrons_96_tiprack_20ul', 3)

    # Plates
    mother_plate = protocol.load_labware('greiner_96_petit_puit', 8)
    plate_to_normalize = protocol.load_labware('axygenpcr_96_wellplate_200ul_onspacer', 5)
    op2_plate = protocol.load_labware('axygenpcr_96_wellplate_200ul', 2)

    # Reservoirs
    LadderReservoir = protocol.load_labware('ladder_4_reservoir_63000ul', 6)
