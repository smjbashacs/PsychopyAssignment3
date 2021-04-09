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

# Initialize components for Routine "Instructions" of task 3
Instructions3Clock = core.Clock()
instructiontext3 = visual.TextStim(win=win, name='instructiontext3',
                                   text='Now you will have color filled rectangles along with words.\n\n',
                                   font='Arial',
                                   pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                                   color='white', colorSpace='rgb', opacity=1,
                                   languageStyle='LTR',
                                   depth=0.0)
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "task3"
trial3Clock = core.Clock()
target3 = visual.TextStim(win=win, name='target3',
                          text='default text',
                          font='Arial',
                          pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                          color='white', colorSpace='rgb', opacity=1,
                          languageStyle='LTR',
                          depth=0.0)
response3 = keyboard.Keyboard()
polygon = visual.Rect(
    win=win, name='polygon',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1, 1, 1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=0.2, depth=-2.0, interpolate=True)


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
# to track time remaining of each (non-slip) routine
routineTimer = core.CountdownTimer()


###################### Start of task 1 ###############################################################
continueRoutine = True
# update component parameters for each repeat
key_resp_1.keys = []
key_resp_1.rt = []
_key_resp_1_allKeys = []
# keep track of which components have finished
Instructions1Components = [instructionstext1, key_resp_1]
for thisComponent in Instructions1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
# t0 is time of first possible flip
Instructions1Clock.reset(-_timeToFirstFrame)
frameN = -1

# -------Run Routine "Instructions1"-------
while continueRoutine:
    # get current time
    t = Instructions1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instructions1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *instructionstext1* updates
    if instructionstext1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionstext1.frameNStart = frameN  # exact frame index
        instructionstext1.tStart = t  # local t and not account for scr refresh
        instructionstext1.tStartRefresh = tThisFlipGlobal  # on global time
        # time at next scr refresh
        win.timeOnFlip(instructionstext1, 'tStartRefresh')
        instructionstext1.setAutoDraw(True)

    # *key_resp_1* updates
    waitOnFlip = False
    if key_resp_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_1.frameNStart = frameN  # exact frame index
        key_resp_1.tStart = t  # local t and not account for scr refresh
        key_resp_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_1, 'tStartRefresh')  # time at next scr refresh
        key_resp_1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_1.clock.reset)  # t=0 on next screen flip
        # clear events on next screen flip
        win.callOnFlip(key_resp_1.clearEvents, eventType='keyboard')
    if key_resp_1.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_1.getKeys(keyList=None, waitRelease=False)
        _key_resp_1_allKeys.extend(theseKeys)
        if len(_key_resp_1_allKeys):
            # just the last key pressed
            key_resp_1.keys = _key_resp_1_allKeys[-1].name
            key_resp_1.rt = _key_resp_1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions1"-------
for thisComponent in Instructions1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructionstext1.started', instructionstext1.tStartRefresh)
thisExp.addData('instructionstext1.stopped', instructionstext1.tStopRefresh)
# the Routine "Instructions1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_1 = data.TrialHandler(nReps=2, method='random',
                             extraInfo=expInfo, originPath=-1,
                             trialList=data.importConditions(
                                 'conditions_trail1.xlsx'),
                             seed=None, name='trials_1')
thisExp.addLoop(trials_1)  # add the loop to the experiment
# so we can initialise stimuli with some values
thisTrial_1 = trials_1.trialList[0]
# abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
if thisTrial_1 != None:
    for paramName in thisTrial_1:
        exec('{} = thisTrial_1[paramName]'.format(paramName))

