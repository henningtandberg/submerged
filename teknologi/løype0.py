#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca
import time


def run():
    chewie = Chewbacca()
     
    # kjører opp og løser M07
    v = chewie.drive_gyro_dist(start_speed= 0, speed= 300, end_speed= 300,
                               target_distance= 95, target_angle= 0,
                               stop_at_end= False)

    v = chewie.drive_gyro_turn(start_speed= v, speed= 300, end_speed= 300, 
                               turn_radius= 250, turn_angle= 70,
                               stop_at_end= False)
    
    v = chewie.drive_gyro_dist(start_speed= v, speed= 300, end_speed= 0,
                               target_distance= 202, target_angle= 80,
                               stop_at_end= True)
    
    chewie.work_motor_L(speed= -500, target_rotation= 250)

    chewie.motor_L.run_angle(40, -10)  #Venstre hjul litt bak
    chewie.work_motor_L(speed= -500, target_rotation= 1055)

    #time.sleep(1)

    # kjører opp mot og løser M01
    v = chewie.drive_gyro_dist(start_speed= 0, speed= 100, end_speed= 0,
                               target_distance= -110, target_angle= 90,
                               stop_at_end= False)


    v = chewie.drive_gyro_turn(start_speed= 0, speed= 100, end_speed= 100, 
                               turn_radius= chewie.WHEEL_DISTANSE / 2, turn_angle= -80,
                               stop_at_end= False)

    v = chewie.drive_gyro_dist(start_speed= v, speed= 100, end_speed= 100,
                               target_distance= 120, target_angle= 0,
                               stop_at_end= False)

    v = chewie.drive_gyro_turn(start_speed= v, speed= 100, end_speed= 0, 
                               turn_radius= chewie.WHEEL_DISTANSE / 2, turn_angle= -85,
                               stop_at_end= False)

    
    v = chewie.drive_gyro_dist(start_speed= v, speed= 70, end_speed= 0,
                               target_distance= 68, target_angle= -90,
                               stop_at_end= True)
    

    # kjører opp mot og løser M02
    v = chewie.drive_gyro_dist(start_speed= v, speed= -100, end_speed= 0,
                               target_distance= 170, target_angle= -90,
                               stop_at_end= False)

    v = chewie.drive_gyro_turn(start_speed= v, speed= 100, end_speed= 0, 
                               turn_radius= chewie.WHEEL_DISTANSE / 2, turn_angle= 35,
                               stop_at_end= False, turn_right= True)


    v = chewie.drive_gyro_dist(start_speed= v, speed= 100, end_speed= 0,
                               target_distance= 205, target_angle= -50,
                               stop_at_end= True)
    
    chewie.work_motor_L(speed= 500, target_rotation= 1330)
 
    chewie.work_motor_L(speed= 500, target_rotation= -800)


    # kjører opp mot og løser M03
    v = chewie.drive_gyro_turn(start_speed= v, speed= -200, end_speed= 0, 
                                turn_radius= 300, turn_angle= 40,
                                stop_at_end= False,)
    
    v = chewie.drive_gyro_turn(start_speed= v, speed= -200, end_speed= 0, 
                                turn_radius= 200, turn_angle= 55,
                                stop_at_end= True,)

    v = chewie.drive_gyro_turn(start_speed= v, speed= -100, end_speed= 0, 
                                turn_radius= 100, turn_angle= -90,
                                stop_at_end= True,)
    
    v = chewie.drive_gyro_dist(start_speed= v, speed= 100, end_speed= 0,
                               target_distance= 117, target_angle= -54  ,
                               stop_at_end= True)
    

    chewie.work_motor_L(speed= 500, target_rotation= 500)
    chewie.work_motor_L(speed= 500, target_rotation= -550)

    v = chewie.drive_gyro_turn(start_speed= v, speed= -100, end_speed= 0, 
                                turn_radius= 300, turn_angle= -32,
                                stop_at_end= True,)
    
    v = chewie.drive_gyro_turn(start_speed= v, speed= 70, end_speed= 0, 
                                turn_radius= chewie.WHEEL_DISTANSE / 2, turn_angle= 40,
                                stop_at_end= False,)

    v = chewie.drive_gyro_turn(start_speed= v, speed= 70, end_speed= 0, 
                                turn_radius= chewie.WHEEL_DISTANSE / 2, turn_angle= 40,
                                stop_at_end= True,)

    chewie.work_motor_L(speed= 500, target_rotation= -1050)

    v = chewie.drive_gyro_turn(start_speed= v, speed= -70, end_speed= 0, 
                                turn_radius= chewie.WHEEL_DISTANSE / 2, turn_angle= -6,
                                stop_at_end= False,)

    v = chewie.drive_gyro_dist(start_speed= v, speed= 100, end_speed= 0,
                               target_distance= 123, target_angle= 90  ,
                               stop_at_end= True)

    # v = chewie.drive_gyro_dist(start_speed= v, speed= 100, end_speed= 0,
    #                            target_distance= -70 , target_angle= -50,
    #                            stop_at_end= True)

    # v = chewie.drive_gyro_turn(start_speed= v, speed= 60, end_speed= 0, 
    #                            turn_radius= 0, turn_angle= -125,
    #                            stop_at_end= True,)
    
    # time.sleep(5)
    
    # v = chewie.drive_gyro_dist(start_speed= v, speed= 100, end_speed= 0,
    #                            target_distance= -190  , target_angle= -180,
    #                            stop_at_end= True)

    # chewie.press_robot_frem(-45)
    # time.sleep(2)
    # chewie.set_known_heading(180)
    # chewie.press_robot_frem_ferdig()

