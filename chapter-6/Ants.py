# write a program to print the lyrics for ten verses of the ants go marching.
#
# def antsGoMarching():
#     print "the ants go marching one by one"
#
# def cheer():
#     print "hurrah! hurrah!"
#
#
# def firstHalf():
#     antsGoMarching()
#     print
#
#
# firstHalf()


def antsACTION (motionsIndex):
    motions = ["suck his thumb", "tie his shoe"]
    print ("The little one stops to %s," %motions[motionsIndex])
def words():
    numbers = ['one','two']
    for i in range(2):

        print ("The ants go marching %s by %s, hurrah! Hurrah!\nThe ants go marching %s by %s, hurrah! Hurrah!\nThe ants go marching %s by %s,"%tuple([numbers[i]]*6))

        antsACTION(i)
    print ("And they all go marching down...\nIn the ground...\nTo get out...\nOf the rain.\nBoom! Boom! Boom!")
words()
