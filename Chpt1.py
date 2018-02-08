
#NOTES Friday Feburary 2nd

# Below are some excercises from chapter 1, took me a couple of hours to read everything and do them. I installed python, watched a video about it, I'll use atom. I have some questions about the later excercises though. I had trouble getting the chaotic function to work as they illustrated in the chapter, I think there are a couple of steps missing so need to figure that out. I tried playing around with it but could not get the function to run.


def hello():
    print "Hello"
    print "computers are fun"

hello()


def greet(person):
    print "Hello", person
    print "how are you?"

greet("John")

greet("Emily")


# File: test.py
# A simple program illustrating chaotic behavior

def main():
    print "this program illustrates a chaotic function"
    x = input("enter a  number between 0 and 1: ")
    for i in range (10):
        x = 3.9 * x * (1 - x)
        print x

main()




# a) software determines what any  computer (hardware) can do. creating software is called programming. Hardware has to do with like, the central processing unit, the random access memory etc. the CPU follows the fetch, excecute cycle, in which it grabs instructions from software and makes the instructions happen.

# b) an  algorithm is a step-by-step process for coming to a desired result, kind of like a recipe. Failing to find an algorithm does not make a problem unsolvable. analysis is examining algorithms and problems mathematically.

# c) Natural language is fraught with abiguety and imprecision. It is not suited for describing complex algorithms.

# d)Python is a high-level language, so you can express things more naturally like c = a+b instead of saying, (at the machine-language level) load the number from mem location 938 into the cpu, load the number from mem location 314 into the cpu, add the two numbers in the cpu,store the result into the location 2003...

# e) a compiler is a complex computer program that take sanother program written in a high-level language and translates into an equavalent program in the machine language of some computer. An interpreter is a program that simulates a computer that understands high-level language. rather than translating the source program into a machine language equavalent, the interpreter analyzes and executes the source code instruction by instruction as nescessary.

# f) syntax vs. sementics- although the different programming languages have many different details, they all share the property of having well defined, unambiguous syntax and semantics. precise form in a programming language is its syntax, and precise meaning is its semantics. the process fo writing an algortithin is called coding
