#!/usr/bin/env python


import pygame.event
import pygame.key
import pygame.display
import pygame.image
import pygame.mixer
#import pygame.mixer.music
import pygame
import time
import os
import linecache

from pygame.locals import *
if 'trivfilepath' in globals():
	print ("Global variable: 'trivfilepath' detected, loading specified trivia script")
else:
	print ("Global variable: 'trivfilepath' not detected, using default trivia script.")
	trivfilepath = (os.path.join('TRIV', 'sample.triv'))


pygame.display.init()
pygame.font.init()
screensurf=pygame.display.set_mode((640, 480))
pygame.display.set_caption("Doorway Trivia 2", "Doorway Trivia 2")
simplefont = pygame.font.SysFont(None, 16)
simplefontB = pygame.font.SysFont(None, 22)

bg1=pygame.image.load(os.path.join('TEX', 'bg1.png'))
correctpic=pygame.image.load(os.path.join('TEX', 'DOOR_OPEN_HALL.PNG'))
incorrectpic=pygame.image.load(os.path.join('TEX', 'DOOR_OPEN_FALL.PNG'))
correctpicbox = correctpic.get_rect()
correctpicbox.centerx = screensurf.get_rect().centerx
correctpicbox.centery = ((screensurf.get_rect().centery))
incorrectpicbox = incorrectpic.get_rect()
incorrectpicbox.centerx = screensurf.get_rect().centerx
incorrectpicbox.centery = ((screensurf.get_rect().centery))

def inpwait():
	while True:
		time.sleep(.1)
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				return()

def splashtext(texttodraw):
	textit=simplefontB.render(texttodraw, True, (0, 0, 0), (255, 255, 255))
	textbox = textit.get_rect()
	textbox.centerx = screensurf.get_rect().centerx
	textbox.centery = ((screensurf.get_rect().centery + 50))
	screensurf.blit(textit, textbox)
	pygame.display.update()

def splashtextB(texttodraw):
	textit=simplefontB.render(texttodraw, True, (0, 0, 0), (255, 255, 255))
	textbox = textit.get_rect()
	textbox.centerx = screensurf.get_rect().centerx
	textbox.centery = ((screensurf.get_rect().centery + 68))
	screensurf.blit(textit, textbox)
	pygame.display.update()

def correctsplash():
	screensurf.blit(correctpic, correctpicbox)
	splashtext("Correct!")
	pygame.display.update()
	pygame.event.pump()
	pygame.event.clear()
	inpwait()
def incorrectsplash():
	screensurf.blit(incorrectpic, incorrectpicbox)
	splashtext("Incorrect!")
	pygame.display.update()
	pygame.event.pump()
	pygame.event.clear()
	inpwait()
def winsplash():
	#screensurf.blit(correctpic, correctpicbox)
	splashtext("Final Score:")
	splashtextB((str(score) + "/" + str(scoreof)))
	pygame.display.update()
	pygame.event.pump()
	pygame.event.clear()
	inpwait()

screensurf.blit(bg1, (0, 0))
def getinst(linenum):
	linet=str(linecache.getline(trivfilepath, linenum)).replace("\n", "")
	#print ("getinst:\n" + linet)
	return(linet)
linetxt=""
lineno=1
trivauthor="unspecified"
trivmode="1"
trivtitle="unnamed"
score=0
scoreof=0


def iteratelist(listtoiterate):
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
		texhigjump=14
		#menu line count variable. should be set to 1 here.
		indlcnt=1
		for indx in listtoiterate:
			if indlcnt==listhighnum:
				textit=simplefont.render(indx, True, (0, 0, 0), (255, 255, 255))
			else:
				textit=simplefont.render(indx, True, (255, 255, 255), (0, 0, 0))
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
		

def drawqtext(texttodraw):
	textchunk=""
	#print ("receved:" + texttodraw)
	qnum=str(scoreof + 1)
	qnumtxt=("Q" + qnum + ":")
	texstart=12
	texjump=20
	texhigcnt=20
	texttodraw=(qnumtxt + texttodraw + "\n")
	for texch in texttodraw:
		#print texch
		if texch=="\n":
			textit=simplefontB.render(textchunk, True, (0, 0, 0), (226, 208, 190))
			screensurf.blit(textit, (0, texhigcnt))
			texhigcnt += texjump
			textchunk=""
			#print "ping"
		else:
			textchunk=(textchunk + texch)
			#print "pong"
	pygame.display.update()

while linetxt!=":end":
	screensurf.blit(bg1, (0, 0))
	#time.sleep(0.8)
	linetxt=getinst(lineno)
	#print("mainloop")
	sublinetxt=""
	sublinetxtb=""
	if linetxt==':declare-title':
		trivtitle=getinst(lineno + 1)
		pygame.display.set_caption(("Doorway Trivia 2 |" + trivtitle), ("Doorway Trivia 2 |" + trivtitle))
		print("set title to:" + trivtitle)
		lineno += 2
	elif linetxt==':declare-author':
		trivauthor=getinst((lineno + 1))
		print("set author to:" + trivauthor)
		lineno += 2
	elif linetxt==":declare-mode":
		trivmode=getinst((lineno + 1))
		print("set mode to:" + trivmode)
		lineno += 2
	elif linetxt==":multi":
		while linetxt!="::":
			if linetxt==":qtext":
				qtextcont=""
				while linetxt!="::":
					lineno += 1
					linetxt=getinst(lineno)
					if linetxt!="::":
						qtextcont=(qtextcont + "\n" + linetxt)
				#print qtextcont
				drawqtext(qtextcont)
			if linetxt==":list":
				lineno += 1
				linetxt=getinst(lineno)
				qlist=[linetxt]
				while linetxt!="::":
					lineno += 1
					linetxt=getinst(lineno)
					if linetxt!="::":
						qlist.extend([linetxt])
				print qlist
			if linetxt==":awns":
				lineno += 1
				linetxt=getinst(lineno)
				qawns=linetxt
				#print qawns
			lineno += 1
			linetxt=getinst(lineno)
		print "multi"
		lineno += 1
		awnsel=str(iteratelist(qlist))
		if awnsel==qawns:
			score +=1
			scoreof +=1
			print("correct")
			correctsplash()
		else:
			scoreof +=1
			print("incorrect")
			incorrectsplash()
	else:
		print("unkown" + linetxt)
		lineno += 1
winsplash()
print "end"