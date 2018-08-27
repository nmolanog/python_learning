###chapter 2: scope
##num is in the local scope, no available in global
def func1():
    num = 3
    print(num)
### num is acceced from the local environment to the global one, and changed in the global
def func2():
    global num
    double_num = num * 2
    num = 6
    print(double_num)
    
num=5
print(num)    
func1()
print(num)    
func2()
print(num)    


###another example modifying a global environment variable
# Create a string: team
team = "teen titans"

# Define change_team()
def change_team():
    """Change the value of the global variable team."""

    # Use team in global scope
    global team

    # Change the value of team in global: team
    team = "justice league"
# Print team
print(team)

# Call change_team()
change_team()

# Print team
print(team)


###import builtins
import builtins
dir(builtins)
###find which of the following isn in dir(builtins)
["sum","range","array","tuple"] in dir(builtins)

for i in ["sum","range","array","tuple"]:
    if not i in dir(builtins):
        print(i)

###more elegant
res={}        
for i in ["sum","range","array","tuple"]:
    res[i]=i in dir(builtins)
    
print(res)    

#nested functions
# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""

    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'

    # Return a tuple of strings
    return (inner(word1), inner(word2), inner(word3))

# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))

# Define echo
###echo returns a function
def echo(n):
    """Return the inner_echo function."""

    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    # Return inner_echo
    return inner_echo

# Call echo: twice
twice = echo(2)
# Call echo: thrice
thrice = echo(3)

# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))



# Define echo_shout()
###just to show nonlocal variable manipulation
def echo_shout(word):
    """Change the value of a nonlocal variable"""
    
    # Concatenate word with itself: echo_word
    echo_word = word+word
    
    #Print echo_word
    print(echo_word)
    
    # Define inner function shout()
    def shout():
        """Alter a variable in the enclosing scope"""    
        #Use echo_word in nonlocal scope
        nonlocal echo_word
        
        #Change echo_word to echo_word concatenated with '!!!'
        echo_word = echo_word + '!!!'
    
    # Call function shout()
    shout()
    
    #Print echo_word
    print(echo_word)

#Call function echo_shout() with argument 'hello'    
echo_shout('hello')

###defaults arguments
# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
     exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1*echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo() with "Hey": no_echo
no_echo = shout_echo("Hey")

# Call shout_echo() with "Hey" and echo=5: with_echo
with_echo = shout_echo("Hey",5)

# Print no_echo and with_echo
print(no_echo)
print(with_echo)


    def shout_echo(word1, echo=1, intense=False):
        """Concatenate echo copies of word1 and three
        exclamation marks at the end of the string."""
    
        # Concatenate echo copies of word1 using *: echo_word
        echo_word = word1 * echo
    
        # Capitalize echo_word if intense is True
        if intense is True:
            # Capitalize and concatenate '!!!': echo_word_new
            echo_word_new = echo_word.upper() + '!!!'
        else:
            # Concatenate '!!!' to echo_word: echo_word_new
            echo_word_new = echo_word + '!!!'
    
        # Return echo_word_new
        return echo_word_new
    
    # Call shout_echo() with "Hey", echo=5 and intense=True: with_big_echo
    with_big_echo = shout_echo("Hey",5,True) 
    
    # Call shout_echo() with "Hey" and intense=True: big_no_echo
    big_no_echo = shout_echo("Hey",intense=True)
    
    # Print values
    print(with_big_echo)
    print(big_no_echo)

