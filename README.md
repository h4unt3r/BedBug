# BedBug
* * * *
### Python profiling for the Lazy Programmer

So here is the deal... I was working with a particularly convoluted piece of 
python and I had the idea... wrap every function call and put it in a tree...
Then graph that shit! Crazy right? Well not really. Anyway now that I've wasted
a little bit of your patience, its time to save time!

Also I AM aware that there is a more developed project called pycallgraph or 
something... I checked it out... It is much better than this! So if you want a
tool like that, fuck off and get it already ;) This is quick and dirty and kind
of cool, nothing more!

## Usage
Simple import and then 'hook' the class you wish to profile:

    from BedBug import bedbug
    bedbug.classHook( classToHook )

And just like that you run your code and bedbug will take care of the rest!
Currently because I was too lazy to write tests for executables and I use this
in Windows a fair bit (ewwwwwwww) I dont autogenerate the images... So you can
do that, write a little script, cmon.
Dot files are output in a directory called .dot and are named for the main
function that they replace (i.e. init for a class). Yeah. If you get use out of
it send me a note? Suggestions? Whatevs :D

Cheers!
