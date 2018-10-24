__author__ = 'rwilbur
#TODO: 
#add a save function, maybe just write level and points and upgrades to a file
#add it so if you go off the screen it will bring you back to the middle
#cleanup file structure (done-ish)


import turtle
import random
import time
import math
def moveforward():
  global speed
  user.forward(speed)
  return
def moveback():
  global speed
  user.forward(-speed)
  return
def turnleft():
  global speed
  user.left(speed)
  return
def turnright():
  global speed
  user.right(speed)
  return
def sidestep_left():
    global speed
    bearing = user.heading()
    rads_bearing = (math.pi)*bearing / 180
    a = rads_bearing + (math.pi)/2
    xmove = speed*math.cos(a) + user.xcor()
    ymove = speed*math.sin(a) + user.ycor()
    user.goto(xmove,ymove)
    return
def sidestep_right():
    global speed
    bearing = user.heading()
    rads_bearing = (math.pi)*bearing / 180
    a = rads_bearing - (math.pi)/2
    xmove = speed*math.cos(a) + user.xcor()
    ymove = speed*math.sin(a) + user.ycor()
    user.goto(xmove,ymove)
    return
def user_attack():
    global attack
    global speed
    global turtle_count
    global turtle_list
    global user
    global heath
    global strength
    global heathBoss
    global ranStr1
    global ranStr2
    global shield
    if attack ==0:
        user.shape(userAttack)
        speed = speed-10
        attack = 1
        shield = 0
    else:
        user.shape(userImage)
        speed = speed+10
        attack = 0
    if attack == 1:
        i = 0
        while len(turtle_list) > i:
            d = ((user.xcor()-turtle_list[i].xcor())**2 + (user.ycor()- turtle_list[i].ycor())**2)**0.5
            if d < 48:
                strength = random.randint(ranStr1,ranStr2)
                heath= heath-strength
                user.shape(userImage)
                speed = speed
                attack = speed+10
                enemyHeathTurt.clear()
                enemyHeathTurt.write(heath, font=('Times New Roman', 20, 'normal'))

            i+=1
    if attack == 1:
        d = ((user.xcor()-bossTurt.xcor())**2 + (user.ycor()- bossTurt.ycor())**2)**0.5
        if d < 76:
            strength = random.randint(ranStr1,ranStr2)
            heathBoss = heathBoss - strength
            enemyHeathTurt.clear()
            enemyHeathTurt.write(heathBoss, font=('Times New Roman', 20, 'normal'))
    return
def user_shield():
    global shield
    global speed
    if shield ==0:
        user.shape(userShield)
        speed = speed-5
        shield = 1
        attack = 0
    else:
        user.shape(userImage)
        speed = speed + 5
        shield = 0
    return
