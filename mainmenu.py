#!/usr/bin/env python
import os
import pygame
import time
from pygame.locals import *
import linecache

mainmenu=("play a trivia game", "help", "about", "quit")

pygame.display.init()
pygame.font.init()
screensurf=pygame.display.set_mode((640, 480))
pygame.display.set_caption("Doorway Trivia 2", "Doorway Trivia 2")
simplefont = pygame.font.SysFont(None, 16)
simplefontB = pygame.font.SysFont(None, 22)
bg3=pygame.image.load(os.path.join('TEX', 'bg3.png'))
titlepic=pygame.image.load(os.path.join('TEX', 'title.png'))
smalltitlepic=pygame.image.load(os.path.join('TEX', 'title-small.png'))
MENUFLG=1
quitflg=0
def iteratelistB(listtoiterate):
	findcnt=0
	for flx in listtoiterate:
		findcnt += 1
	selectmade=0
	listhighnum=1
	
	while selectmade!=1:
		
		if listhighnum<=0:
			listhighnum=findcnt
		elif listhighnum>findcnt:
			listhighnum=1
			
		#starting point for menu
		texhigcnt=350
		#separation between each line of text's origin
		texhigjump=20
		#menu line count variable. should be set to 1 here.
		indlcnt=1
		for indx in listtoiterate:
			if indlcnt==listhighnum:
				textit=simplefontB.render(indx, True, (0, 0, 0), (255, 255, 255))
			else:
				textit=simplefontB.render(indx, True, (255, 255, 255), (0, 0, 0))
			screensurf.blit(textit, (0, texhigcnt))
			texhigcnt += texhigjump
			indlcnt += 1
		pygame.display.update()
		pygame.event.pump()
		pygame.event.clear()
		evhappenflg=0
		while evhappenflg==0:
			time.sleep(.1)
			for event in pygame.event.get():
				if event.type == KEYDOWN and event.key == K_UP:
					listhighnum -= 1
					evhappenflg=1
				if event.type == KEYDOWN and event.key == K_DOWN:
					listhighnum += 1
					evhappenflg=1
				if event.type == KEYDOWN and event.key == K_RETURN:
					ixreturn=1
					evhappenflg=1
					return(listhighnum)

def iteratelistC(listtoiterate):
	findcnt=0
	for flx in listtoiterate:
		findcnt += 1
	selectmade=0
	listhighnum=1
	
	while selectmade!=1:
		
		if listhighnum<=0:
			listhighnum=findcnt
		elif listhighnum>findcnt:
			listhighnum=1
			
		#starting point for menu
		texhigcnt=20
		#separation between each line of text's origin
		texhigjump=20
		#menu line count variable. should be set to 1 here.
		indlcnt=1
		for indx in listtoiterate:
			if indlcnt==listhighnum:
				textit=simplefontB.render(indx, True, (0, 0, 0), (255, 255, 255))
			else:
				textit=simplefontB.render(indx, True, (0, 0, 0), (226, 208, 190))
			screensurf.blit(textit, (200, texhigcnt))
			texhigcnt += texhigjump
			indlcnt += 1
		pygame.display.update()
		pygame.event.pump()
		pygame.event.clear()
		evhappenflg=0
		while evhappenflg==0:
			time.sleep(.1)
			for event in pygame.event.get():
				if event.type == KEYDOWN and event.key == K_UP:
					listhighnum -= 1
					evhappenflg=1
				if event.type == KEYDOWN and event.key == K_DOWN:
					listhighnum += 1
					evhappenflg=1
				if event.type == KEYDOWN and event.key == K_RETURN:
					ixreturn=1
					evhappenflg=1
					return(listhighnum)

def drawsmalltitle():
	screensurf.blit(smalltitlepic, (30, 20))

def inpwait():
	while True:
		time.sleep(.1)
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				return()

def aboutscreen():
	screensurf.blit(bg3, (0, 0))
	drawsmalltitle()
	pixcnt1=20
	pixjmp=14
	abt = open('live-about.txt')
	for fnx in abt:
		fnx=fnx.replace('\n', '')
		abttext=simplefont.render(fnx, True, (0, 0, 0), (226, 208, 190))
		screensurf.blit(abttext, (200, pixcnt1))
		pixcnt1 += pixjmp
	pygame.display.update()
	inpwait()

def helpscreen():
	screensurf.blit(bg3, (0, 0))
	drawsmalltitle()
	pixcnt1=20
	pixjmp=14
	abt = open('live-help.txt')
	for fnx in abt:
		fnx=fnx.replace('\n', '')
		abttext=simplefont.render(fnx, True, (0, 0, 0), (226, 208, 190))
		screensurf.blit(abttext, (200, pixcnt1))
		pixcnt1 += pixjmp
	pygame.display.update()
	inpwait()

while quitflg!=1:
	screensurf.blit(bg3, (0, 0))
	screensurf.blit(titlepic, (200, 80))
	itemsel=iteratelistB(mainmenu)
	if itemsel==1:
		screensurf.blit(bg3, (0, 0))
		drawsmalltitle()
		trivlist=(["cancel"])
		trivfil = open("trivlist.txt")
		for fline in trivfil:
			fline=fline.replace("\n", "")
			#print fline
			trivlist.extend([fline])
		trivnum=iteratelistC(trivlist)
		if trivnum!=1:
			trivcnt=1
			trivfil = open("trivlist.txt")
			for eline in trivfil:
				eline=eline.replace("\n", "")
				trivcnt +=1
				if trivnum==trivcnt:
					trivfilepath=(os.path.join('TRIV', eline))
					execfile('DT2-ENG.py')
					break
	if itemsel==4:
		quitflg=1
	if itemsel==3:
		aboutscreen()
	if itemsel==2:
		helpscreen()
