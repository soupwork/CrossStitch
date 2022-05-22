# CrossStitch
Python Program to create cross stitch patterns

A program to create cross stitch patterns? How hard could it be? Ha! For any creative/coder/engineering type, any task, no matter how simple, can be convoluted into something so massive that George R.R. Martin and his Game of Thrones pantheon of characters would shake their heads and tear-up at.

I'll work on this in at least three stages.
The first stage will be to just get the background mechanics working. so I can take an image, resize it (probably using Pillow), put it into an array (probably using Numpy), set colours (colors), and save the pattern.

The second stage will be to convert to a MVC pattern to provide a gui interface and some useage enhancements.

The third stage will further develop the User Experience (UX) with more control over the transformation from an image to a cross stitch pattern.

I know very little about image processing, but now seems like a good time to learn. Likewise with Pillow and Numpy. Learning new things is a reward in itself. Building something new is a challenge and a trophy at the end. Sharing knowledge, ideas, and discoveries is a gift that persists to the end of the universe.

The cloth used for cross stitch is Aida cloth, and usually has a 'fabric count' or 'stitch count' which measures the number of stitches per inch. 10 count Aida cloth would allow/require 10 stitches per inch. 20 count would have 20 stitches per inch. Typical sizes are 7, 10, 11*, 12, 14*, 16, 18*, 22*, and 28* count(wikipedia). Most common sizes from other sources marked with "*". 
I know. It upsets my sense of math and symetry, but I think this is more about what makes sense to the people making the cloth and doing the stitching.
If I wanted the resulting image to fit on a 10 inch x 10 inch square, the image size would be 110 x 110
Regardless of my desire to have things work out in even numbers, I want to accomodate the end user more. 

At the command line, starting the program, I'll have options for
  * -f or -fi filename in
  * -fo filename out (default is filename + '_xstitch') should program save as png? pdf?
  * -x -y size of canvas. if only x, then a square is assumed
  * -sc Aida Cloth Stitch Count (should this be ac, or cc?)