def enemyAttack(turt):
    global shield
    global user
    global mainHeathuser
    global heathUser
    if turt == enemy1turt:
        d = ((user.xcor()-enemy1turt.xcor())**2 + (user.ycor()- enemy1turt.ycor())**2)**0.5
        enemy1turt.shape(enemy1Attack)
        enemy1turt.shape(enemy1)
        enemy1turt.shape(enemy1Attack)
        if d < 48 and shield == 0:
            heathUser= heathUser-random.randint(10,11)
            enemy1turt.shape(enemy1)
            userHeathTurt.clear()
            userHeathTurt.write(heathUser, font=('Times New Roman', 20, 'normal'))
    if turt == enemy2turt:
        d = ((user.xcor()-enemy2turt.xcor())**2 + (user.ycor()- enemy2turt.ycor())**2)**0.5
        enemy2turt.shape(enemy2Attack)
        enemy2turt.shape(enemy2)
        enemy2turt.shape(enemy2Attack)
        if d < 48 and shield == 0:
            heathUser= heathUser-random.randint(10,12)
            enemy2turt.shape(enemy2)
            userHeathTurt.clear()
            userHeathTurt.write(heathUser, font=('Times New Roman', 20, 'normal'))
    if turt == enemy3turt:
        d = ((user.xcor()-enemy3turt.xcor())**2 + (user.ycor()- enemy3turt.ycor())**2)**0.5
        enemy3turt.shape(enemy3Attack)
        enemy3turt.shape(enemy3)
        enemy3turt.shape(enemy3Attack)
        if d < 48 and shield == 0:
            heathUser=heathUser-random.randint(10,13)
            enemy3turt.shape(enemy3)
            userHeathTurt.clear()
            userHeathTurt.write(heathUser, font=('Times New Roman', 20, 'normal'))
    if turt == enemy2turt:
        d = ((user.xcor()-enemy4turt.xcor())**2 + (user.ycor()- enemy4turt.ycor())**2)**0.5
        enemy4turt.shape(enemy4Attack)
        enemy4turt.shape(enemy4)
        enemy4turt.shape(enemy4Attack)
        if d < 48 and shield == 0:
            heathUser = heathUser-random.randint(10,14)
            enemy4turt.shape(enemy4)
            userHeathTurt.clear()
            userHeathTurt.write(heathUser, font=('Times New Roman', 20, 'normal'))
    if turt == enemy5turt:
        d = ((user.xcor()-enemy5turt.xcor())**2 + (user.ycor()- enemy5turt.ycor())**2)**0.5
        enemy5turt.shape(enemy5Attack)
        enemy5turt.shape(enemy5)
        enemy5turt.shape(enemy5Attack)
        if d < 48 and shield == 0:
            heathUser=heathUser-random.randint(10,15)
            enemy5turt.shape(enemy5)
            userHeathTurt.clear()
            userHeathTurt.write(heathUser, font=('Times New Roman', 20, 'normal'))
    if turt == enemy6turt:
        d = ((user.xcor()-enemy6turt.xcor())**2 + (user.ycor()- enemy6turt.ycor())**2)**0.5
        enemy6turt.shape(enemy6Attack)
        enemy6turt.shape(enemy6)
        enemy6turt.shape(enemy6Attack)
        if d < 48 and shield == 0:
            heathUser= heathUser-random.randint(10,16)
            enemy6turt.shape(enemy6)
            userHeathTurt.clear()
            userHeathTurt.write(heathUser, font=('Times New Roman', 20, 'normal'))
    if turt == enemy7turt:
        d = ((user.xcor()-enemy7turt.xcor())**2 + (user.ycor()- enemy7turt.ycor())**2)**0.5
        enemy7turt.shape(enemy7Attack)
        enemy7turt.shape(enemy7)
        enemy7turt.shape(enemy7Attack)
        if d < 48 and shield == 0:
            heathUser= heathUser-random.randint(10,17)
            enemy7turt.shape(enemy7)
            userHeathTurt.clear()
            userHeathTurt.write(heathUser, font=('Times New Roman', 20, 'normal'))
    if turt == enemy8turt:
        d = ((user.xcor()-enemy8turt.xcor())**2 + (user.ycor()- enemy8turt.ycor())**2)**0.5
        enemy8turt.shape(enemy8Attack)
        enemy8turt.shape(enemy8)
        enemy8turt.shape(enemy8Attack)
        if d < 48 and shield == 0:
            heathUser= heathUser-random.randint(10,17)
            enemy8turt.shape(enemy8)
            userHeathTurt.clear()
            userHeathTurt.write(heathUser, font=('Times New Roman', 20, 'normal'))
    if turt == enemy9turt:
        d = ((user.xcor()-enemy9turt.xcor())**2 + (user.ycor()- enemy9turt.ycor())**2)**0.5
        enemy9turt.shape(enemy9Attack)
        enemy9turt.shape(enemy9)
        enemy9turt.shape(enemy9Attack)
        if d < 48 and shield == 0:
            heathUser= heathUser-random.randint(10,18)
            enemy9turt.shape(enemy9)
            userHeathTurt.clear()
            userHeathTurt.write(heathUser, font=('Times New Roman', 20, 'normal'))

    if turt == bossTurt:
        d = ((user.xcor()-bossTurt.xcor())**2 + (user.ycor()- bossTurt.ycor())**2)**0.5
        bossTurt.shape(bossAttack)
        bossTurt.shape(boss)
        bossTurt.shape(bossAttack)
        if d < 76 and shield == 0:
            heathUser= heathUser-random.randint(18,23)
            bossTurt.shape(boss)
            userHeathTurt.clear()
            userHeathTurt.write(heathUser, font=('Times New Roman', 20, 'normal'))
    return
def mouseclick(x,y):
    global points
    global strength
    global speed
    global mainHeathuser
    global ranStr1
    global ranStr2
    if points > 0:
        if abs(x - jackStrength.xcor()) <= 50 and abs(y - jackStrength.ycor()) <= 50:
            ranStr1 += 2
            ranStr2 += 2
            strength = random.randint(ranStr1,ranStr2)
            points-=1
            pointTurtle.clear()
            pointTurtle.write(points, font=('Times New Roman', 20, 'normal'))
        if abs(x - jackSpeed.xcor()) <= 50 and abs(y - jackSpeed.ycor()) <= 50:
            speed+=5
            points-=1
            pointTurtle.clear()
            pointTurtle.write(points, font=('Times New Roman', 20, 'normal'))
        if abs(x - jackHeath.xcor()) <= 50 and abs(y - jackHeath.ycor()) <= 50:
            mainHeathuser +=10
            points-=1
            pointTurtle.clear()
            pointTurtle.write(points, font=('Times New Roman', 20, 'normal'))
            userHeathTurt.clear()
            userHeathTurt.write(mainHeathuser, font=('Times New Roman', 20, 'normal'))
    elif points == 0:
        if abs(x - jackHeath.xcor()) <= 50 and abs(y - jackHeath.ycor()) <= 50:
            randomWriter.goto(-30,0)
            randomWriter.pendown()
            randomWriter.write('No Points to spend', font=('Times New Roman', 20, 'normal'))
            randomWriter.penup()
            randomWriter.goto(1000,1000)
            randomWriter.clear()
        elif abs(x - jackSpeed.xcor()) <= 50 and abs(y - jackSpeed.ycor()) <= 50:
            randomWriter.goto(-30,0)
            randomWriter.pendown()
            randomWriter.write('No Points to spend', font=('Times New Roman', 20, 'normal'))
            randomWriter.penup()
            randomWriter.goto(1000,1000)
            randomWriter.clear()
        elif abs(x - jackStrength.xcor()) <= 50 and abs(y - jackStrength.ycor()) <= 50:
            randomWriter.goto(-30,0)
            randomWriter.pendown()
            randomWriter.write('No Points to spend', font=('Times New Roman', 20, 'normal'))
            randomWriter.penup()
            randomWriter.goto(1000,1000)
            randomWriter.clear()
    return
