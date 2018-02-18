#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 14:52:47 2017

@author: cammilligan
"""

from TwitterFollowBot import TwitterBot

my_bot = TwitterBot('*')
my_bot.sync_follows()
#my_bot.auto_follow("#machinelearning")

