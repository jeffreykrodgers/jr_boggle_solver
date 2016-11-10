# Python Programming Challenge
This challenge is inspired by [Boggle](https://en.wikipedia.org/wiki/Boggle), a classic word finding game.

![](http://i.imgur.com/Jd1o6nd.gif)

## General Requirements
Create a python program that solves an `n x m` sized word puzzle,
similar to a boggle board, but where `3 <= n <= 100` and `3 <= m <= 100`.

* The letters must be adjoining in a 'chain'. (Letter cubes in the chain may be adjacent horizontally, vertically, or diagonally.)
* Words must contain at least three letters.
* No letter cube may be used more than once within a single word.

## Details
Your program should accept input from stdin when called
from the shell and write one word per line to stdout

Example of how I want to use it:
```
$ python your_program.py < boggle_board.txt
```

As you can see in the example above, i'll be using a unix shell
and the input will be a text file representation of the board.
1 board row = 1 text file line.

Example of such a file:
```
IEIEE
EAMOR
FNEIN
HRMNW
MBHOT

```

you should also expose a function/class/module/whatever that can
be imported for use elsewhere. The api is up to you, but i'd like
the output to be  a sorted iterable of the found words.

Example:
```python
from cool_boggle_module import solve

boggle_board = ['iez', 'meo', 'plb']

solution = solve(boggle_board)

for word in solution:
   # do something cool with the words
```

## File Descriptions
There're some files you probably want to know about in the repo.

1. dice.py
	* makes boggle boards, i did not put a lot of effort into this
	* `python dice.py > boggle_board.txt`
	* there's some values you can change inside to output different boggle boards
	* the dice values are from a real boggle variant as far as i know,
	found them on some forum
2. dictionary.txt
	* use this to figure out if things are words
3. boards/boggle\_board\*.txt
	* inputs to run your program against
4. solutions/boggle\_board\*.txt
	* solutions to the boards in `/boards`
	* I'll use these to test your program if/when you turn it in,
	and also some other secret ones

## Restrictions
Python 2.7, standard lib only.
We'll be running your code on mac/linux so it should run on those platforms. If you are
a Windows person, but you're not sure if your code is cross platform ready
I'd suggest to run a VM or check out https://c9.io/

## Judgement Day
What we're looking for here is:
* correct output
* good design decisions
* clean code, code that we wouldn't mind working with every day
* not slow, the 100x100 board should run in a decent amount of time
* probably other stuff, maybe write some tests or assertions

To submit your code, just commit all of your changes and push the repo to your own Github account, then send us the link.
Please do not push solution code to a fork of this repo, because then I'll have to reupload it so people
don't take the easy way out and copy your solution, and I don't want to do that.

If you have any questions please ask!