def teleBossRoom(t1,t2):
    global bossRoom
    global room
    d = ((t1.xcor() - t2.xcor()) ** 2 + (t1.ycor() - t2.ycor()) ** 2) ** 0.5
    if d <= 50 and room == 0:
        window.bgpic(bossRoom)
        jackHeath.hideturtle()
        jackSpeed.hideturtle()
        jackStrength.hideturtle()
        teleportTurt.hideturtle()
        teleportTurt.goto(-268,-268)
        teleportTurt.showturtle()
        user.hideturtle()
        user.goto(-217,-217)
        user.showturtle()
        bossTurt.goto(200,200)
        enemyHeathTurt.clear()
        enemyHeathTurt.write(heathBoss, font=('Times New Roman', 20, 'normal'))
        bossTurt.showturtle()
        userHeathTurt.clear()
        userHeathTurt.write(mainHeathuser, font=('Times New Roman', 20, 'normal'))
        room = 3
    elif d <= 50 and room == 3:
        windowPic = 'src/room/MainRoom.gif'
        window.bgpic(windowPic)
        jackHeath.showturtle()
        jackSpeed.showturtle()
        jackStrength.showturtle()
        teleportTurt.hideturtle()
        teleportTurt.goto(268,268)
        teleportTurt.showturtle()
        user.hideturtle()
        user.goto(217,217)
        user.showturtle()
        bossTurt.hideturtle()
        bossTurt.goto(1000,1000)
        enemyHeathTurt.clear()
        enemyHeathTurt.write(heath, font=('Times New Roman', 20, 'normal'))
        room = 0
    return
windowPic = 'src/TittleScreen.gif'
room = 0
#MainRoom = 0
#TopRoom = 1
#RightRoom = 2
#boss room = 3
window = turtle.Screen()
turtle.setup(800,700)
window.bgpic(windowPic)
window.title('Elite Combat')

attack = 0
shield = 0
speed = 20
ranStr1 = 5
ranStr2 = 10
strength = random.randint(ranStr1,ranStr2)


userImage = ('src/User.gif')
userAttack = ('src/UserAttack.gif')
userShield = ('src/UserShield.gif')

strengthUpgrade = ('src/strength.gif')
speedUpgrade = ('src/speed.gif')
healthUpgrade = ('src/health.gif')

window.addshape(strengthUpgrade)
window.addshape(speedUpgrade)
window.addshape(healthUpgrade)

boss = ('src/enemy/Boss.gif')
bossAttack = ('src/enemy/BossAttack.gif')
bossRoom = ('src/room/BossRoom.gif')
enemy1 = ('src/enemy/Enemy1.gif')
enemy2 = ('src/enemy/Enemy2.gif')
enemy3 = ('src/enemy/Enemy3.gif')
enemy4 = ('src/enemy/Enemy4.gif')
enemy5 = ('src/enemy/Enemy5.gif')
enemy6 = ('src/enemy/Enemy6.gif')
enemy7 = ('src/enemy/Enemy7.gif')
enemy8 = ('src/enemy/Enemy8.gif')
enemy9 = ('src/enemy/Enemy9.gif')


enemy1Attack = ('src/enemy/Enemy11.gif')
enemy2Attack = ('src/enemy/Enemy22.gif')
enemy3Attack = ('src/enemy/Enemy33.gif')
enemy4Attack = ('src/enemy/Enemy44.gif')
enemy5Attack = ('src/enemy/Enemy55.gif')
enemy6Attack = ('src/enemy/Enemy66.gif')
enemy7Attack = ('src/enemy/Enemy77.gif')
enemy8Attack = ('src/enemy/Enemy88.gif')
enemy9Attack = ('src/enemy/Enemy99.gif')

window.addshape(boss)
window.addshape(bossAttack)
window.addshape(bossRoom)
window.addshape(enemy1)
window.addshape(enemy2)
window.addshape(enemy3)
window.addshape(enemy4)
window.addshape(enemy5)
window.addshape(enemy6)
window.addshape(enemy7)
window.addshape(enemy8)
window.addshape(enemy9)
window.addshape(enemy1Attack)
window.addshape(enemy2Attack)
window.addshape(enemy3Attack)
window.addshape(enemy4Attack)
window.addshape(enemy5Attack)
window.addshape(enemy6Attack)
window.addshape(enemy7Attack)
window.addshape(enemy8Attack)
window.addshape(enemy9Attack)

