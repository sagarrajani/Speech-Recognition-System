from tester import *
import os

# word=[]
# for file in os.listdir("test_files"):
#     if file.endswith(".wav"):
#         base=os.path.basename(file)
#         word.append(os.path.splitext(base)[0])

# print word
the_input = raw_input("Enter input: ")
# for i in range(0,len(word)):
filename = "test_files/"+the_input+".wav"
    # print "said word :", word[i]
output=feedToNetwork(extractFeature(filename), testInit())
print ""






