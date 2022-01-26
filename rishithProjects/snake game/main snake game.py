import turtle
import time
import random

score = 0
highscore = 0
delay = 0.1

# window

win = turtle.Screen()
win.title("Snake game")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

# food
food = turtle.Turtle()
food_colors = random.choice(['red', 'green', 'yellow'])
food_shapes = random.choice(['circle', 'triangle', 'classic'])
food.shape(food_shapes)
food.speed(0)
food.color(food_colors)
food.penup()
food.goto(0, 100)

# head

head = turtle.Turtle()
head.shape('square')
head.color('white')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

pen = turtle.Turtle()
pen.speed(0)
pen.shape('classic')
pen.color('white')
pen.up()
pen.hideturtle()
pen.goto(40, 275)
pen.write('score:  highscore: 0', align='left', font=('consolas', 15, 'bold'))


# key directions

def go_up():
    if head.direction != 'down':
        head.direction = 'up'


def go_down():
    if head.direction != 'up':
        head.direction = 'down'


def go_left():
    if head.direction != 'right':
        head.direction = 'left'


def go_right():
    if head.direction != 'left':
        head.direction = 'right'


def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)


win.listen()
win.onkeypress(go_up, 'w')
win.onkeypress(go_down, 's')
win.onkeypress(go_left, 'a')
win.onkeypress(go_right, 'd')

segment = []

# game loop (persistent)
while True:
    win.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'stop'
        food_colors = random.choice(['red', 'green', 'yellow'])
        food_shapes = random.choice(['circle', 'triangle', 'classic'])
        for x in segment:
            x.goto(1000, 1000)
        segment.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write('score: {} highscore: {}'.format(score, highscore), align='left', font=('consolas', 15, 'bold'))
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
        # add segment
        newSegment = turtle.Turtle()
        newSegment.speed(0)
        newSegment.shape('square')
        newSegment.color('orange')
        newSegment.penup()
        segment.append(newSegment)
        delay -= 0.01
        score += 1
        if score > highscore:
            highscore = score
        pen.clear()
        pen.write('score: {} high score: {}'.format(score, highscore), align='left', font=('consolas', 15, 'bold'))
    # check for collisions (b/w head and segments)
    for index in range(len(segment) - 1, 0, -1):
        x = segment[index - 1].xcor()
        y = segment[index - 1].ycor()
        segment[index].goto(x, y)
    if len(segment) > 0:
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x, y)
    move()
    for x in segment:
        if x.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'
            food_colors = random.choice(['red', 'green', 'yellow'])
            food_shapes = random.choice(['circle', 'triangle', 'classic'])
            for x in segment:
                x.goto(1000, 1000)
            x.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write('score: {} highscore: {}'.format(score, highscore), align='left', font=('consolas', 15, 'bold'))
    time.sleep(delay)

win.mainloop()