window.addshape(userImage)
window.addshape(userAttack)
window.addshape(userShield)


user = turtle.Turtle()
user.penup()
user.turtlesize(3,3)
user.shape(userImage)
user.hideturtle()

turtle_count = 1
turtle_list = []
stageCount = 1

heath = 100

time.sleep(2)
instructions = ('src/Instructions.gif')
window.bgpic(instructions)



enemy1turt = turtle.Turtle()
enemy1turt.penup()
enemy1turt.shape(enemy1)
enemy1turt.hideturtle()
enemy1turt.goto(2000,2000)
turtle_list.append(enemy1turt)


enemy2turt = turtle.Turtle()
enemy2turt.penup()
enemy2turt.shape(enemy2)
enemy2turt.hideturtle()
enemy2turt.goto(2000,2000)
turtle_list.append(enemy2turt)

enemy3turt = turtle.Turtle()
enemy3turt.penup()
enemy3turt.shape(enemy3)
enemy3turt.hideturtle()
enemy3turt.goto(2000,2000)
turtle_list.append(enemy3turt)

enemy4turt = turtle.Turtle()
enemy4turt.penup()
enemy4turt.shape(enemy4)
enemy4turt.hideturtle()
enemy4turt.goto(2000,2000)
turtle_list.append(enemy4turt)

enemy5turt = turtle.Turtle()
enemy5turt.penup()
enemy5turt.shape(enemy5)
enemy5turt.hideturtle()
enemy5turt.goto(2000,2000)
turtle_list.append(enemy5turt)

enemy6turt = turtle.Turtle()
enemy6turt.penup()
enemy6turt.shape(enemy6)
enemy6turt.hideturtle()
enemy6turt.goto(2000,2000)
turtle_list.append(enemy6turt)

enemy7turt = turtle.Turtle()
enemy7turt.penup()
enemy7turt.shape(enemy7)
enemy7turt.hideturtle()
enemy7turt.goto(2000,2000)
turtle_list.append(enemy7turt)

enemy8turt = turtle.Turtle()
enemy8turt.penup()
enemy8turt.shape(enemy8)
enemy8turt.hideturtle()
enemy8turt.goto(2000,2000)
turtle_list.append(enemy8turt)

enemy9turt = turtle.Turtle()
enemy9turt.penup()
enemy9turt.shape(enemy9)
enemy9turt.hideturtle()
enemy9turt.goto(2000,2000)
turtle_list.append(enemy9turt)

bossTurt = turtle.Turtle()
bossTurt.penup()
bossTurt.shape(boss)
bossTurt.hideturtle()
bossTurt.goto(1000,1000)
heathBoss = 500

enemyHeathTurt = turtle.Turtle()
enemyHeathTurt.penup()
enemyHeathTurt.hideturtle()

userHeathTurt = turtle.Turtle()
userHeathTurt.penup()
userHeathTurt.hideturtle()
heathUser = 100
mainHeathuser = 100
line = turtle.Turtle()
line.hideturtle()

jackStrength = turtle.Turtle()
jackSpeed = turtle.Turtle()
jackHeath =turtle.Turtle()
jackStrength.shape(strengthUpgrade)
jackSpeed.shape(speedUpgrade)
jackHeath.shape(healthUpgrade)
jackStrength.hideturtle()
jackHeath.hideturtle()
jackSpeed.hideturtle()
jackStrength.penup()
jackSpeed.penup()
jackHeath.penup()
jackStrength.goto(-318,268)
jackSpeed.goto(-318,0)
jackHeath.goto(-318,-268)
jackStrength.showturtle()
jackSpeed.showturtle()
jackHeath.showturtle()

window.listen()
window.onkey(moveforward,'Right')
window.onkey(moveback,'Left')
window.onkey(sidestep_left,'Up')
window.onkey(sidestep_right,'Down')
window.onkey(user_attack,'z')
window.onkey(user_shield,'x')
window.onclick(mouseclick)
#window.onclick(teleBossRoom)

line.pencolor('white')
line.penup()
line.goto(-390,300)
line.pendown()
line.write('User Health:', font=('Times New Roman', 20, 'normal'))

line.pencolor('red')
line.penup()
line.goto(-390,-310)
line.pendown()
line.write('Enemy Health:', font=('Times New Roman', 20, 'normal'))

userHeathTurt.goto(-250,300)
userHeathTurt.pendown()
userHeathTurt.pencolor('white')
userHeathTurt.write(mainHeathuser, font=('Times New Roman', 20, 'normal'))

enemyHeathTurt.goto(-225,-310)
enemyHeathTurt.pendown()
enemyHeathTurt.pencolor('red')
enemyHeathTurt.write(heath, font=('Times New Roman', 20, 'normal'))

teleportTurt = turtle.Turtle()
teleportTurt.shape('square')
teleportTurt.pencolor('red')
teleportTurt.penup()
teleportTurt.hideturtle()
teleportTurt.goto(268,268)
teleportTurt.showturtle()
teleportTurt.turtlesize(5,5)

