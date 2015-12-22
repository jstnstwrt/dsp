[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> We investigated how bais is introduced into the distibution of the number of children in the families sampled by requesting the information from the children. This is immediately apparent when considering that familiies with no children would immediately be excluded from the sample when acquiring responses in this fashion. More precisely, this is seen by constructing both distributions. First, we create the actual distribution by normalizing the histogram of family size data by the number of families sampled, in effect creating the probability mass function. Then we create the biased distibution by rewieghting the actual distibution we would find if we solicited responses from each child from each family. That is, multiplying the weight associated with a family size by the number of times we would get that response from the *same* family (i.e., the number of children). The corresponding distributions are shown in Figure 1 below. The difference between the actual and biased distibutions can also be seen in the difference in means, 1.024 and 2.404, respectively.


![alt text](https://github.com/jstnstwrt/dsp/blob/master/img/figure_ex31.png =250x "Figure depicting probability mass funcstions" )
>> Figure 1

