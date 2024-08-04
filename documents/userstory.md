User Story
Title: Image to Knitting or Crochet Pattern Converter

As a: Hobbyist or Professional Knitter/Crocheter

I want: An application that converts my images into knitting or crochet patterns.

So that: I can easily follow the pattern to knit or crochet the image design.

Brainstorming Session

1. Understanding the User Needs

Primary Users:

Hobbyist Knitters
Professional Knitters
Hobbyist Crocheters
Professional Crocheters
Art and Craft Enthusiasts
Key Requirements:

Ability to upload any image format (PNG, JPG, JPEG)
Define pixel size for the pattern
Generate a pixelated version of the image
Display a color grid with color names
Provide a tooltip for each cell displaying color and position
Sidebar list of colors with highlighted click and hover information 2. Core Functionalities

a. Image Uploading

Objective: Allow users to upload an image from their device.
Requirements:
An input element to select and upload an image.
Supported formats: PNG, JPG, JPEG.
b. Define Pixel Size

Objective: Allow users to specify the granularity of the knitting or crochet pattern.
Requirements:
An input field to specify the pixel size.
Default value set to a reasonable pixel size.
c. Image Processing

Objective: Convert the uploaded image into a pixelated version based on the specified pixel size.
Requirements:
Use an algorithm to reduce the image resolution.
Enhance and resize the image back to original dimensions using the reduced resolution.
d. Color Grid Generation

Objective: Display a grid where each cell represents a color in the pixelated image.
Requirements:
Create a grid layout using HTML and CSS.
Each cell should display the respective color.
e. Tooltip Display

Objective: Provide additional information when hovering over a cell.
Requirements:
Display color name and position when a cell is hovered over.
Implement using CSS and JavaScript.
f. Color List Sidebar

Objective: Display a list of all colors used in the pattern.
Requirements:
Generate a list of unique colors from the pixelated image.
Display each color with its name and allow interaction.
Highlight and show details on hover and click.
