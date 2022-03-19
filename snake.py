from turtle import Turtle

STARTING_LENGTH = 3
MOVE_DISTANCE = 20
TURTLE_SHAPE = 'square'
TURTLE_COLOR = 'white'

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self, screen):

        self.segments = []  # Snake body
        self.create_snake()
        self.head = self.segments[0]  # Get snake head for reusing later

        # Setup keys to control the snake
        screen.listen()
        screen.onkey(self.up, 'Up')
        screen.onkey(self.down, 'Down')
        screen.onkey(self.right, 'Right')
        screen.onkey(self.left, 'Left')

    def create_snake(self):
        """
        Create a new snake to start the game
        """
        for num in range(STARTING_LENGTH):
            x_cor = - num * 20
            self.add_segment((x_cor, 0))

    def add_segment(self, position):
        """
        Create a segment of the snake body and add it to the whole snake body
        :param position: A tuple (x_cor, y_cor) representing the position of the segment
        """
        new_segment = Turtle(TURTLE_SHAPE)
        new_segment.color(TURTLE_COLOR)
        new_segment.penup()  # Does not draw line
        new_segment.goto(position)

        # Add the segment to the whole snake body
        self.segments.append(new_segment)

    def extend(self):
        """
        Extend the length of the snake by one
        """
        self.add_segment(self.segments[-1].position())

    def is_hit_wall(self):
        """
        Check if the snake hits the wall
        """
        wall_bound = 290  # Screen width / 2 - 10 = 290
        return self.head.xcor() > wall_bound or self.head.xcor() < -wall_bound or self.head.ycor() < -wall_bound or self.head.ycor() > wall_bound

    def move(self):
        """
        Move the snake always moving
        """
        # Each body segment follows the move of the previous one
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        # Move head
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        """
        Turn the snake to its left
        """
        if self.head.heading() != RIGHT:  # Snake does not turn around
            self.head.setheading(LEFT)

    def right(self):
        """
        Turn the snake to its right
        """
        if self.head.heading() != LEFT:  # Snake does not turn around
            self.head.setheading(RIGHT)

    def up(self):
        """
        Turn the snake upwards
        """
        if self.head.heading() != DOWN:  # Snake does not turn around
            self.head.setheading(UP)

    def down(self):
        """
        Turn the snake downwards
        """
        if self.head.heading() != UP:  # Snake does not turn around
            self.head.setheading(DOWN)