for thisTrial_1 in trials_1:
    currentLoop = trials_1
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
    if thisTrial_1 != None:
        for paramName in thisTrial_1:
            exec('{} = thisTrial_1[paramName]'.format(paramName))

    # ------Prepare to start Routine "trail1"-------
    continueRoutine = True
    # update component parameters for each repeat
    target1.setColor(color, colorSpace='rgb')
    target1.setText(word
                    )
    response1.keys = []
    response1.rt = []
    _response1_allKeys = []
    # keep track of which components have finished
    trail1Components = [target1, response1]
    for thisComponent in trail1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trail1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "trail1"-------
    while continueRoutine:
        # get current time
        t = trail1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trail1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        # number of completed frames (so 0 is the first frame)
        frameN = frameN + 1
        # update/draw components on each frame

        # *target1* updates
        if target1.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            target1.frameNStart = frameN  # exact frame index
            target1.tStart = t  # local t and not account for scr refresh
            target1.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(target1, 'tStartRefresh')
            target1.setAutoDraw(True)
        if target1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target1.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                target1.tStop = t  # not accounting for scr refresh
                target1.frameNStop = frameN  # exact frame index
                # time at next scr refresh
                win.timeOnFlip(target1, 'tStopRefresh')
                target1.setAutoDraw(False)

        # *response1* updates
        waitOnFlip = False
        if response1.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            response1.frameNStart = frameN  # exact frame index
            response1.tStart = t  # local t and not account for scr refresh
            response1.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(response1, 'tStartRefresh')
            response1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response1.clock.reset)  # t=0 on next screen flip
            # clear events on next screen flip
            win.callOnFlip(response1.clearEvents, eventType='keyboard')
        if response1.status == STARTED and not waitOnFlip:
            theseKeys = response1.getKeys(
                keyList=['left', 'right', 'down'], waitRelease=False)
            _response1_allKeys.extend(theseKeys)
            if len(_response1_allKeys):
                # just the last key pressed
                response1.keys = _response1_allKeys[-1].name
                response1.rt = _response1_allKeys[-1].rt
                # was this correct?
                if (response1.keys == str(corans)) or (response1.keys == corans):
                    response1.corr = 1
                else:
                    response1.corr = 0
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trail1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trail1"-------
    for thisComponent in trail1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_1.addData('target1.started', target1.tStartRefresh)
    trials_1.addData('target1.stopped', target1.tStopRefresh)
    # check responses
    if response1.keys in ['', [], None]:  # No response was made
        response1.keys = None
        # was no response the correct answer?!
        if str(corans).lower() == 'none':
            response1.corr = 1  # correct non-response
        else:
            response1.corr = 0  # failed to respond (incorrectly)
    # store data for trials_1 (TrialHandler)
    trials_1.addData('response1.keys', response1.keys)
    trials_1.addData('response1.corr', response1.corr)
    if response1.keys != None:  # we had a response
        trials_1.addData('response1.rt', response1.rt)
    trials_1.addData('response1.started', response1.tStartRefresh)
    trials_1.addData('response1.stopped', response1.tStopRefresh)
    # the Routine "trail1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()

###################### End of task 1 ###############################################################


###################### start of task 2 ###############################################################
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
Instructions2Components = [Instructiontext2, key_resp_2]
for thisComponent in Instructions2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
# t0 is time of first possible flip
Instructions2Clock.reset(-_timeToFirstFrame)
frameN = -1

