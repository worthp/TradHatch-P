#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import typing

import commands2
from wpilib import DataLogManager
from wpilib import DriverStation

from robotcontainer import RobotContainer


class MyRobot(commands2.TimedCommandRobot):

    autonomousCommand: typing.Optional[commands2.Command] = None

    """
    This function is run when the robot is first started up and should be used for any
    initialization code.
    """
    def __init__(self) -> None:
        super().__init__()

        # Instantiate our RobotContainer.  This will perform all our button bindings, and put our
        # autonomous chooser on the dashboard.
        self.container = RobotContainer()

        # Start recording to data log
        DataLogManager.start()

        # Record DS control and joystick data.
        # Change to `false` to not record joystick data.
        DriverStation.startDataLog(DataLogManager.getLog(), True)

    def disabledInit(self) -> None:
        """This function is called once each time the robot enters Disabled mode."""

    def disabledPeriodic(self) -> None:
        """This function is called periodically when disabled"""

    def autonomousInit(self) -> None:
        self.autonomousCommand = self.container.getAutonomousCommand()

        if self.autonomousCommand:
            self.autonomousCommand.schedule()

    def autonomousPeriodic(self) -> None:
        pass

    def teleopInit(self) -> None:
        if self.autonomousCommand:
            self.autonomousCommand.cancel()

    def teleopPeriodic(self) -> None:
        """This function is called periodically during operator control"""

    def utilityInit(self) -> None:
        # Cancels all running commands at the start of utility mode
        commands2.CommandScheduler.getInstance().cancelAll()
