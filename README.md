﻿# 30 Days of Processing
Hi.

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
- Recreating classic games might also be a good idea to work towards
- Take a look at this and [implement it in one of your sketches](https://stackoverflow.com/questions/8200243/can-i-store-function-names-in-final-hashmap-for-execution/8200427).
- [Alexander Calder sculptures](https://www.google.ae/search?q=alexander+calder&safe=strict&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiPm9bPvPjaAhVMuhQKHYvyB3oQ_AUICigB&biw=1163&bih=536)
- Recreate this [moving head sculpture in processing](https://twitter.com/Rainmaker1973/status/993837231247851520)
- typing spaces

# Useful code snippets

The following are useful `ffmpeg` commands for making animation gifs/mp4. 

Turning image sequence to a video
```
ffmpeg -framerate 30 -i animation%3d.png -pix_fmt yuv420p output.mp4
```

Concatenating two videos to create a reverse loop
```
ffmpeg -i input.mov -filter_complex "[0:v]reverse,fifo[r];[0:v][r] concat=n=2:v=1 [v]" -map "[v]" output.mp4
```

Generating palette.png and using it to create smaller gifs. [Reference 1.](https://engineering.giphy.com/how-to-make-gifs-with-ffmpeg/) [Reference 2.](https://medium.com/@colten_jackson/doing-the-gif-thing-on-debian-82b9760a8483)
```
ffmpeg -i output.mp4 -vf palettegen palette.png
ffmpeg -i output.mp4 -i palette.png -filter_complex “fps=30,scale=400:-1:flags=lanczos[x];[x][1:v]paletteuse” output.gif
ffmpeg -ss 2.6 -t 1.3 -i output.mp4 -i palette.png -filter_complex “fps=30,scale=400:-1:flags=lanczos[x];[x][1:v]paletteuse” output.gif
```

Running a processing sketch in terminal [Check this out](https://github.com/processing/processing/wiki/Command-Line):

```
processing-java --sketch=%cd% --run
```

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
16      |  Hammer Time                                 |  Followed along with [Jeremy Behreandt’s](https://medium.com/@behreajj/3d-models-in-processing-7d968a7cede5) medium article on basic material properties for 3d shapes in processing. Created a sample geometry to play with in processing.                                                                                                               |  :white_check_mark:     |            |
17      |  Subtract Mode                               |  I've always looked at drawings and illustrations of Iakov Chernikov where he overlapping geometries and colored them in a way that is best described today as Subtract mode. This sketch illustrates the interesting variations achievement from this mode by applying it on a pattern of circles growing in radii and arranged in a hexagonal pattern.  |  :white_check_mark:     |            |
18      |  SVG Curves                                  |  Needed to find a connection between my existing workflow in drawing in Rhino 3D, Adobe illustrator and Processing. This sketch illustrates a good way of doing this, and I'm thinking of potentially using this in Circle Morphing coding challenge sketch later.                                                                                        |  :white_check_mark:     |            |
19      |  PShape + Ball class                         |  Displayed bouncing balls as a moving QUAD shape with varying vertex colors. Different way of visualizing the traditional ball sketch.                                                                                                                                                                                                                    |  :white_check_mark:     |            |
20      |  Circle Triangle Morph                       |  One svg file containing one triangle and one circle, subdivided and oriented in a way so that point indices are aligned nearest to each other. Demonstrating of what can be done by combining vector drawing workflow with processing                                                                                                                    |  :white_check_mark:     |            |
21      |  3D Curve import                             |  Trying to import a 3-dimensional curve into Processing by exporting the curve vertices as points in csv                                                                                                                                                                                                                                                  |  :white_check_mark:     |            |
22      |  Tetris geometry                             |  2D implementation of tetris geometry I had in mind. This is the first step in setting up a 3D tetris tilings (likely to look more columnar)                                                                                                                                                                                                              |  :white_check_mark:     |            |
23      |  Circ-Tri morph tiled                        |  Fixed some coordinate issues with the svg file as well as tiled hexagonally the previous pattern in Difference mode (again!). Makes for some interesting output. I also left the x and y spacing variable depending on your mousePressed coordinates.                                                                                                    |  :white_check_mark:     |            |
24      |  Circ-Tri morph with offset                  |  Added slight offset to previous circ-tri sketch                                                                                                                                                                                                                                                                                                          |  :white_check_mark:     |            |
25      |  SpherePyraMorph                             |  Morphing between pyramid and spherical geometry. Extension of previous 2D morphing sketch into 3D                                                                                                                                                                                                                                                        |  :white_check_mark:     |            |
26      |  May the 4th Sketch                          |  May 4th coding challenge done while following Daniel Shiffman livestream.                                                                                                                                                                                                                                                                                |  :white_check_mark:     |            |
27      |  Polygonal Ripples                           |  Ripple sketch of polygons (or ellipses) and `blendMode(DIFFERENCE)`                                                                                                                                                                                                                                                                                      |  :white_check_mark:     |            |
28      |  Chromatic Abberation                        |  Sketch illustrating an approach of creating a chromatic abberation effect.                                                                                                                                                                                                                                                                               |  :white_check_mark:     |            |
29      |  Bumpy Road Through Space                    |  Variation on the Daniel Shiffman's starfield coding challenge                                                                                                                                                                                                                                                                                            |  :white_check_mark:     |            |
30      |  Muqarnas                                    |  Variation on the Daniel Shiffman's phyllotaxis coding challenge. Possibly useful for making muqarnas designs in the future.                                                                                                                                                                                                                              |  :white_check_mark:     |            |

# Final thoughts

~30 days of Processing~, finished on April 8th, 2018. 

Overall, it was a good haul and I picked up good tools for processing toolbox. Moving forward I'm planning to spin off some off these sketches into a series deserving of its own repo. There is a lot of things to mine from in modular/pattern based sketches. Unresolved issues include:

- figuring out a way to move mesh vertices as if it's welded 
- and more optimized gifs (though making good head way using ffmpeg). 

May revisit this to either check off p5js sketches or to turn this into 60 (accumulative) days of processing, or to just turn this into a processing playground. 
