import RPi.GPIO as GPIO
from time import sleep
import threading


class Motor_thread():
    dc_motor = None
    motor_thread = None

    def __init__(self):
        print('***** init {}'.format(self.__class__.__name__))
        self.dc_motor = Dc_motor()

    # def key_thread_watcher(self, key):
    #     if key == None:
    #         self.key_released()
    #     else:
    #         self.motor_thread = threading.Thread(target=self.dc_motor.main_loop, args=(key,))
    #         self.motor_thread.start()
    #
    # def key_released(self):
    #     try:
    #         if self.motor_thread.isAlive():
    #             self.motor_thread.join()
    #             self.motor_thread = threading.Thread(target=self.dc_motor.main_loop, args=('s',))
    #             self.motor_thread.start()
    #             self.motor_thread.join()
    #     except AttributeError:
    #         pass

    def key_watcher(self, key):
        self.dc_motor.main_loop(key)


class Dc_motor():
    enA = 26
    in1 = 19
    in2 = 13

    in3 = 21
    in4 = 20
    enB = 16

    key = None

    def __init__(self):
        print('***** init {}'.format(self.__class__.__name__))

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.setup(self.enA, GPIO.OUT)
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        self.p = GPIO.PWM(self.enA, 100)
        self.p.start(100)

        GPIO.setup(self.in3, GPIO.OUT)
        GPIO.setup(self.in4, GPIO.OUT)
        GPIO.setup(self.enB, GPIO.OUT)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.LOW)
        self.p2 = GPIO.PWM(self.enB, 100)
        self.p2.start(100)


    def main_loop(self, key=None):

        if key == 'ArrowUp':
            # print("run")
            GPIO.output(self.in1, GPIO.HIGH)
            GPIO.output(self.in2, GPIO.LOW)
            GPIO.output(self.in3, GPIO.HIGH)
            GPIO.output(self.in4, GPIO.LOW)
            key = 'z'

        elif key == 'ArrowDown':
            GPIO.output(self.in1, GPIO.LOW)
            GPIO.output(self.in2, GPIO.HIGH)
            GPIO.output(self.in3, GPIO.LOW)
            GPIO.output(self.in4, GPIO.HIGH)
            x = 'z'

        elif key == 'ArrowRight':
            GPIO.output(self.in1, GPIO.LOW)
            GPIO.output(self.in2, GPIO.HIGH)
            GPIO.output(self.in3, GPIO.HIGH)
            GPIO.output(self.in4, GPIO.LOW)
            x = 'z'

        elif key == 'ArrowLeft':
            GPIO.output(self.in1, GPIO.HIGH)
            GPIO.output(self.in2, GPIO.LOW)
            GPIO.output(self.in3, GPIO.LOW)
            GPIO.output(self.in4, GPIO.HIGH)
            x = 'z'


        elif key in ['s', None]:
            # print("stop")
            GPIO.output(self.in1, GPIO.LOW)
            GPIO.output(self.in2, GPIO.LOW)
            GPIO.output(self.in3, GPIO.LOW)
            GPIO.output(self.in4, GPIO.LOW)
            x = 'z'


        # elif key == 'l':
        #     # print("low")
        #     p.ChangeDutyCycle(50)
        #     p2.ChangeDutyCycle(50)
        #     x = 'z'
        #
        # elif key == 'm':
        #     # print("medium")
        #     self.p.ChangeDutyCycle(75)
        #     self.p2.ChangeDutyCycle(75)
        #     x = 'z'
        #
        # elif key == 'h':
        #     # print("high")
        #     self.p.ChangeDutyCycle(100)
        #     self.p2.ChangeDutyCycle(100)
        #     x = 'z'

        elif key == 'e':
            GPIO.cleanup()


        else:
            pass
            # print("<<<  wrong data  >>>")
            # print("please enter the defined data to continue.....")

    # GPIO.cleanup()


if __name__ == '__main__':
    dc_motor = Dc_motor()
    dc_motor.main_loop()
