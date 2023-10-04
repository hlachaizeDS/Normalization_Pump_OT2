import serial


def colOfLabware(labware, col, wellNb):
    if wellNb == 24:
        lineNb = 4
    if wellNb == 96:
        lineNb = 8
    if wellNb == 4:
        lineNb = 1
    if wellNb == 12:
        lineNb = 1

    return labware + ".wells()[" + str((col-1) * lineNb) + "]"


def pickup_tips_multi_WL(protocolFile, pipet, tipLabware, column):
    #protocolFile.write("    " + pipet + ".pick_up_tip(" + tipLabware + ".wells()[" + str((column-1)*8) + "], 2, 6.0)\n")
    protocolFile.write("    " + pipet + ".pick_up_tip(" + tipLabware + ".wells()[" + str((column-1)*8) + "])\n")


def pickup_tips_multi_one_tip_WL(protocolFile, pipet, tipLabware, column, force):
    protocolFile.write("    " + pipet + ".pick_up_tip(" + tipLabware + ".wells()[" + str((column-1)*8) + "], 2, " + str(force) + ")\n")


def pickup_tips_single_WL(protocolFile, pipet, tipLabware, well):
    protocolFile.write("    " + pipet + ".pick_up_tip(" + tipLabware + ".wells()[" + str(well) + "], 2, 6.0)\n")


def pipet_Zaxis_speed_WL(protocolFile, speed):
    protocolFile.write("    protocol.max_speeds['Z'] = " + str(speed) + "\n")  # only for left Pipette


def pipet_Xaxis_speed_WL(protocolFile, speed):
    protocolFile.write("    protocol.max_speeds['X'] = " + str(speed) + "\n")


def pipet_Yaxis_speed_WL(protocolFile, speed):
    protocolFile.write("    protocol.max_speeds['Y'] = " + str(speed) + "\n")


def aspirate_WL(protocolFile, pipet, location, volume, flow_rate):
    if volume != 0:
        protocolFile.write("    " + pipet + ".aspirate(" + str(volume) + ", " + location + ", " + str(flow_rate)
                           + ")\n")


def dispense_WL(protocolFile, pipet, location , volume, flow_rate):
    if volume != 0:
        protocolFile.write("    " + pipet + ".dispense(" + str(volume) + ", " + location + ", " + str(flow_rate)
                           + ")\n")


def air_gap_WL(protocolFile, pipet, air_vol):
    protocolFile.write("    " + pipet + ".air_gap(" + str(air_vol) + ")\n")


def return_WL(protocolFile, pipet):
    protocolFile.write("    " + pipet + ".return_tip()\n")


def drop_WL(protocolFile, pipet):
    protocolFile.write("    " + pipet + ".drop_tip()\n")


def mix_WL(protocolFile, pipet, repetitions, volume, location, flow_rate):
    protocolFile.write("    " + pipet + ".mix(" + str(repetitions) + ", " + str(volume) + ", " + location + ", "
                       + str(flow_rate)+")\n")


def mix_noLoc_WL(protocolFile, pipet, repetitions, volume, flow_rate):  #noLoc = no location
    protocolFile.write("    " + pipet + ".mix(" + str(repetitions) + ", " + str(volume) + ", rate=" + str(flow_rate)
                       + ")\n")


def blow_out_WL(protocolFile, pipet, location=""):
    protocolFile.write("    " + pipet + ".blow_out(" + location + ")\n")


def touch_tip_WL(protocolFile, pipet, location, radius=1, offset=-1):
    protocolFile.write("    " + pipet + ".touch_tip(" + location + ", radius=" + str(radius) + ", v_offset=" + str(offset) + ")\n")


def move_to_WL(protocolFile, pipet, location):
    protocolFile.write("    " + pipet + ".move_to(" + str(location) + ")\n")


def delay_WL(protocolFile, seconds=0, minutes=0):
    protocolFile.write("    protocol.delay(seconds=" + str(seconds) + ", minutes=" + str(minutes) + ")\n")


def comment_WL(protocolFile: object, msg: object) -> object:
    protocolFile.write("    protocol.comment(\"" + msg + "\")\n")


def pause_WL(protocolFile):
    protocolFile.write("    protocol.pause()\n")


def move_well_center_WL(protocolFile, positionName, well, x=0, y=0, z=0):
    protocolFile.write("    " + str(positionName) + " = " + str(well) + ".center().move(types.Point(x=" + str(x)
                       + ", y=" + str(y) + ", z=" + str(z) + "))\n")

#PUMP CONTROL
#need to place pyTMCL and DispensUnit_1161 in /data of the Opentrons to be used,
#along with some additional parameters in header

def init(protocolFile, volume):
    protocolFile.write("    if protocol.is_simulating()==False:" + "\n")
    protocolFile.write("        pump_1.init()" + "\n")

def dispense(protocolFile, volume):
    protocolFile.write("    if protocol.is_simulating()==False:" + "\n")
    protocolFile.write("        pump_1.wait_for_idle()" + "\n")
    protocolFile.write("        pump_1.dispense(" + str(volume) + ")" + "\n")
    protocolFile.write("        pump_1.wait_for_canmove()" + "\n")

# Arduino elementary functions
def sendSerial(protocolFile, COMPORT, intToTransfer):
    protocolFile.write("    ser = serial.Serial(\"" + COMPORT + "\", 9600)\n")
    protocolFile.write("    ser.write(b\'" + str(intToTransfer) + "\\r\\n\')\n")
    protocolFile.write("    ser.close()\n")


def startStirring(protocolFile, COMPORT):
    comment_WL(protocolFile, "Start Stirring")
    sendSerial(protocolFile, COMPORT, 900)


