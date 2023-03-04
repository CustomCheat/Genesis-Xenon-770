import sys
import time
from array import array

import usb.core
import usb.util
import re
import binascii
import random
VID = 0x258A
PID = 0x0027

dev = None
wIndex = None


def main():
    attach_mouse()
    # set_color("ed1004")
    #print("Original: " + getMemory(True))
    #while True:
        #set_color_to_memory(getMemory(True), str(hex(random.randint(0,16777215))).replace("0x", ""), 1)
        #time.sleep(0.3)
    #setFlickerModeColor(getMemory(True), "fc0093", 2)
    #setMode(getMemory(True), 1)
    #setModeColor(getMemory(True), "fc0000", 6)
    #setMode(getMemory(Tru, 9e), 5)
    #setModeColor(getMemory(True), "0e11ea", 5)
    #setMode(getMemory(True), 3)
    #setBreathingModeColor(getMemory(True), "FF0004", 1)
    #setBreathingModeColor(getMemory(True), "4612E2", 2)
    #setBreathingModeColor(getMemory(True), "CCE212", 3)
    #setKey3("11020000")
    setMacro(7,"31013203") 
    #setSteadyModeBrightness(getMemory(True), 4)
    #setModeColor(getMemory(True), "780eea", 9)
   # setBreathingModeColor(getMemory(True), "000000", 1)
    # flicker, star twinkle, breathing, wave
    #setMode(getMemory(True), 8)
    #setSteadyColor(getMemory(True), "780eea")
    # dev.ctrl_transfer(0x21, 0x09, 0x0305, 1, binascii.unhexlify('051100000000'))
    # dev.ctrl_transfer(0x21, 0x09, 0x0304, 1, binascii.unhexlify(
    # '0411007b00000600640e0416c0070b17232f3d00000000000000000000ffff0000ff00ff00000000ffff00ff00ffff00000000000001320040ff00004206ff00000000ff8000fffac603fa036afa00fa000000424240ff00000000ff00ff008000fffac603fa036a000000000000ff0000ff000042ff00000000ff42420000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'))
    # dev.ctrl_transfer(0x21, 0x09, 0x0305, 1, binascii.unhexlify('050201000000'))
    # set_color("ed1004")
    detach_mouse()
defaultMapping = '04120050000000001101000011020000110400004101000041020000110100001102000011020000110100001102000011020000110100001102000011020000500100005001000050010000500100005001000050010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
def test():
    a = dev.ctrl_transfer(0x21, 0x09, 0x0304, 1, '')
    dev.ctrl_transfer(0x21, 0x09, 0x0305,1, binascii.unhexlify('051100000000'))
    data = dev.ctrl_transfer(0xa1, 0x01, 0x0304,1, 520)
    dev.ctrl_transfer(0x21, 0x09, 0x0305,1, binascii.unhexlify('050201000000'))
    #print("data: " + str(data))
    #print("Done, code: " + str(a))
# 01 left click
# 02 right click
# 04 middle btn
# 10 forward
# 08 back
# 20 Scroll up
# 2ff scroll down
# 31013203 three click

def getKeyInBinary(num):
      switch={
      1:'13',
      2:'10',
      3:'7',
      4:'14',
      5:'11',
      6:'8',
      7:'15',
      8:'12',
      9:'9'
      }
      return switch.get(num,"Invalid input")

def setKey2(st):
    a = dev.ctrl_transfer(0x21, 0x09, 0x0304, 1, binascii.unhexlify(defaultMapping.replace("110800001108", "1108000011" + st)))
    dev.ctrl_transfer(0x21, 0x09, 0x0305,1, binascii.unhexlify('051100000000'))
    data = dev.ctrl_transfer(0xa1, 0x01, 0x0304,1, 520)
    dev.ctrl_transfer(0x21, 0x09, 0x0305,1, binascii.unhexlify('050201000000'))
    # 11010000
def setKey3(st):
    a = dev.ctrl_transfer(0x21, 0x09, 0x0304, 1, binascii.unhexlify(defaultMapping.replace("42040000", st)))
    dev.ctrl_transfer(0x21, 0x09, 0x0305,1, binascii.unhexlify('051100000000'))
    data = dev.ctrl_transfer(0xa1, 0x01, 0x0304,1, 520)
    dev.ctrl_transfer(0x21, 0x09, 0x0305,1, binascii.unhexlify('050201000000'))

def setMacro(kNum, macroData):
    writeTo = int(getKeyInBinary(kNum)) * 8
    newMem = list(defaultMapping)
    dataToList = list(macroData)
    for i in range(8):
        newMem[writeTo + i] = dataToList[i]
    newMem = ''.join(map(str, newMem))
    print(newMem)
    # this writes to the macro memory
    a = dev.ctrl_transfer(0x21, 0x09, 0x0304, 1, binascii.unhexlify(newMem))
    dev.ctrl_transfer(0x21, 0x09, 0x0305,1, binascii.unhexlify('051100000000'))
    data = dev.ctrl_transfer(0xa1, 0x01, 0x0304,1, 520)
    dev.ctrl_transfer(0x21, 0x09, 0x0305,1, binascii.unhexlify('050201000000'))
    
        
def print_error(msg):
    print('Error: ' + msg)
    sys.exit(1)


