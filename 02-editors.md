# Choose and learn your editor(s)

Computing's interface is text. To work effectively, you need to be fluent with this interface.


### Typing

It may sound silly, but [make sure](http://www.typingtest.com/) you know how to type. You should be comfortable typing with perfect accuracy at 60 words per minute, at least. If you currently can't, practice until you can.

A lot of your work will be done in a text editor. You have to know how to use your editor. Any editor will work, but knowing a powerful editor well will make you faster, more comfortable, and more effective.


### Terminal Editor

Sometimes you will need to use a non-graphical text editor. This means an editor that will run entirely inside a terminal window, without spawning a new window, entirely without mouse input.

Make sure that you know at least one of these well enough to do basic editing in a terminal:

 * Emacs
 * vim
 * nano

You should know at least enough vim to be able to get out of it, because it is the default on many systems and you might find yourself in it even if you didn't mean to be.

If you intend to use a graphical editor that doesn't run in a terminal, nano might be a good choice for you because it is very simple.

Both Emacs and vim have built-in interactive tutorials that you can try.

---

What terminal editor will you use? How did you make your decision?

I will use vim as a terminal text editor. I made this decision because it seems that nano will be easy to learn on the fly if needed and I'd rather spend the time learning the more difficult but efficient editor. I felt that emacs was not the right tool for me because it seems that the value from emacs comes from it's ability to do absolutely everything you may need from the terminal and I would really only need it for it's  text editing capabilities. 

---


### Graphical Editor

You will probably spend most of your time with access to a graphical interface, where you have more choices in editors and integrated development environments.

Popular editors and IDEs include:

 * Emacs
 * vim
 * Sublime
 * Atom
 * Spyder
 * PyCharm

If you choose Emacs or vim, you will have essentially the same editor experience across graphical and non-graphical environments, which is nice. It's also nice to be able to work without ever having to use a mouse. Emacs and vim have somewhat steep learning curves, but they give you the ability to customize your environment quite a lot to make it exactly what you want.

Sublime is probably the most popular editor for new coders. You can set it up to integrate with Python fairly well. Atom is pretty similar to Sublime but has an interesting open architecture and is developed by folks at GitHub.

Spyder and PyCharm are IDEs for Python. They try to give you a fully configured setup out of the box.

We will also use Jupyter (IPython) notebooks, but this does not remove the need for proficiency in an editor or IDE.

---

What graphical editor will you use? How did you make your decision? What are some interesting features of your editor? What are some useful keyboard shortcuts for your editor? How do you customize your editor?

I have decided to use Sublime Text as my graphical editor. I did some reading online to see how more experienced Python developers compared various popular editors. I found that most ranked Sublime very highly relative to others, especially for its extensibility and extent to which it is customizable through the use of packages and key bindings. It seems that there is much room for efficiency gains in my programming through the use of this editor.

Some keyboard shortcuts for Sublime Text:

shift + command + f, Allows you to search for strings throghout an entire set of project files. Futhermore, it automatically creates a text file for you describing the filepath and line number of every instance of the string found.
 
option + command + n, where n is a number 1-5, Allows you to control the screen layout and split the screen you up to four times. 

control + command + f, Applies full screen mode.

cmd + left (right) arrow key, Takes the cursor to the beginning (end) of the current line.

cmd + d, Selects a word and by repeating the shortcut, it selects the next occurences of the word. You can select as many as you like. 

You can customize Sublime in a number of ways. First you can create custom keyboard shortcuts by creating your own key bindings. These are set in the Packages/User/Default.sublime-keymap XML file containing the defualt binds and are fully configurable. Additionally, Sublime can be customized by installing other exiting packages accomplishing certian ends. This can be done using Packege Control which needs to be installed.    

---