def stopStirring(protocolFile, COMPORT):
    comment_WL(protocolFile, "Stop Stirring")
    sendSerial(protocolFile, COMPORT, 1)


def startVac(protocolFile, COMPORT):
    comment_WL(protocolFile, "Start Vac")
    sendSerial(protocolFile, COMPORT, 2500)


def stopVac(protocolFile, COMPORT):
    comment_WL(protocolFile, "Stop Vac")
    sendSerial(protocolFile, COMPORT, 3000)


def startHeating(protocolFile, COMPORT):
    comment_WL(protocolFile, "Start heating")
    sendSerial(protocolFile, COMPORT, 1500)


def stopHeating(protocolFile, COMPORT):
    comment_WL(protocolFile, "Stop heating")
    sendSerial(protocolFile, COMPORT, 2000)


def startVent (protocolFile, COMPORT):
    comment_WL(protocolFile, "Start vent")
    sendSerial(protocolFile, COMPORT, 3500)


def stopVent (protocolFile, COMPORT):
    comment_WL(protocolFile, "Stop vent")
    sendSerial(protocolFile, COMPORT, 4000)


def incubate(protocolFile, COMPORT, seconds=0, minutes=0):
    if seconds == 0 and minutes == 0:
        delay_WL(protocolFile, 2)
        return
    startStirring(protocolFile, COMPORT)
    delay_WL(protocolFile, seconds, minutes)
    stopStirring(protocolFile, COMPORT)


# def vacuum(protocolFile, COMPORT, seconds=0, minutes=0):
#     startVac(protocolFile, COMPORT)
#     delay_WL(protocolFile, seconds, minutes)
#     stopVac(protocolFile, COMPORT)
#     delay_WL(protocolFile, 3)

def vacuum(protocolFile, COMPORT, VacSeconds=0, VacMinutes=0, VentSeconds=12, VentMinutes=0):
    startVac(protocolFile, COMPORT)
    delay_WL(protocolFile, VacSeconds-6, VacMinutes)
    startVent(protocolFile, COMPORT)
    delay_WL(protocolFile, 6, 0)
    stopVac(protocolFile, COMPORT)
    delay_WL(protocolFile, VentSeconds-6, VentMinutes)
    stopVent(protocolFile, COMPORT)


def vent(protocolFile, COMPORT, seconds=0, minutes=0):
    startVent(protocolFile, COMPORT)
    delay_WL(protocolFile, seconds, minutes)
    stopVent(protocolFile, COMPORT)


# Bioshake elementary functions
def startStirringBioshake(protocolFile, COMPORT, velocity):
    comment_WL(protocolFile, "Start Stirring Bioshake")
    protocolFile.write("    ser = serial.Serial(\'" + COMPORT + "\', timeout=1)\n")
    protocolFile.write("    command = 'ssts' + str(" + str(velocity) + ") + \'\\r\'\n")
    protocolFile.write("    ser.write(bytes(command, 'ascii'))\n")
    delay_WL(protocolFile, 1)
    protocolFile.write("    ser.write(b\'son\\r\')\n")
    delay_WL(protocolFile, 1)
    protocolFile.write("    ser.close()\n")


def stopStirringBioshake(protocolFile, COMPORT):
    comment_WL(protocolFile, "Stop Stirring Bioshake")
    protocolFile.write("    ser = serial.Serial(\'" + COMPORT + "\', timeout=1)\n")
    protocolFile.write("    ser.write(b\'soff\\r\')\n")
    delay_WL(protocolFile, 1)
    protocolFile.write("    ser.close()\n")


def startHeatingBioshake(protocolFile, COMPORT, temperature):
    comment_WL(protocolFile, "Start Heating Bioshake")
    protocolFile.write("    ser = serial.Serial(\'" + COMPORT + "\', timeout=1)\n")
    protocolFile.write("    command = 'stt' + str(" + str(temperature) + "0) + \'\\r\'\n")
    protocolFile.write("    ser.write(bytes(command, 'ascii'))\n")
    delay_WL(protocolFile, 1)
    protocolFile.write("    ser.write(b\'ton\\r\')\n")
    delay_WL(protocolFile, 1)
    protocolFile.write("    ser.close()\n")


def stopHeatingBioshake(protocolFile, COMPORT):
    comment_WL(protocolFile, "Stop Heating Bioshake")
    protocolFile.write("    ser = serial.Serial(\'" + COMPORT + "\', timeout=1)\n")
    protocolFile.write("    ser.write(b\'toff\\r\')\n")
    delay_WL(protocolFile, 1)
    protocolFile.write("    ser.close()\n")


def incubateBioshake(protocolFile, COMPORT, velocity, seconds=0,minutes=0):
    startStirringBioshake(protocolFile, COMPORT, velocity)
    delay_WL(protocolFile, seconds, minutes)
    stopStirringBioshake(protocolFile, COMPORT)


# PRESSURE CONTROLLER
def sendSerial_pressure(protocolFile, PRESSURE_COMPORT, msg):
    protocolFile.write("    ser = serial.Serial(\"" + PRESSURE_COMPORT + "\",57600)\n")
    protocolFile.write("    ser.write(b\'" + msg + "\\r\\n\')\n")
    protocolFile.write("    ser.close()\n")


def changePressure(protocolFile, PRESSURE_COMPORT, pressure):
    sendSerial_pressure(protocolFile, PRESSURE_COMPORT, "cC " + str(pressure))


def startPressure(protocolFile, PRESSURE_COMPORT):
    sendSerial_pressure(protocolFile, PRESSURE_COMPORT, "dB")


def stopPressure(protocolFile, PRESSURE_COMPORT):
    sendSerial_pressure(protocolFile, PRESSURE_COMPORT, "dE")