def set_color_to_memory(memory, color, dpi):
    if dpi == 0:
        dpi = memory[22]
    if dpi < 1 or dpi > 6:
        return
    if(len(color) != 6):
        while(len(color) != 6):
            color += "f"
    dpi1pos = 58
    dpipos = dpi1pos + (dpi - 1) * 6
    newMem = ""
    for i in range(len(memory)):
        if dpipos <= i and i < dpipos + 6:
            if dpipos == i:
                newMem += color
        else:
            newMem += memory[i]
    writeToMemory(newMem)
def writeToMemory(memory):
    dev.ctrl_transfer(0x21, 0x09, 0x0305, 1, binascii.unhexlify('051100000000'))
    dev.ctrl_transfer(0x21, 0x09, 0x0304, 1, binascii.unhexlify(memory))
    dev.ctrl_transfer(0x21, 0x09, 0x0305, 1, binascii.unhexlify('050201000000'))
# 0 = LED OFF; 1 = PRISMO effect; 2 = Steady; 3 = Breathing; 4 = Colorful Tail; 5 = Neon; 6 = Colorful Steady; 7 = Flicker; 8 = Stars Twinkle; 9 = Wave
def setMode(memory, modeNum):
    if modeNum < 0 or modeNum > 9:
        return;
    newMem = list(memory)
    newMem[107] = modeNum
    newMem =  ''.join(map(str, newMem))
    writeToMemory(newMem)
def setModeSpeed(memory, speed):
    newMem = list(memory)
    newMem[109] = speed
    newMem = ''.join(map(str, newMem))
    writeToMemory(newMem)
# 1 = 25% 2 = 50% 3 = 75% 4 = 100%
def setSteadyModeBrightness(memory, brightness):
    newMem = list(memory)
    newMem[112] = brightness
    newMem = ''.join(map(str, newMem))
    writeToMemory(newMem)
# direction is 0 or 1
def setPrismoEffectModeDirection(memory, direction):
    if direction != 0 and direction != 1:
        return
    newMem = list(memory)
    newMem[111] = direction
    newMem = ''.join(map(str, newMem))
    writeToMemory(newMem)

def setFlickerModeColor(memory, color, colornum):
    if colornum < 1 or colornum > 2:
        return
    if (len(color) != 6):
        while (len(color) != 6):
            color += "f"
    colormode1 = 234
    colorpos = colormode1 + (colornum - 1) * 6
    newMem = ""
    for i in range(len(memory)):
        if colorpos <= i and i < colorpos + 6:
            if colorpos == i:
                newMem += color
        else:
            newMem += memory[i]
    writeToMemory(newMem)
def setSteadyColor(memory, color):
    if(len(color) != 6):
        while(len(color) != 6):
            color += "f"
    steadycolorpos = 114
    newMem = ""
    for i in range(len(memory)):
        if steadycolorpos <= i and i < steadycolorpos + 6:
            if steadycolorpos == i:
                newMem += color
        else:
            newMem += memory[i]
    writeToMemory(newMem)
# 7 colors
def setBreathingModeColor(memory, color, colornum):
    if colornum < 1 or colornum > 7:
        return
    if(len(color) != 6):
        while(len(color) != 6):
            color += "f"
    colormode1 = 124
    colorpos = colormode1 + (colornum - 1) * 6
    newMem = ""
    for i in range(len(memory)):
        if colorpos <= i and i < colorpos + 6:
            if colorpos == i:
                newMem += color
        else:
            newMem += memory[i]
    writeToMemory(newMem)
def setColorfulSteadyModeColor(memory, color, colornum):
    if colornum < 1 or colornum > 6:
        return
    if(len(color) != 6):
        while(len(color) != 6):
            color += "f"
    colormode1 = 172
    colorpos = colormode1 + (colornum - 1) * 6
    newMem = ""
    for i in range(len(memory)):
        if colorpos <= i and i < colorpos + 6:
            if colorpos == i:
                newMem += color
        else:
            newMem += memory[i]
    writeToMemory(newMem)

def getMemory(senadble):
    dev.ctrl_transfer(0x21, 0x09, 0x0305, 1, binascii.unhexlify('051100000000'))
    test = dev.ctrl_transfer(0xa1, 0x01, 0x0304, 1, 520)
    string = ''.join(('%2s' % hex(d)[2:]).replace(' ', '0') for d in test)
    if not senadble:
        return string
    sendableMemory = list(string)
    sendableMemory[6] = "7"
    sendableMemory[7] = "b"
    sendableMemory = "".join(sendableMemory)
    for i in range(1040 - len(sendableMemory)):
        sendableMemory += "0"
    return sendableMemory




def attach_mouse():
    global dev
    global wIndex
    dev = usb.core.find(idVendor=VID, idProduct=PID)
    if dev is None:
        print_error('Device {:04x}:{:04x} not found.'.format(VID, PID))
    wIndex = 0x01
    if dev.is_kernel_driver_active(wIndex) is True:
        dev.detach_kernel_driver(wIndex)
        usb.util.claim_interface(dev, wIndex)


def detach_mouse():
    global dev
    global wIndex
    if wIndex is not None:
        usb.util.release_interface(dev, wIndex)
        dev.attach_kernel_driver(wIndex)
        dev = None
        wIndex = None


if __name__ == '__main__':
    main()


