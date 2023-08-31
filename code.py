import time
import board
import digitalio
import pwmio

from adafruit_motor import motor

PWM_MLA = board.GP12
PWM_MLB = board.GP13
PWM_MLC = board.GP1
PWM_MLD = board.GP2

pwm_La = pwmio.PWMOut(PWM_MLA, frequency=10000)
pwm_Lb = pwmio.PWMOut(PWM_MLB, frequency=10000)
pwm_Lc = pwmio.PWMOut(PWM_MLC, frequency=10000)
pwm_Ld = pwmio.PWMOut(PWM_MLD, frequency=10000)


Left_Motor = motor.DCMotor(pwm_La, pwm_Lb)
Left_Motor_speed = 0
Right_Motor = motor.DCMotor(pwm_Lc, pwm_Ld)
Right_Motor_speed = 0



while True:

    Left_Motor_speed = -1
    Left_Motor.throttle = Right_Motor_speed
    time.sleep(2)
    Left_Motor_speed = 1
    Left_Motor.throttle = Right_Motor_speed
    time.sleep(2)

    Right_Motor_speed = -1
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(2)
    Right_Motor_speed = 1
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(2)
# Write your code here :-)
