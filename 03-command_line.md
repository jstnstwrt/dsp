# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

1. multiple flags can be called by combinding them or calling them all seperately. e.g., -a -l -h or -alh

2. 


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

The command ls (without flags) lists out all of non hidden files and directories contained in the working directory you are sitting in.

 If you add the flag -a, ls -a returns the complete list of files/directories, including all hidden files. The -l flag concerns the information displayed about each file listed, it stands for long form. So the listed files also include last date modified, premissions, filename, file owner, and so on. If you use the combined flag of -lh, it combines the long form flag with the human readable formatting flag. This means that file sizes displayed for each file reported will be in the easily readable 3.1K vs 3127. 

ls -a, ls -l are meaningful, but ls -h isnt meaningfully different than ls.
ls -al, ls lh are meaningful, but ls -ah isnt meaningfully different from ls -a.
ls -alh is a meaningful command as well.  

---


---

What does `xargs` do? Give an example of how to use it.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

