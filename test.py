import stddrawpygame
import pygame

#-------------------------------------------
# testing client
stddrawpygame.createWindow()
stddrawpygame.setFontFamily("calibri")
stddrawpygame.setFontSize(20)

stddrawpygame._pixel(0.5, 0.5)
stddrawpygame.circle(0.5, 0.5, 0.25)
stddrawpygame.square(0.5, 0.5, 0.5)
stddrawpygame.rectangle(0.3, 0.2, 0.2, 0.2)

stddrawpygame.text(0.75, 0.75, "hello my name is kuni")

stddrawpygame.save()
while True:
	stddrawpygame.show()