# -------Run Routine "Instructions2"-------
while continueRoutine:
    # get current time
    t = Instructions2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instructions2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *Instructiontext2* updates
    if Instructiontext2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructiontext2.frameNStart = frameN  # exact frame index
        Instructiontext2.tStart = t  # local t and not account for scr refresh
        Instructiontext2.tStartRefresh = tThisFlipGlobal  # on global time
        # time at next scr refresh
        win.timeOnFlip(Instructiontext2, 'tStartRefresh')
        Instructiontext2.setAutoDraw(True)

    # *key_resp_2* updates
    if key_resp_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        key_resp_2.clock.reset()  # now t=0
        key_resp_2.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = key_resp_2.getKeys(keyList=None, waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            # just the last key pressed
            key_resp_2.keys = _key_resp_2_allKeys[-1].name
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions2"-------
for thisComponent in Instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instructiontext2.started', Instructiontext2.tStartRefresh)
thisExp.addData('Instructiontext2.stopped', Instructiontext2.tStopRefresh)
# the Routine "Instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=2, method='random',
                             extraInfo=expInfo, originPath=-1,
                             trialList=data.importConditions(
                                 'conditions_trail2.xlsx'),
                             seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
# so we can initialise stimuli with some values
thisTrial_2 = trials_2.trialList[0]
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))

    # ------Prepare to start Routine "trial2"-------
    continueRoutine = True
    # update component parameters for each repeat
    target2.setColor(color, colorSpace='rgb')
    target2.setText(word)
    response2.keys = []
    response2.rt = []
    _response2_allKeys = []
    # keep track of which components have finished
    trial2Components = [target2, response2]
    for thisComponent in trial2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "trial2"-------
    while continueRoutine:
        # get current time
        t = trial2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        # number of completed frames (so 0 is the first frame)
        frameN = frameN + 1
        # update/draw components on each frame

        # *target2* updates
        if target2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            target2.frameNStart = frameN  # exact frame index
            target2.tStart = t  # local t and not account for scr refresh
            target2.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(target2, 'tStartRefresh')
            target2.setAutoDraw(True)
        if target2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target2.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                target2.tStop = t  # not accounting for scr refresh
                target2.frameNStop = frameN  # exact frame index
                # time at next scr refresh
                win.timeOnFlip(target2, 'tStopRefresh')
                target2.setAutoDraw(False)

        # *response2* updates
        waitOnFlip = False
        if response2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            response2.frameNStart = frameN  # exact frame index
            response2.tStart = t  # local t and not account for scr refresh
            response2.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(response2, 'tStartRefresh')
            response2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response2.clock.reset)  # t=0 on next screen flip
            # clear events on next screen flip
            win.callOnFlip(response2.clearEvents, eventType='keyboard')
        if response2.status == STARTED and not waitOnFlip:
            theseKeys = response2.getKeys(
                keyList=['left', 'right', 'down'], waitRelease=False)
            _response2_allKeys.extend(theseKeys)
            if len(_response2_allKeys):
                # just the last key pressed
                response2.keys = _response2_allKeys[-1].name
                response2.rt = _response2_allKeys[-1].rt
                # was this correct?
                if (response2.keys == str(corans)) or (response2.keys == corans):
                    response2.corr = 1
                else:
                    response2.corr = 0
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial2"-------
    for thisComponent in trial2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('target2.started', target2.tStartRefresh)
    trials_2.addData('target2.stopped', target2.tStopRefresh)
    # check responses
    if response2.keys in ['', [], None]:  # No response was made
        response2.keys = None
        # was no response the correct answer?!
        if str(corans).lower() == 'none':
            response2.corr = 1  # correct non-response
        else:
            response2.corr = 0  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('response2.keys', response2.keys)
    trials_2.addData('response2.corr', response2.corr)
    if response2.keys != None:  # we had a response
        trials_2.addData('response2.rt', response2.rt)
    trials_2.addData('response2.started', response2.tStartRefresh)
    trials_2.addData('response2.stopped', response2.tStopRefresh)
    # the Routine "trial2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()

###################### End of task 2 ###############################################################


###################### Start of task 3 ###############################################################
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
Instructions3Components = [instructiontext3, key_resp_3]
for thisComponent in Instructions3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
# t0 is time of first possible flip
Instructions3Clock.reset(-_timeToFirstFrame)
frameN = -1

