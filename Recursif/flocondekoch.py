import turtle as tl


def courbe(n,cote) :
	if n==0 :
		tl.forward(cote)
	else :
		courbe(n-1,cote/3)
		tl.left(60)
		courbe(n-1,cote/3)
		tl.left(-120)
		courbe(n-1,cote/3)
		tl.left(60)
		courbe(n-1,cote/3)


def flocon(n, cote) :
	for _ in range(3) :
		courbe(n,cote)
		tl.left(-120)

tl.setheading(0)
tl.hideturtle()
tl.speed(0)
tl.color('green')
flocon(n=4, cote=500)
tl.exitonclick()