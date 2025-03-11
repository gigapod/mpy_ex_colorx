
##
# @file blink.py
# @brief This file contains functions to control LED transitions and a blinky example for use in micropython
# @details
# This module provides the `led_transition` function to smoothly transition an LED to a specified RGB value and
# the `blinky` function to demonstrate color transitions.
#
# @note This code is designed to work with the `neopixel` library and a compatible microcontroller, such as the
# SparkFun IoT RedBoard - ESP32, or the SparkFun IoT RedBoard - RP2350
#
# @author SparkFun Electronics
# @date March 2025
# @copyright Copyright (c) 2024-2025, SparkFun Electronics Inc.
#
# SPDX-License-Identifier: MIT
# @license MIT
#

import machine, neopixel, time


def wink_led(led) :

    cur_clr = led[0]
    # wink the LED ...
    for i in range(0, 3):
        led[0] = [0, 0, 0]
        led.write()
        time.sleep_ms(100)
        led[0] = cur_clr
        led.write()
        time.sleep_ms(100)

#---------------------------------------------------------------------------------
# Transition the current LED value to a given RGB value.
# This function assumes pixel color/channel values are 8 bit (0-255)
def led_transition(led, R, G, B):
    """
        @brief Transition the current LED value to a given RGB value.

        This function assumes pixel color/channel values are 8-bit (0-255).

        @param led The LED object to be controlled. It is expected to be a `neopixel.NeoPixel` object.
        @param R The target red color value (0-255).
        @param G The target green color value (0-255).
        @param B The target blue color value (0-255).

        @details
        - Retrieves the current color of the LED
        - transitions the current color to the provided color over a series of increments.
        - Also outputs a dot for each increment to indicate progress.

        @example
        @code
        led_transition(led, 255, 0, 0);  // Transition to red color
        @endcode
        """

    #  get current led value - which is a tuple
    #  Note - we convert to a list to support value assignment below.
    clrCurrent = list(led[0])

    # How many increments during the transition
    inc = 51 # 255/5

    # how much to change a value every increment
    rInc = (R - clrCurrent[0])/inc
    gInc = (G - clrCurrent[1])/inc
    bInc = (B - clrCurrent[2])/inc

    # loop - adjust color during each increment.
    for i in range(0, inc):

        # add the desired increment to each color value. Use route() to convert the float value to an integer
        clrCurrent[0] = round(clrCurrent[0] + rInc)
        clrCurrent[1] = round(clrCurrent[1] + gInc)
        clrCurrent[2] =  round(clrCurrent[2] + bInc)

        # set the new LED color and write (enable) it
        led[0] = clrCurrent
        led.write()

        # indicate process ... add a small delay
        print(".", end='')
        time.sleep_ms(20)


def blinky():
    pin = machine.Pin("NEOPIXEL")
    led = neopixel.NeoPixel(pin, 1)

    # start at off
    led[0] = (0, 0, 0)
    led.write()

    print("\n-----------------------------------------------------------")
    print("On-board LED color example...")
    print("-----------------------------------------------------------\n")
    time.sleep_ms(100);

    # print("Off to Blue:", end='')
    print("<Off>\t", end='')
    led_transition(led, 0, 0, 255)
    print(" <Blue>")
    wink_led(led)

    print("<Blue>\t", end='')
    led_transition(led, 255, 0, 0)
    print(" <Red>")
    wink_led(led)

    print("<Red>\t", end='')
    led_transition(led, 0, 255, 0)
    print(" <Green>")
    wink_led(led)

    print("<Green>\t", end='')
    led_transition(led, 255, 255, 0)
    print(" <Yellow>")
    wink_led(led)

    print("<Yellow>", end='')
    led_transition(led, 255, 255, 255)
    print(" <White>")
    wink_led(led)

    print("<White>\t", end='')
    led_transition(led, 0, 0, 0)
    print(" <Off>")

    print("\nDone!\n")

    led[0]=(0,0,0)
    led.write()

    # for i in range(0, 255, 5)
    #
    #     print(".", end='')
    #     led[0] = (i, 0, 255-i)
    #     led.write()
    #     time.sleep_ms(100)
    #
    # print("\nRed to Green:", end='')
    # for i in range(0, 255, 5):
    #     print(".", end='')
    #     led[0] = (255-i, i, 0)
    #     led.write()
    #     time.sleep_ms(100)
    #
    # print("\nGreen to Blue:", end='')
    # for i in range(0, 255, 5):
    #     print(".", end='')
    #     led[0] = (0, 255-i, i)
    #     led.write()
    #     time.sleep_ms(100)

    # led[0] = (0, 0, 0)
    # led.write()
    # print("\nBlink Example Done")