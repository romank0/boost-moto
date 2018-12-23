#!/usr/bin/env python3

from pyb00st.movehub import MoveHub
from pyb00st.constants import *
from time import sleep

mymovehub = MoveHub('00:16:53:AA:9F:76', 'BlueGiga', '')

try:
    mymovehub.start()
    print(mymovehub.get_name())

    for i in range(20):
        # turn motor A ON for 1000 ms at 100% duty cycle in both directions
        mymovehub.run_motor_for_time(MOTOR_A, 1000, 100)
        sleep(1)
        mymovehub.run_motor_for_time(MOTOR_A, 1000, -100)
        sleep(1)

finally:
    mymovehub.stop()