# -------Run Routine "Instructions3"-------
while continueRoutine:
    # get current time
    t = Instructions3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instructions3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *instructiontext3* updates
    if instructiontext3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructiontext3.frameNStart = frameN  # exact frame index
        instructiontext3.tStart = t  # local t and not account for scr refresh
        instructiontext3.tStartRefresh = tThisFlipGlobal  # on global time
        # time at next scr refresh
        win.timeOnFlip(instructiontext3, 'tStartRefresh')
        instructiontext3.setAutoDraw(True)

    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        # clear events on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=None, waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            # just the last key pressed
            key_resp_3.keys = _key_resp_3_allKeys[-1].name
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions3"-------
for thisComponent in Instructions3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructiontext3.started', instructiontext3.tStartRefresh)
thisExp.addData('instructiontext3.stopped', instructiontext3.tStopRefresh)
# the Routine "Instructions3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='random',
                             extraInfo=expInfo, originPath=-1,
                             trialList=data.importConditions(
                                 'conditions_trail3.xlsx'),
                             seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
# so we can initialise stimuli with some values
thisTrial_3 = trials_3.trialList[0]
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))

    # ------Prepare to start Routine "trial3"-------
    continueRoutine = True
    # update component parameters for each repeat
    target3.setColor(color, colorSpace='rgb')
    target3.setText(word)
    response3.keys = []
    response3.rt = []
    _response3_allKeys = []
    polygon.setFillColor(polycolor)
    # keep track of which components have finished
    trial3Components = [target3, response3, polygon]
    for thisComponent in trial3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "trial3"-------
    while continueRoutine:
        # get current time
        t = trial3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        # number of completed frames (so 0 is the first frame)
        frameN = frameN + 1
        # update/draw components on each frame

        # *target3* updates
        if target3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            target3.frameNStart = frameN  # exact frame index
            target3.tStart = t  # local t and not account for scr refresh
            target3.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(target3, 'tStartRefresh')
            target3.setAutoDraw(True)
        if target3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target3.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                target3.tStop = t  # not accounting for scr refresh
                target3.frameNStop = frameN  # exact frame index
                # time at next scr refresh
                win.timeOnFlip(target3, 'tStopRefresh')
                target3.setAutoDraw(False)

        # *response3* updates
        waitOnFlip = False
        if response3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            response3.frameNStart = frameN  # exact frame index
            response3.tStart = t  # local t and not account for scr refresh
            response3.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(response3, 'tStartRefresh')
            response3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response3.clock.reset)  # t=0 on next screen flip
            # clear events on next screen flip
            win.callOnFlip(response3.clearEvents, eventType='keyboard')
        if response3.status == STARTED and not waitOnFlip:
            theseKeys = response3.getKeys(
                keyList=['left', 'right', 'down'], waitRelease=False)
            _response3_allKeys.extend(theseKeys)
            if len(_response3_allKeys):
                # just the last key pressed
                response3.keys = _response3_allKeys[-1].name
                response3.rt = _response3_allKeys[-1].rt
                # was this correct?
                if (response3.keys == str(corans)) or (response3.keys == corans):
                    response3.corr = 1
                else:
                    response3.corr = 0
                # a response ends the routine
                continueRoutine = False

        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(polygon, 'tStartRefresh')
            polygon.setAutoDraw(True)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial3"-------
    for thisComponent in trial3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('target3.started', target3.tStartRefresh)
    trials_3.addData('target3.stopped', target3.tStopRefresh)
    # check responses
    if response3.keys in ['', [], None]:  # No response was made
        response3.keys = None
        # was no response the correct answer?!
        if str(corans).lower() == 'none':
            response3.corr = 1  # correct non-response
        else:
            response3.corr = 0  # failed to respond (incorrectly)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('response3.keys', response3.keys)
    trials_3.addData('response3.corr', response3.corr)
    if response3.keys != None:  # we had a response
        trials_3.addData('response3.rt', response3.rt)
    trials_3.addData('response3.started', response3.tStartRefresh)
    trials_3.addData('response3.stopped', response3.tStopRefresh)
    trials_3.addData('polygon.started', polygon.tStartRefresh)
    trials_3.addData('polygon.stopped', polygon.tStopRefresh)
    # the Routine "trial3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()

###################### End of task 3 ###############################################################
