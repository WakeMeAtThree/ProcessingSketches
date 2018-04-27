﻿# 30 Days of Processing

I've been away to python land for a while, but I'm back to the java jungle. This repo is a daily commitment to *writing* a sketch a day in processing, no matter how simple or basic. 

My exploration started off around the GLSL shaders and geometry transformations. It then went through Daniel Shiffman coding challenges, then started to be inspired by the processing's twitter community. The open source community for processing is quite wonderful and generous with the knowledge they're providing, which I will try my best to name in this repository. 

# Useful tools and resources
- [Markdown table generator](https://www.tablesgenerator.com/markdown_tables#)
- [Another table generator](https://donatstudios.com/CsvToMarkdownTable)
- [Book of shaders](http://thebookofshaders.com/)
  - [Shaping functions](http://www.thebookofshaders.com/05/)
- [Andres Colubri's PShader tutorial](https://processing.org/tutorials/pshader/) as well as the accompanying [github repo](https://github.com/codeanticode/pshader-tutorials)
- [Shadershop for creating functions](http://tobyschachman.com/Shadershop/)
- [Color generator](https://coolors.co/) which is useful for generating some color palettes

# Post-repo ideas:
- Varying the CodingTrain CC's in its own repo (as well as a plan for plans for physical manifestations of it)
- Python implementation of one of these sketches using numpy + matplotlib
- Accompanying LQ/HQ gifs OR p5js translations for sharing online
- Default 3d model of my own for future use (elaborately intricate to accomodate different surface conditions)
- Observation: I'm gravitating more and more towards patterns-based sketches.
___

# 30 Days of Processing

I've been away to python land for a while, but I'm back to the java jungle. This repo is a daily commitment to *writing* a sketch a day in processing, no matter how simple or basic. 

My exploration started off around the GLSL shaders and geometry transformations. It then went through Daniel Shiffman coding challenges, then started to be inspired by the processing's twitter community. The open source community for processing is quite wonderful and generous with the knowledge they're providing, which I will try my best to name in this repository. 

# Useful tools and resources
- [Markdown table generator](https://www.tablesgenerator.com/markdown_tables#)
- [Another table generator](https://donatstudios.com/CsvToMarkdownTable)
- [Book of shaders](http://thebookofshaders.com/)
  - [Shaping functions](http://www.thebookofshaders.com/05/)
- [Andres Colubri's PShader tutorial](https://processing.org/tutorials/pshader/) as well as the accompanying [github repo](https://github.com/codeanticode/pshader-tutorials)
- [Shadershop for creating functions](http://tobyschachman.com/Shadershop/)
- [Color generator](https://coolors.co/) which is useful for generating some color palettes

# Post-repo ideas:
- Varying the CodingTrain CC's in its own repo (as well as a plan for plans for physical manifestations of it)
- Python implementation of one of these sketches using numpy + matplotlib
- Accompanying LQ/HQ gifs OR p5js translations for sharing online
- Default 3d model of my own for future use (elaborately intricate to accomodate different surface conditions)
- Observation: I'm gravitating more and more towards patterns-based sketches.
___

**id**  |  **Name**                                    |  **Description**                                                                                                                                                                                                                                                                                                                                          |  **Processing - Java**  |  **p5js**  |  **Python**
--------|----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|------------|--------------------
1       |  Placeholder Debut                           |  This is the debut sketch to start off this repo.                                                                                                                                                                                                                                                                                                         |  :white_check_mark:     |            |
2       |  Square shift                                |  Building upon the previous sketch and adding a square motion.                                                                                                                                                                                                                                                                                            |  :white_check_mark:     |            |
3       |  Steering Trails Blur GLSL                   |  Testing out filter blur GLSL shader by applying it to steering trails.                                                                                                                                                                                                                                                                                   |  :white_check_mark:     |            |
4       |  Ten Print Class                             |  Factoring out a ten print sketch into its own class, testing blur shader on it.                                                                                                                                                                                                                                                                          |  :white_check_mark:     |            |
5       |  JSON streamer                               |  Ball bouncing class written in python that runs and streams to a json, with a processing sketch that visualizes contents of json in real time. Experimenting with ways of connecting both languages.                                                                                                                                                     |  :white_check_mark:     |            |  :white_check_mark:
6       |  Blur Filter expanded                        |  Added more kernels to the glsl example in the processing Blur Filter example, as well as discovered a neat trick to have changes to glsl files update immediately, thus giving a better feedback as you play around with glsl code. This could be a great tutorial or p5js sketch for others to learn glsl as well.                                      |  :white_check_mark:     |            |
7       |  Line Twirls                                 |  I'm quite busy today to think of a more elaborate sketch, so here's a simple line twirling with changing colors.                                                                                                                                                                                                                                         |  :white_check_mark:     |            |
8       |  Spiral Lerp                                 |  Mixing two colors as a point turns around the middle of the canvas.                                                                                                                                                                                                                                                                                      |  :white_check_mark:     |            |
9       |  Octagonal Module                            |  Module for an octagonal shifting edges module, inspired by hexes sketch by Dave Whyte                                                                                                                                                                                                                                                                    |  :white_check_mark:     |            |
10      |  Octagonal Module Tiled                      |  Module tiled on the canvas                                                                                                                                                                                                                                                                                                                               |  :white_check_mark:     |            |
11      |  Octagonal Module Tiled with Distance Field  |  Module tiled on the canvas with distance field                                                                                                                                                                                                                                                                                                           |  :white_check_mark:     |            |
12      |  Octagonal Module Class                      |                                                                                                                                                                                                                                                                                                                                                           |  :white_check_mark:     |            |
13      |  Lerp tricks                                 |  Playing around with lerp and delay following the Etienne Jacob's tutorial on using lerp for some interesting effects                                                                                                                                                                                                                                     |  :white_check_mark:     |            |
14      |  Polygonal Tunnel                            |  Created a polygonal tunnel sketch after being inspired by some of hexiosis gifs                                                                                                                                                                                                                                                                          |  :white_check_mark:     |            |
15      |  Radial Field                                |  Created a center radial field effect. Useful tool in future processing sketches. ~~Need to translate to java, as I struggled to figure out a way of sorting in java that is as intuitive as python.~~ Translated to java after getting help from /processing subreddit (Thanks, mrsirrisrm!)                                                             |  :white_check_mark:     |            |  :white_check_mark:
16      |  Hammer Time                                 |  Followed along with [Jeremy Behreandt’s] (https://medium.com/@behreajj/3d-models-in-processing-7d968a7cede5) medium article on basic material properties for 3d shapes in processing. Created a sample geometry to play with in processing.                                                                                                              |  :white_check_mark:     |            |
17      |  Subtract Mode                               |  I've always looked at drawings and illustrations of Iakov Chernikov where he overlapping geometries and colored them in a way that is best described today as Subtract mode. This sketch illustrates the interesting variations achievement from this mode by applying it on a pattern of circles growing in radii and arranged in a hexagonal pattern.  |  :white_check_mark:     |            |
18      |  SVG Curves                                  |  Needed to find a connection between my existing workflow in drawing in Rhino 3D, Adobe illustrator and Processing. This sketch illustrates a good way of doing this, and I'm thinking of potentially using this in Circle Morphing coding challenge sketch later.                                                                                        |  :white_check_mark:     |            |
19      |  PShape + Ball class                         |  Displayed bouncing balls as a moving QUAD shape with varying vertex colors. Different way of visualizing the traditional ball sketch.                                                                                                                                                                                                                    |  :white_check_mark:     |            |
20      |  Circle Triangle Morph                       |  One svg file containing one triangle and one circle, subdivided and oriented in a way so that point indices are aligned nearest to each other. Demonstrating of what can be done by combining vector drawing workflow with processing                                                                                                                    |  :white_check_mark:     |            |
21      |  3D Curve import                             |  Trying to import a 3-dimensional curve into Processing by exporting the curve vertices as points in csv                                                                                                                                                                                                                                                  |  :white_check_mark:     |            |
22      |  To be determined                            |                                                                                                                                                                                                                                                                                                                                                           |                         |            |
23      |  To be determined                            |                                                                                                                                                                                                                                                                                                                                                           |                         |            |
24      |  To be determined                            |                                                                                                                                                                                                                                                                                                                                                           |                         |            |
25      |  To be determined                            |                                                                                                                                                                                                                                                                                                                                                           |                         |            |
26      |  To be determined                            |                                                                                                                                                                                                                                                                                                                                                           |                         |            |
27      |  To be determined                            |                                                                                                                                                                                                                                                                                                                                                           |                         |            |
28      |  To be determined                            |                                                                                                                                                                                                                                                                                                                                                           |                         |            |
29      |  May the 4th Sketch                          |                                                                                                                                                                                                                                                                                                                                                           |                         |            |
30      |  To be determined                            |  Final sketch                                                                                                                                                                                                                                                                                                                                             |                         |            |