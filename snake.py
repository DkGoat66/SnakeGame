from turtle import Turtle

# Starting positions for the snake segments
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20  # Distance by which the snake moves in each step
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        # Initialize the snake with starting segments and head
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # Create snake segments at starting positions
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # Add a new segment to the snake
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        # Reset the snake to starting position and clear segments
        for seg in self.segments:
            seg.goto(1000, 1000)  # Move segments off-screen
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        # Extend the snake by adding a new segment at the last segment's position
        self.add_segment(self.segments[-1].position())

    def move(self):
        # Move the snake forward by one step
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # Change snake's direction to up, if not already moving down
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Change snake's direction to down, if not already moving up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # Change snake's direction to left, if not already moving right
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # Change snake's direction to right, if not already moving left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