randomWriter = turtle.Turtle()
randomWriter.hideturtle()
randomWriter.penup()
randomWriter.pencolor('red')

line.penup()
line.pencolor('white')
line.goto(205,-300)
line.write('Points:', font=('Times New Roman', 20, 'normal'))
points = 3
pointTurtle = turtle.Turtle()
pointTurtle.penup()
pointTurtle.hideturtle()
pointTurtle.goto(300,-300)
pointTurtle.pendown()
pointTurtle.pencolor('white')
pointTurtle.write(points, font=('Times New Roman', 20, 'normal'))

windowPic = 'src/room/MainRoom.gif'
window.bgpic('src/room/MainRoom.gif')
user.showturtle()
turtInRoom = 1
T = 1
gameOn = True
attackVariable = 3
num = 5
while gameOn == True:
    user.forward(.0001)
    randomAttack = random.randint(0, attackVariable)
    randomBossAttack = random.randint(1,3)
    if room == 0 or room == 3:
        teleBossRoom(user,teleportTurt)
    userX = user.xcor()
    userY = user.ycor()
    if randomAttack == 1 or randomAttack == 0:
        enemyAttack(enemy1turt)
        enemyAttack(enemy2turt)
        enemyAttack(enemy3turt)
        enemyAttack(enemy4turt)
        enemyAttack(enemy5turt)
        enemyAttack(enemy6turt)
        enemyAttack(enemy7turt)
        enemyAttack(enemy8turt)
        enemyAttack(enemy9turt)
    if room == 3:
        if randomBossAttack == 1:
            enemyAttack(bossTurt)
        userX = user.xcor()
        userY = user.ycor()
        bossTurt.goto(userX/num,userY/num)
        if num > 0:
            num-=1
        if num == 1:
            enemyAttack(bossTurt)
        if num == 0:
            num = 5

    #main to top
    if userY > 398 and userX > -200 and userX < 200 and room == 0:
        windowPic = 'src/room/TopRoom.gif'
        window.bgpic(windowPic)
        user.hideturtle()
        user.goto(userX,-395)
        user.showturtle()
        room = 1
        jackHeath.hideturtle()
        jackSpeed.hideturtle()
        jackStrength.hideturtle()
        teleportTurt.hideturtle()
        teleportTurt.goto(1000,1000)
    #main to right
    if userX > 398 and userY > -200 and userY < 200 and room == 0:
        windowPic = 'src/room/RightRoom.gif'
        window.bgpic(windowPic)
        user.hideturtle()
        user.goto(-395,userY)
        user.showturtle()
        room = 2
        jackHeath.hideturtle()
        jackSpeed.hideturtle()
        jackStrength.hideturtle()
        teleportTurt.hideturtle()
        teleportTurt.goto(1000,1000)
    #top to main
    if userY < -398 and userX > -200 and userX < 200 and room == 1:
        windowPic = 'src/room/MainRoom.gif'
        window.bgpic(windowPic)
        user.hideturtle()
        user.goto(userX,395)
        user.showturtle()
        room = 0
        heathUser = mainHeathuser
        userHeathTurt.clear()
        userHeathTurt.write(heathUser, font=('Times New Roman', 20, 'normal'))
        jackHeath.showturtle()
        jackSpeed.showturtle()
        jackStrength.showturtle()
        teleportTurt.goto(268,268)
        teleportTurt.showturtle()
        turtInRoom = 1
    #right to main
    if userX < -398 and userY > -200 and userY < 200 and room == 2:
        windowPic = 'src/room/MainRoom.gif'
        window.bgpic(windowPic)
        user.hideturtle()
        user.goto(395,userY)
        user.showturtle()
        room = 0
        heathUser = mainHeathuser
        userHeathTurt.clear()
        userHeathTurt.write(heathUser, font=('Times New Roman', 20, 'normal'))
        jackHeath.showturtle()
        jackSpeed.showturtle()
        jackStrength.showturtle()
        teleportTurt.goto(268,268)
        teleportTurt.showturtle()
        turtInRoom = 1


    if room == 2 and turtle_count == 1:
        if turtInRoom == 1:
            enemy1turt.goto(200,0)
            enemy1turt.showturtle()
            turtInRoom = 0
        userX = user.xcor()
        userY = user.ycor()
        enemy1turt.goto(userX/num,userY/num)
        if num > 0:
            num-=1
        if num == 0:
            num = 5
        enemyHeathTurt.clear()
        enemyHeathTurt.write(heath, font=('Times New Roman', 20, 'normal'))
    elif room == 1 and turtle_count == 2:
        if T == 1:
            heath = 150
            enemyHeathTurt.clear()
            enemyHeathTurt.write(heath, font=('Times New Roman', 20, 'normal'))
            enemy1turt.goto(0,200)
            enemy1turt.showturtle()
            T=T+1
        userX = user.xcor()
        userY = user.ycor()
        enemy1turt.goto(userX/num,userY/num)
        if num > 0:
            num-=1
        if num == 0:
            num = 5
    else:
        enemy1turt.hideturtle()
        enemy1turt.goto(1000,1000)

    if room == 2 and turtle_count == 3:
        if turtInRoom == 1:
            enemy2turt.goto(200,0)
            enemy2turt.showturtle()
            turtInRoom = 0
        userX = user.xcor()
        userY = user.ycor()
        enemy2turt.goto(userX/num,userY/num)
        if num > 0:
            num-=1
        if num == 0:
            num = 5
        enemyHeathTurt.clear()
        enemyHeathTurt.write(heath, font=('Times New Roman', 20, 'normal'))
    elif room == 1 and turtle_count == 4:
        if T == 2:
            heath = 160
            enemyHeathTurt.clear()
            enemyHeathTurt.write(heath, font=('Times New Roman', 20, 'normal'))
            enemy2turt.goto(0, 200)
            enemy2turt.showturtle()
            T+=1
        userX = user.xcor()
        userY = user.ycor()
        enemy2turt.goto(userX/num,userY/num)
        if num > 0:
            num-=1
        if num == 0:
            num = 5
    else:
        enemy2turt.hideturtle()
        enemy2turt.goto(1000,1000)

    if room == 2 and turtle_count == 5:
        if turtInRoom == 1:
            enemy3turt.goto(200,0)
            enemy3turt.showturtle()
            turtInRoom = 0
        userX = user.xcor()
        userY = user.ycor()
        enemy3turt.goto(userX/num,userY/num)
        if num > 0:
            num-=1
        if num == 0:
            num = 5
        enemyHeathTurt.clear()
        enemyHeathTurt.write(heath, font=('Times New Roman', 20, 'normal'))
    elif room == 1 and turtle_count == 6:
        if T==3:
            heath = 170
            enemyHeathTurt.clear()
            enemyHeathTurt.write(heath, font=('Times New Roman', 20, 'normal'))
            enemy3turt.goto(0, 200)
            enemy3turt.showturtle()
            T+=1
        userX = user.xcor()
        userY = user.ycor()
        enemy3turt.goto(userX/num,userY/num)
        if num > 0:
            num-=1
        if num == 0:
            num = 5
    else:
        enemy3turt.hideturtle()
        enemy3turt.goto(1000,1000)

    if room == 2 and turtle_count == 7:
        if turtInRoom == 1:
            enemy4turt.goto(200,0)
            enemy4turt.showturtle()
            turtInRoom = 0
        userX = user.xcor()
        userY = user.ycor()
        enemy4turt.goto(userX/num,userY/num)
        if num > 0:
            num-=1
        if num == 0:
            num = 5
        enemyHeathTurt.clear()
        enemyHeathTurt.write(heath, font=('Times New Roman', 20, 'normal'))
    elif room == 1 and turtle_count ==8:
        if T ==4:
            heath = 180
            enemy4turt.goto(0, 200)
            enemy4turt.showturtle()
            enemyHeathTurt.clear()
            enemyHeathTurt.write(heath, font=('Times New Roman', 20, 'normal'))
            T+=1
        userX = user.xcor()
        userY = user.ycor()
        enemy4turt.goto(userX/num,userY/num)
        if num > 0:
            num-=1
        if num == 0:
            num = 5
    else:
        enemy4turt.hideturtle()
        enemy4turt.goto(1000, 1000)

    if room == 2 and turtle_count == 9:
        if turtInRoom == 1:
            enemy5turt.goto(200,0)
            enemy5turt.showturtle()
            turtInRoom = 0
        userX = user.xcor()
        userY = user.ycor()
        enemy5turt.goto(userX/num,userY/num)
        if num > 0:
            num-=1
        if num == 0:
            num = 5
        enemyHeathTurt.clear()
        enemyHeathTurt.write(heath, font=('Times New Roman', 20, 'normal'))
    elif room == 1 and turtle_count ==10:
        if T ==5:
            heath = 190
            enemy5turt.goto(0, 200)
            enemy5turt.showturtle()
            enemyHeathTurt.clear()
            enemyHeathTurt.write(heath, font=('Times New Roman', 20, 'normal'))
            T+=1
        userX = user.xcor()
        userY = user.ycor()
        enemy5turt.goto(userX/num,userY/num)
        if num > 0:
            num-=1
        if num == 0:
            num = 5
    else:
        enemy5turt.hideturtle()
        enemy5turt.goto(1000, 1000)

    if room == 2 and turtle_count == 11:
        if turtInRoom == 1:
            enemy6turt.goto(200,0)
            enemy6turt.showturtle()
            turtInRoom = 0
        userX = user.xcor()
        userY = user.ycor()
        enemy6turt.goto(userX/num,userY/num)
        if num > 0:
            num-=1
        if num == 0:
            num = 5
        enemyHeathTurt.clear()
        enemyHeathTurt.write(heath, font=('Times New Roman', 20, 'normal'))
    elif room == 1 and turtle_count == 12:
        if T == 6:
            heath = 200
            enemy6turt.goto(0, 200)
            enemy6turt.showturtle()
            enemyHeathTurt.clear()
            enemyHeathTurt.write(heath, font=('Times New Roman', 20, 'normal'))
            T+=1
        userX = user.xcor()
        userY = user.ycor()
        enemy6turt.goto(userX/num,userY/num)
        if num > 0:
            num-=1
        if num == 0:
            num = 5
    else:
        enemy6turt.hideturtle()
        enemy6turt.goto(1000, 1000)

    if room == 2 and turtle_count == 13:
        if turtInRoom == 1:
            enemy7turt.goto(200,0)
            enemy7turt.showturtle()
            turtInRoom = 0
        userX = user.xcor()
        userY = user.ycor()
        enemy7turt.goto(userX/num,userY/num)
        if num > 0:
            num-=1
        if num == 0:
            num = 5
        enemyHeathTurt.clear()
        enemyHeathTurt.write(heath, font=('Times New Roman', 20, 'normal'))
    elif room == 1 and turtle_count == 14:
        if T == 7:
            heath = 210
            enemy7turt.goto(0, 200)
            enemy7turt.showturtle()
            enemyHeathTurt.clear()
            enemyHeathTurt.write(heath, font=('Times New Roman', 20, 'normal'))
            T+=1
        userX = user.xcor()
        userY = user.ycor()
        enemy7turt.goto(userX/num,userY/num)
        if num > 0:
            num-=1
        if num == 0:
            num = 5
    else:
        enemy7turt.hideturtle()
        enemy7turt.goto(1000, 1000)

    if room == 2 and turtle_count == 15:
        if turtInRoom == 1:
            enemy8turt.goto(200,0)
            enemy8turt.showturtle()
            turtInRoom = 0
        userX = user.xcor()
        userY = user.ycor()
        enemy8turt.goto(userX/num,userY/num)
        if num > 0:
            num-=1
        if num == 0:
            num = 5
        enemyHeathTurt.clear()
        enemyHeathTurt.write(heath, font=('Times New Roman', 20, 'normal'))
    elif room == 1 and turtle_count == 16:
        if T == 8:
            heath = 220
            enemy8turt.goto(0, 200)
            enemy8turt.showturtle()
            enemyHeathTurt.clear()
            enemyHeathTurt.write(heath, font=('Times New Roman', 20, 'normal'))
            T+=1
        userX = user.xcor()
        userY = user.ycor()
        enemy8turt.goto(userX/num,userY/num)
        if num > 0:
            num-=1
        if num == 0:
            num = 5
    else:
        enemy8turt.hideturtle()
        enemy8turt.goto(1000, 1000)

    if room == 2 and turtle_count == 17:
        if turtInRoom == 1:
            enemy9turt.goto(200,0)
            enemy9turt.showturtle()
            turtInRoom = 0
        userX = user.xcor()
        userY = user.ycor()
        enemy9turt.goto(userX/num,userY/num)
        if num > 0:
            num-=1
        if num == 0:
            num = 5
        enemyHeathTurt.clear()
        enemyHeathTurt.write(heath, font=('Times New Roman', 20, 'normal'))
    elif room == 1 and turtle_count ==18:
        if T==9:
            heath = 230
            enemy9turt.goto(0, 200)
            enemy9turt.showturtle()
            enemyHeathTurt.clear()
            enemyHeathTurt.write(heath, font=('Times New Roman', 20, 'normal'))
            T = 1
        userX = user.xcor()
        userY = user.ycor()
        enemy9turt.goto(userX/num,userY/num)
        if num > 0:
            num-=1
        if num == 0:
            num = 5
    else:
        enemy9turt.hideturtle()
        enemy9turt.goto(1000, 1000)


    if attack == 1:
        i = 0
        while len(turtle_list) > i:
            d = ((user.xcor()-turtle_list[i].xcor())**2 + (user.ycor()- turtle_list[i].ycor())**2)**0.5
            if d < 48:
                heath= heath-strength
                user.shape(userImage)
                speed = speed+10
                attack = 0
                enemyHeathTurt.clear()
                enemyHeathTurt.write(heath, font=('Times New Roman', 20, 'normal'))

            i+=1

    if attack == 1:
        d = ((user.xcor()-bossTurt.xcor())**2 + (user.ycor()- bossTurt.ycor())**2)**0.5
        if d < 76:
            heathBoss = heathBoss - strength
            enemyHeathTurt.clear()
            enemyHeathTurt.write(heathBoss, font=('Times New Roman', 20, 'normal'))
            attack = 0

    if heath <= 0:
        heath = 0
        enemyHeathTurt.clear()
        enemyHeathTurt.write(heath, font=('Times New Roman', 20, 'normal'))
        if turtle_count == 1:
            enemy1turt.hideturtle()
            enemy1turt.goto(1000,1000)
            turtle_count = 2
            points+=1
            pointTurtle.clear()
            pointTurtle.write(points, font=('Times New Roman', 20, 'normal'))
            heath = 100
        elif turtle_count == 2:
            enemy1turt.hideturtle()
            enemy1turt.goto(1000,1000)
            turtle_count = 3
            heath = 110
            points+=1
            pointTurtle.clear()
            pointTurtle.write(points, font=('Times New Roman', 20, 'normal'))
        elif turtle_count == 3:
            enemy2turt.hideturtle()
            enemy2turt.goto(1000,1000)
            turtle_count = 4
            heath = 120
            points+=1
            pointTurtle.clear()
            pointTurtle.write(points, font=('Times New Roman', 20, 'normal'))
        elif turtle_count == 4:
            enemy2turt.hideturtle()
            enemy2turt.goto(1000,1000)
            turtle_count = 5
            heath = 120
            points+=1
            pointTurtle.clear()
            pointTurtle.write(points, font=('Times New Roman', 20, 'normal'))
        elif turtle_count == 5:
            enemy3turt.hideturtle()
            enemy3turt.goto(1000,1000)
            turtle_count = 6
            heath = 140
            points+=1
            pointTurtle.clear()
            pointTurtle.write(points, font=('Times New Roman', 20, 'normal'))
        elif turtle_count == 6:
            enemy3turt.hideturtle()
            enemy3turt.goto(1000,1000)
            turtle_count = 7
            heath = 130
            points+=1
            pointTurtle.clear()
            pointTurtle.write(points, font=('Times New Roman', 20, 'normal'))
        elif turtle_count == 7:
            enemy4turt.hideturtle()
            enemy4turt.goto(1000,1000)
            turtle_count = 8
            heath = 160
            points+=1
            pointTurtle.clear()
            pointTurtle.write(points, font=('Times New Roman', 20, 'normal'))
        elif turtle_count == 8:
            enemy4turt.hideturtle()
            enemy4turt.goto(1000,1000)
            turtle_count = 9
            heath = 140
            points+=1
            pointTurtle.clear()
            pointTurtle.write(points, font=('Times New Roman', 20, 'normal'))
        elif turtle_count == 9:
            enemy5turt.hideturtle()
            enemy5turt.goto(1000,1000)
            turtle_count = 10
            heath = 180
            points+=1
            pointTurtle.clear()
            pointTurtle.write(points, font=('Times New Roman', 20, 'normal'))
        elif turtle_count == 10:
            enemy5turt.hideturtle()
            enemy5turt.goto(1000, 1000)
            turtle_count = 11
            heath = 150
            points+=1
            pointTurtle.clear()
            pointTurtle.write(points, font=('Times New Roman', 20, 'normal'))
        elif turtle_count == 11:
            enemy6turt.hideturtle()
            enemy6turt.goto(1000, 1000)
            turtle_count = 12
            heath = 200
            points+=1
            pointTurtle.clear()
            pointTurtle.write(points, font=('Times New Roman', 20, 'normal'))
        elif turtle_count == 12:
            enemy6turt.hideturtle()
            enemy6turt.goto(1000, 1000)
            turtle_count = 13
            heath = 160
            points+=1
            pointTurtle.clear()
            pointTurtle.write(points, font=('Times New Roman', 20, 'normal'))
        elif turtle_count == 13:
            enemy7turt.hideturtle()
            enemy7turt.goto(1000, 1000)
            turtle_count = 14
            heath = 220
            points+=1
            pointTurtle.clear()
            pointTurtle.write(points, font=('Times New Roman', 20, 'normal'))
        elif turtle_count == 14:
            enemy7turt.hideturtle()
            enemy7turt.goto(1000, 1000)
            turtle_count = 15
            heath = 170
            points+=1
            pointTurtle.clear()
            pointTurtle.write(points, font=('Times New Roman', 20, 'normal'))
        elif turtle_count == 15:
            enemy8turt.hideturtle()
            enemy8turt.goto(1000, 1000)
            turtle_count = 16
            heath = 240
            points+=1
            pointTurtle.clear()
            pointTurtle.write(points, font=('Times New Roman', 20, 'normal'))
        elif turtle_count == 16:
            enemy8turt.hideturtle()
            enemy8turt.goto(1000, 1000)
            turtle_count = 17
            heath = 180
            points+=1
            pointTurtle.clear()
            pointTurtle.write(points, font=('Times New Roman', 20, 'normal'))
        elif turtle_count == 17:
            enemy9turt.hideturtle()
            enemy9turt.goto(1000, 1000)
            turtle_count = 18
            heath = 260
            points+=1
            pointTurtle.clear()
            pointTurtle.write(points, font=('Times New Roman', 20, 'normal'))
        elif turtle_count == 18:
            enemy9turt.hideturtle()
            enemy9turt.goto(1000, 1000)
            turtle_count = 1
            heath = 100
            points+=1
            pointTurtle.clear()
            pointTurtle.write(points, font=('Times New Roman', 20, 'normal'))

    if heathBoss <= 0:
        bossTurt.hideturtle()
        line.penup()
        line.goto(0,0)
        line.write('YOU WIN!', font=('Times New Roman', 20, 'normal'))
        time.sleep(2)
        gameOn = False
        window.bye()

    elif heathUser <= 0:
        line.penup()
        line.goto(0,0)
        line.write('You lost.', font=('Times New Roman', 20, 'normal'))
        time.sleep(2)
        gameOn = False
        window.bye()


window.mainloop()
