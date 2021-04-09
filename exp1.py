#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on April 09, 2021, at 16:54
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# Importing all the required packages
from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os
import sys
from psychopy.hardware import keyboard


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session - timestamp, participant info, psychopy tool info
psychopyVersion = '2020.2.10'
expName = 'exp1'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + \
    u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath='C:\\Users\\smjba\\Desktop\\psyexp\\exp1.py',
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
# this outputs to the screen, not a file
logging.console.setLevel(logging.WARNING)

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame


# Setup the Window monitor
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess


# Initialize components for "Instructions" of Task 1
InstructionsClock = core.Clock()
instructionstext = visual.TextStim(win=win, name='instructionstext',
                                   text='Choose the color of letters ignoring the word\n\nleft = red\nright = blue\ndown = green\n',
                                   font='Arial',
                                   pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                                   color='white', colorSpace='rgb', opacity=1,
                                   languageStyle='LTR',
                                   depth=0.0)
key_resp = keyboard.Keyboard()


# Initialize components for Routine "task1"
trail1Clock = core.Clock()
target1 = visual.TextStim(win=win, name='target1',
                          text='default text',
                          font='Arial',
                          pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                          color='white', colorSpace='rgb', opacity=1,
                          languageStyle='LTR',
                          depth=0.0)
response1 = keyboard.Keyboard()


# Initialize components for Routine "Instructions2" of task2
Instructions2Clock = core.Clock()
Instructiontext2 = visual.TextStim(win=win, name='Instructiontext2',
                                   text='Now the word text and color of words can be different. Choose response based on color of word and not the text of word.',
                                   font='Arial',
                                   pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                                   color='white', colorSpace='rgb', opacity=1,
                                   languageStyle='LTR',
                                   depth=0.0)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "task2"
trial2Clock = core.Clock()
target2 = visual.TextStim(win=win, name='target2',
                          text='default text',
                          font='Arial',
                          pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                          color='white', colorSpace='rgb', opacity=1,
                          languageStyle='LTR',
                          depth=0.0)
response2 = keyboard.Keyboard()
