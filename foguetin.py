from graphics import *
import random

def meteoro(met,Jogo):
		meteorin = Image(Point(random.randrange(100,900),-random.randrange(10,500)),met)
		meteorin.draw(Jogo)
		return meteorin

def listaMeteoro(listaArquivo,Jogo):
	lista=[]
	for arq in listaArquivo:
		m=meteoro(arq,Jogo)
		lista.append(m)
	return lista

def colidiu(x_min, y_min, x_max, y_max, p1, p2):
	return (p1.getX() <= x_max) and (x_min <= p2.getX()) and \
	(p1.getY() <= y_max) and (y_min <= p2.getY())

def colisaoFogMet(foguetin,meteoros):

	x_min_fog = foguetin.getAnchor().getX() - foguetin.getWidth()  // 2
	y_min_fog = foguetin.getAnchor().getY() - foguetin.getHeight() // 2

	x_max_fog = foguetin.getAnchor().getX() + foguetin.getWidth()  // 2
	y_max_fog = foguetin.getAnchor().getY() + foguetin.getHeight() // 2
#lista
	for m in meteoros:
		xminM = m.getAnchor().getX() - m.getWidth()  // 2
		yminM = m.getAnchor().getY() - m.getHeight()  // 2
		xmaxM = m.getAnchor().getX() + m.getWidth()  // 2
		ymaxM = m.getAnchor().getY() + m.getHeight()  // 2
		if colidiu(x_min_fog, y_min_fog, x_max_fog, y_max_fog, Point(xminM,yminM),Point(xmaxM,ymaxM)):
			return True
	return False

def Game_Over(Jogo, larJan, altJan):
	TelaGameOver=Image(Point(larJan / 2, altJan / 2), 'game_over.png')
	TelaGameOver.draw(Jogo)

def reiniciar(Jogo):
	foguetin()

def fechar(Jogo):
	Jogo.close()

def foguetin():
	a=int(input("Digite qual foguete deseja, 1,2 ou 3: "))
	#cria a janela
	larJan=1000
	altJan=1000
	#cria o foguete
	Jogo= GraphWin('jogo do foguetin', larJan, altJan, autoflush=False)
	Espaço= Image(Point(larJan/2,altJan/2),'espaço.png')
	Continuação_do_Espaço=Image(Point(larJan/2,-500),'espaço(1).png')
	foguetin1= Image(Point(larJan/2,900),'foguetin1.png')
	foguetin2= Image(Point(larJan/2,900),'foguetin2.png')
	foguetin3= Image(Point(larJan/2,900),'foguetin3.png')

	listaMeteoros=['meteoro1.png','meteoro2.png','meteoro3.png','meteoro4.png','meteoro5.png','meteoro6.png', \
		'meteoro7.png','meteoro8.png','meteoro9.png','meteoro10.png']


	if a==1:
		foguetin=foguetin1
	elif a==2:
		foguetin=foguetin2
	elif a==3:
		foguetin=foguetin3


	Espaço.draw(Jogo)
	Continuação_do_Espaço.draw(Jogo)
	foguetin.draw(Jogo)
	
	meteoros = listaMeteoro(listaMeteoros,Jogo)
	velx=[]
	vely=[]
	for m in range(len(meteoros)):
			velx.append(random.randrange(-2,3))
			vely.append(random.randrange(2,4))

	
	#Pra repetir infinitamente
	cc =0
	fim = False
	while not fim:


	
		#Para deixar o espaço infinito
		centroEspaço=Espaço.getAnchor().getY()
		centroContinuação_do_Espaço=Continuação_do_Espaço.getAnchor().getY()
		Espaço.move(0,5)
		Continuação_do_Espaço.move(0,5)
		if centroEspaço >= 1500:
			Espaço.move(0,-2000)
		if centroContinuação_do_Espaço >= 1500:
			Continuação_do_Espaço.move(0,-2000)
		

		#Para o foguete não sair da tela
		Xcentrofoguetin=foguetin.getAnchor().getX()
		Ycentrofoguetin=foguetin.getAnchor().getY()
		if Xcentrofoguetin>1000:
			foguetin.move(-1000,0)
		if Xcentrofoguetin<0:
			foguetin.move(1000,0)
		if Ycentrofoguetin<0:
			foguetin.move(0,1000)
		if Ycentrofoguetin>1000:
			foguetin.move(0,-1000)

		# Pega nova posição do foguete
		key = Jogo.checkKey()
		centrofoguetin=foguetin.getAnchor()

		if key == "Right":
			# Move o foguete
			foguetin.move(35,0)
			# Pega nova posição do foguete
			centrofoguetin=foguetin.getAnchor()
		elif key == "Left":
			foguetin.move(-35,0)
			centrofoguetin=foguetin.getAnchor()
		elif key == "Up":
			foguetin.move(0,-35)
			centrofoguetin=foguetin.getAnchor()
		elif key == "Down":
			foguetin.move(0,35)
			centrofoguetin=foguetin.getAnchor()

		if key=='r':
			Jogo.close()
			reiniciar(Jogo)

		if key=='x':
			fechar(Jogo)

		for m in meteoros:
			if m.getAnchor().getY() > 1000:
				xx=m.getAnchor().getX()
				yy=m.getAnchor().getY()

				dx=random.randrange(200,700)-xx
				dy=-200-yy
				m.move(dx,dy)

				velx[meteoros.index(m)]=random.randrange(-2,3)
				vely[meteoros.index(m)]=random.randrange(2,5)

			else:
				vx=velx[meteoros.index(m)]
				vy=vely[meteoros.index(m)]
				m.move(vx,vy)

		if colisaoFogMet(foguetin,meteoros) == True:
			foguetin.undraw()
			cc = cc + 1
			print(cc)
			fim = True
			
	Game_Over(Jogo, larJan, altJan)

	Jogo.getMouse()
	Jogo.close()

foguetin()
#pngwing: site de achar "png"
#site pra brincar com imagens: iloveimg