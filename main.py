import PySimpleGUI as sg

"""
Cria uma GUI para o programa. Por que sim, sabe.
"""

sg.theme('DarkAmber')

layout = [[sg.Text("Col")]]


def intersecta(x1, x2, x3, x4, y1, y2, y3, y4):
	xDistBig = abs(x1 - x4)
	xDist1 = abs(x1 - x2)
	xDist2 = abs(x3 - x4)

	yDistBig = abs(y1 - y4)
	yDist1 = abs(y1 - y2)
	yDist2 = abs(y3 - y4)

	return ((xDist1 + xDist2) > xDistBig) or ((yDist1 + yDist2) > yDistBig) # Se a distância entre o primeiro e o último for menor que o tamanho dos dois lados, há intersecção

