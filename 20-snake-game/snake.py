from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x = 0
        y = 0
        for _ in range(3):
            self.add_segment(x, y)
            x -= MOVE_DISTANCE

    def add_segment(self, curr_x, curr_y):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(curr_x, curr_y)
        self.segments.append(new_segment)

    def extend(self):
        new_x = self.segments[len(self.segments) - 1].xcor() - MOVE_DISTANCE
        new_y = self.segments[len(self.segments) - 1].ycor()
        self.add_segment(new_x, new_y)

    def move(self):
        # move to the last segment 3 --> 2, 2 --> 1 etc.
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        # Move the first segment
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
