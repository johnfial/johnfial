2021 04 Nov:

'''
Evan Hackett  11:38 AM
So copilot solved the halting problem? :smile:
11:39
Actually, looking at the code, it looks like it will indeed run forever if one of the input programs doesn’t halt. So I guess Turing was right after all. (edited) 
11:40
haha pretty cool though

Michael  12:15 PM
So the problem is that a program that doesn't halt, won't halt, and this program will never say it does not halt?  Tbh, I had a bit of a hard time understanding the halting problem. A friend told me I should try it on copilot.

Evan Hackett  12:34 PM
So some necessary context is that the halting problem was originally more of a thought experiment put forth by Alan Turing, as he was exploring the landscape of “what is computable by a Universal Turing Machine?” Basically, what are the limits of computation? What are some problems that cannot be solved?
So, one such example of an “unsolvable problem” is to create a turing machine (lets just call this a “program”), that can analyze any arbitrary program and determine if it will run forever or not. This is known as the halting problem. What is interesting is that Turing proved that this cannot be constructed. It is impossible to create a program that can tell you whether another program will halt or not, for any given input program.
To bring it back to your copilot-generated code, you can see on lines 59-60 that it simply runs the programs, and then only after they have finished running will it determine if they halted or not. Meaning, if one of the input programs gets caught in an infinite loop, the copilot program will never reach line 63 and will just run forever.
Thus we have yet to construct a program that can achieve the unachievable.
:raised_hands:
2

12:37
For those curious, you should look into Turings proof. It is not as math-heavy as you might expect. It’s actually quite accessible. I think computerphile (on youtube) has some videos on this topic.

Michael  1:20 PM
Nice explanation, I'll have to find that vid, computerphile is great
:+1:
2

'''