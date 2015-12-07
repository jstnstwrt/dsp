# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

1. Multiple flags can be called by combinding them or calling them all seperately. e.g., -a -l -h or -alh

2. Edit the file at '~/.bash_profile' to create custom commands by setting aliases. Can be exteremly helpful when you find yourself doing a long sequence of commands over and over.

3. Use the -p flag with 'mkdir' if you want create a sequence of nested directories in one step.

4. 'popd' enables you to quickly navigate back to directories that you have set (using 'pushd') in your directory stack. In regular english 'pushd' says to save where I am and then go somewhere, whereas 'popd' says go back the location I saved. 

5. 'less' displays some of a file at a time with read only capabilities. My initial impulses was to just use vim to read a file, but remember that less (or more) should be used when there is a concern about writing to the file you are only intending to read (e.g., a log file).

6. In redirection, if you use '>' it will either direct the output of whatever is to the left of the operator to a new file or write over the existing file with that name. However if you use '>>' will either create a new file with the output or append the output to the existing file with same name. 

7. '|' is the pipe redirection operator. It sends the output of whatever is to the left of the pipe "through" whatever function or command is to the left of the pipe. For example, imagine the you wanted to sort the output of ls in alphabetical order. This can be accomplished by 'ls | sort'. You can use multiple pipe operators at once. 

8. Sometimes you may want to preform an operation to multiple files all at once, in these cases, you can use '*', the wild card matching operator. 

9. The 'find' command is used to find all the files that meet some condition, e.g., end with .txt. Remember that '.' is used to tell find to start looking in the current directory.

10. The command 'export' allows you to set environment variables. Important environment variable to remember: $PATH. The command 'unset' unsets environment variables.    


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

The command ls (without flags) lists out all of non hidden files and directories contained in the working directory you are sitting in.

 If you add the flag -a, ls -a returns the complete list of files/directories, including all hidden files. The -l flag concerns the information displayed about each file listed, it stands for long form. So the listed files also include last date modified, premissions, filename, file owner, and so on. If you use the combined flag of -lh, it combines the long form flag with the human readable formatting flag. This means that file sizes displayed for each file reported will be in the easily readable 3.1K vs 3127. 

The flags -a and -l are meaningful, but -h on it's own is not meaningfully different than the ls command. The combined flags -al and  -lh are meaningful, but -ah is not meaningfully different from ls -a. The combined flag -alh is a meaningful command as well.  

---


---

What does `xargs` do? Give an example of how to use it.

The command xargs helps to transform space or tab delimited data coming in via the stdin, the standard input stream, into arguments. This is very helpful because some functions do not accept input in the form the standard input stream. This is often used with pipes that connects stdout of the first process to the stdin on the second process. 

For example, if you a sequence of file paths as the stdout of some process and you wanted to do somesthing with them, say delete them. In this case, because 'rm -rf' does not act on stdout directly, you would use xargs to transform the filepath data into arguments that the second process can now act on.

---

