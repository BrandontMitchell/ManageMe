from tkinter import *
import time
from PIL import Image, ImageTk
import numpy as np
import matplotlib
import matplotlib.pyplot as plt



netflixBasic = 0
netflixStandard = 0
netflixPremium = 0
#hulu
huluBasic = 0
huluBasicNoAds = 0
huluBasicScreens = 0
huluBasicScreensNoAds = 0
#amazon
aPrime = 0
aPrimeStudent = 0

L = [netflixBasic, netflixStandard, netflixPremium, huluBasic, huluBasicNoAds, huluBasicScreens, huluBasicScreensNoAds, aPrime, aPrimeStudent]
window = Tk()
window.title("Welcome to ManageMe")
window.configure(background="#F0F0F0")
window.geometry('700x700')


def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(scrollregion=canvas.bbox('all'))

canvas = Canvas(window)
canvas.pack(side=LEFT, fill=BOTH)
scrollbar = Scrollbar(window, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=BOTH)
canvas.configure(yscrollcommand = scrollbar.set)
canvas.bind('<Configure>', on_configure)
frame = Frame(canvas)
canvas.create_window((0,0), window=frame, anchor=NW)
canvas.config(width=678, height=600)


def __init__(self, parent, *args, **kwargs):
    Frame.__init__(self, parent, *args, **kwargs)

def location(ans):         #Hulu only in Japan
    if ans == 11:                    #If they select option 1
        L[0] += 8
        L[1] += 7
        L[2] += 6

        L[3] += 15
        L[4] += 12
        L[5] += 10
        L[6] += 9

        L[7] += 10
        L[8] += 11

    elif ans == 12:                  #If they select option 2
        L[0] += 7
        L[1] += 8
        L[2] += 6

        L[3] *= 0
        L[4] *= 0
        L[5] *= 0
        L[6] *= 0

        L[7] += 9
        L[8] += 10

    elif ans == 13:                  #If they select option 3
        L[0] += 9
        L[1] += 8
        L[2] += 7

        L[3] -= 40
        L[4] -= 40
        L[5] -= 40
        L[6] -= 40

        L[7] += 9
        L[8] += 10

    elif ans == 14:                  #If they select option 4
        L[0] += 10
        L[1] += 9
        L[2] += 8

        L[3] -= 50
        L[4] -= 50
        L[5] -= 50
        L[6] -= 50

        L[7] += 9
        L[8] += 10

    elif ans == 15:                  #If they select option 5
        L[0] += 10
        L[1] += 9
        L[2] += 8

        L[3] -= 40
        L[4] -= 40
        L[5] -= 40
        L[6] -= 40

        L[7] += 9
        L[8] += 10

    elif ans == 6:                  #If they select option
        L[0] += 10
        L[1] += 9
        L[2] += 8

        L[3] += 12
        L[4] += 11
        L[5] += 9
        L[6] += 9

        L[7] += 9
        L[8] += 10

    elif ans == 7:                  #If they select option 5
        L[0] += 10
        L[1] += 9
        L[2] += 8

        L[3] -= 40
        L[4] -= 40
        L[5] -= 40
        L[6] -= 40

        L[7] += 0
        L[8] += 0

    elif ans == 7:                  #If they select option 5
        L[0] += 10
        L[1] += 9
        L[2] += 8

        L[3] -= 40
        L[4] -= 40
        L[5] -= 40
        L[6] -= 40

        L[7] += 9
        L[8] += 10

    return L

# Budget
def budget(ans):
    if ans == 21:                    #If they select option 1
        L[0] += 5
        L[1] += 2
        L[2] += 1

        L[3] += 5
        L[4] += 3
        L[5] += 2
        L[6] += 1

        L[7] += 1
        L[8] += 5

    elif ans == 22:                  #If they select option 2
        L[0] += 6
        L[1] += 5
        L[2] += 4

        L[3] += 5
        L[4] += 4
        L[5] += 2
        L[6] += 1

        L[7] += 5
        L[8] += 6

    elif ans == 23:                  #If they select option 3
        L[0] += 6
        L[1] += 5
        L[2] += 4

        L[3] += 6
        L[4] += 5
        L[5] += 4
        L[6] += 3

        L[7] += 5
        L[8] += 6

    elif ans == 24:                  #If they select option 4
        L[0] += 6
        L[1] += 5
        L[2] += 4

        L[3] += 40
        L[4] += 33
        L[5] += 20
        L[6] += 12

        L[7] += 5
        L[8] += 6

    elif ans == 25:                  #If they select option 5
        L[0] += 6
        L[1] += 5
        L[2] += 4

        L[3] += 11
        L[4] += 12
        L[5] += 10
        L[6] += 7

        L[7] += 5
        L[8] += 6

    return L

#3 Kids Content
def kids(ans):
    if ans == 31:
        L[0] += 10
        L[1] += 9
        L[2] += 8

        L[3] += 20
        L[4] += 12
        L[5] += 18
        L[6] += 6

        L[7] += 1
        L[8] += 2

    elif ans == 32:                  #If they select option 2
        L[0] += 10
        L[1] += 9
        L[2] += 8

        L[3] += 6
        L[4] += 5
        L[5] += 4
        L[6] += 3

        L[7] += 4
        L[8] += 5

    elif ans == 33:                  #If they select option 3
        L[0] += 10
        L[1] += 9
        L[2] += 8

        L[3] += 10
        L[4] += 9
        L[5] += 8
        L[6] += 7

        L[7] += 9
        L[8] += 10

    return L


#4 Downloadable Content
def download(ans):
    if ans == 41:
        L[0] += 10
        L[1] += 9
        L[2] += 8

        L[3] += 0
        L[4] += 0
        L[5] += 0
        L[6] += 0

        L[7] += 3
        L[8] += 4

    elif ans == 42:                  #If they select option 2
        L[0] += 10
        L[1] += 10
        L[2] += 10

        L[3] += 4
        L[4] += 4
        L[5] += 4
        L[6] += 4

        L[7] += 6
        L[8] += 6

    elif ans == 43:                  #If they select option 3
        L[0] += 10
        L[1] += 10
        L[2] += 10

        L[3] += 6
        L[4] += 8
        L[5] += 10
        L[6] += 10

        L[7] += 10
        L[8] += 10

    return L

#5 of Devices
def simStream(ans):
    if ans == 51:
        L[0] += 10
        L[1] += 10
        L[2] += 10

        L[3]+= 10
        L[4]+= 10
        L[5]+= 10
        L[6]+= 10

        L[7]+= 10
        L[8]+= 10


    elif ans == 52:                  #If they select option 2
        L[0] += 0
        L[1] += 10
        L[2] += 10

        L[3] += 0
        L[4] += 0
        L[5] += 10
        L[6] += 10

        L[7] += 10
        L[8] += 10


    elif ans == 53:                  #If they select option 3
        L[0] += 0
        L[1] += 0
        L[2] += 10

        L[3] += 0
        L[4] += 0
        L[5] += 20
        L[6] += 20

        L[7] += 8
        L[8] += 8


    elif ans == 54:                  #If they select option 4
        L[0] += 0
        L[1] += 0
        L[2] += 0

        L[3] += 0
        L[4] += 0
        L[5] += 10
        L[6] += 10

        L[7] += 0
        L[8] += 0

    return L

#6 of Profiles
def profile(ans):
    if ans == 61:
        L[0] += 10
        L[1] += 10
        L[2] += 10

        L[3] += 7
        L[4] += 10
        L[5] += 10
        L[6] += 10

        L[7] += 7
        L[8] += 7

    elif ans == 62:                  #If they select option 2
        L[0] += 7
        L[1] += 4
        L[2] += 10

        L[3] += 7
        L[4] += 6
        L[5] += 3
        L[6] += 10

        L[7] += 0
        L[8] += 0

    elif ans == 63:                  #If they select option 3
        L[0] += 7
        L[1] += 7
        L[2] += 7

        L[3] += 7
        L[4] += 0
        L[5] += 10
        L[6] += 10

        L[7] += 0
        L[8] += 0

    return L

#7 Foreign Content
def foreign(ans):         #Hulu only in Japan
    if ans == 71:                    #If they select option 1
        L[0] += 2
        L[1] += 5
        L[2] += 10

        L[3] += 3
        L[4] += 3
        L[5] += 3
        L[6] += 3

        L[7] += 5
        L[8] += 5

    elif ans == 72:                  #If they select option 2
        L[0] += 10
        L[1] += 10
        L[2] += 10

        L[3] += 4
        L[4] += 6
        L[5] += 6
        L[6] += 6

        L[7] += 8
        L[8] += 8

    elif ans == 73:                  #If they select option 3
        L[0] += 10
        L[1] += 10
        L[2] += 10

        L[3] += 5
        L[4] += 10
        L[5] += 10
        L[6] += 10

        L[7] += 10
        L[8] += 10

    return L


#8 Video Quality
def quality(ans):
    if ans == 81:
        L[0] += 10
        L[1] += 7
        L[2] += 10

        L[3] += 4
        L[4] += 10
        L[5] += 10
        L[6] += 10

        L[7] += 10
        L[8] += 10

    elif ans == 82:                  #If they select option 2
        L[0] += 3
        L[1] += 7
        L[2] += 10

        L[3] += 5
        L[4] += 7
        L[5] += 8
        L[6] += 10

        L[7] += 10
        L[8] += 10

    elif ans == 83:                  #If they select option 3
        L[0] += 0
        L[1] += 0
        L[2] += 10

        L[3] += 0
        L[4] += 0
        L[5] += 0
        L[6] += 0

        L[7] += 10
        L[8] += 10

    return L

#9 Closed Captions
def cc(ans):
    if ans == 91:
        L[0] += 10
        L[1] += 7
        L[2] += 10

        L[3] += 4
        L[4] += 4
        L[5] += 4
        L[6] += 4

        L[7] += 6
        L[8] += 6

    elif ans == 92:                  #If they select option 2
        L[0] += 10
        L[1] += 7
        L[2] += 10

        L[3] += 4
        L[4] += 6
        L[5] += 6
        L[6] += 6

        L[7] += 8
        L[8] += 8

    elif ans == 93:                  #If they select option 3
        L[0] += 10
        L[1] += 7
        L[2] += 10

        L[3] += 8
        L[4] += 10
        L[5] += 10
        L[6] += 10

        L[7] += 10
        L[8] += 10

    return L


 # Original Content
def originals(ans):

    if ans == 101:
        L[0] += 10
        L[1] += 10
        L[2] += 10

        L[3] += 2
        L[4] += 6
        L[5] += 4
        L[6] += 6

        L[7] += 2
        L[8] += 2


    elif ans == 102:                  #If they select option 2
        L[0] += 10
        L[1] += 10
        L[2] += 10

        L[3] += 4
        L[4] += 8
        L[5] += 8
        L[6] += 8

        L[7] += 5
        L[8] += 5


    elif ans == 103:                  #If they select option 3
        L[0] += 10
        L[1] += 10
        L[2] += 10

        L[3] += 10
        L[4] += 10
        L[5] += 10
        L[6] += 10

        L[7] += 10
        L[8] += 10

    return L

def finalMovie(ans):

    if ans == 111:
        L[0] += 17
        L[1] += 19
        L[2] += 21

        L[3] += 0
        L[4] += 0
        L[5] += 0
        L[6] += 0

        L[7] += 0
        L[8] += 0


    elif ans == 112:                  #If they select option 2
        L[0] += 0
        L[1] += 0
        L[2] += 0

        L[3] += 10
        L[4] += 15
        L[5] += 15
        L[6] += 15

        L[7] += 0
        L[8] += 0


    elif ans == 113:                  #If they select option 3
        L[0] += 0
        L[1] += 0
        L[2] += 0

        L[3] += 0
        L[4] += 0
        L[5] += 0
        L[6] += 0

        L[7] += 15
        L[8] += 15

    return L



def graph():

    objects = ('Netflix' + '\n' + '(Basic)', 'Netflix' + '\n' + '(Standard)', 'Netflix' + '\n' + '(Premium)', 'Hulu' + '\n' + '(Basic)', 'Hulu' + '\n' + '(Ad Free)', 'Hulu' + '\n' + '(Multi- ' + '\n' + 'screen)', 'Hulu' + '\n' + '(Mult- ' + '\n' + 'screen' + '\n' + 'Ad Free)', 'aPrime', 'aPrime' + '\n' + 'Student')
    x = np.arange(len(objects))
    performance = L

    maxValue = L.index(max(L))
    print(maxValue)
    plt.bar(x, performance, align='center', alpha=.5, color='midnightblue')
    plt.bar(maxValue, performance, align='center', alpha=.5, color='red')
    plt.xticks(x, objects, size=8)
    plt.ylabel('Match Rating')
    plt.title('Best fit streaming service')
    plt.show()

def maxIndex():
    """ Provides the position of the maximum value of L,
    which gives us the streaming service with the highest points,
    ergo, the best fit.
    """
    ind_max=np.argmax(L)
    return ind_max



def restart():
    v1.set(3)
    v2.set(3)
    v3.set(3)
    v4.set(3)
    v5.set(5)
    v6.set(3)
    v7.set(3)
    v8.set(3)
    v9.set(3)
    v10.set(3)
    v11.set(3)

def results():
    if 1 == 1:
        location(v1.get())
        budget(v2.get())
        kids(v3.get())
        download(v4.get())
        simStream(v5.get())
        profile(v6.get())
        foreign(v7.get())
        quality(v8.get())
        cc(v9.get())
        originals(v10.get())
        finalMovie(v11.get())
        time.sleep(0.5)
        graph()





def createQuestion(q, w=5, h=5, color='turquoise', fontc='white'):
    if 1+1 == 2:
        questionName = Label(frame, text = q, width=w, height = h, bg = color, bd = 0, fg = fontc, font = ("helvetica", 13))
    questionName.pack(fill=X, padx=10, pady=20)
    questionName.pack()

#creation of image
pilImage = Image.open('finallogo.png')
image = ImageTk.PhotoImage(pilImage)
imagesprite = canvas.create_image(200, 200, image=image)
header = Label(frame, image = image, bg = 'gray87')
header.pack()

#questions begin, in order as the layout matters
q1 = createQuestion("Where do you plan on using your subscription service?", 5, 2, 'powder blue', 'white')
#frame for radio buttons
iframe1 = Frame(frame)
iframe1.pack(expand=1, fill=X, pady=10, padx=5)
v1 = IntVar()

a11 = Radiobutton(iframe1, text="N America", padx = 13, variable = v1, value = 11).pack(side=LEFT, anchor=W)
a12 = Radiobutton(iframe1, text="S America", padx = 13, variable = v1, value = 12).pack(side=LEFT, anchor=W)
a13 = Radiobutton(iframe1, text="EU", padx = 13, variable = v1, value = 13).pack(side=LEFT, anchor=W)
a14 = Radiobutton(iframe1, text="AUS", padx = 13, variable = v1, value = 14).pack(side=LEFT, anchor=W)
a15 = Radiobutton(iframe1, text="AFR", padx = 13, variable = v1, value = 15).pack(side=LEFT, anchor=W)
a16 = Radiobutton(iframe1, text="JPN", padx = 13, variable = v1, value = 16).pack(side=LEFT, anchor=W)
a17 = Radiobutton(iframe1, text="IND", padx = 13, variable = v1, value = 17).pack(side=LEFT, anchor=W)
a18 = Radiobutton(iframe1, text="Rest of Asia", padx = 13, variable = v1, value = 18).pack(side=LEFT, anchor=W)

q2 = createQuestion("How much are you willing to pay (per month)? ", 5, 2, 'powder blue', 'white')
#frame for radio buttons
iframe2 = Frame(frame)
iframe2.pack(expand=1, fill=X, pady=10, padx=80)
v2 = IntVar()

a21 = Radiobutton(iframe2, text="Under $10", padx = 20, variable = v2, value = 21).pack(side=LEFT, anchor=W)
a22 = Radiobutton(iframe2, text="$10-$20", padx = 20, variable = v2, value = 22).pack(side=LEFT, anchor=W)
a23 = Radiobutton(iframe2, text="$20-$30", padx = 20, variable = v2, value = 23).pack(side=LEFT, anchor=W)
a24 = Radiobutton(iframe2, text="$30-$40", padx = 20, variable = v2, value = 24).pack(side=LEFT, anchor=W)
a25 = Radiobutton(iframe2, text="$40+", padx = 20, variable = v2, value = 25).pack(side=LEFT, anchor=W)


q3 = createQuestion("How important is the availability of kid-friendly entertainment?", 5, 2, 'powder blue', 'white')
#frame for radio buttons
iframe3a = Frame(frame)
iframe3a.pack(expand=1, fill=X, pady=10, padx=120)
v3 = IntVar()

a31 = Radiobutton(iframe3a, text="Indifferent", padx = 20, variable = v3, value = 31).pack(side=LEFT, anchor=W)
a32 = Radiobutton(iframe3a, text="Somewhat Important", padx = 20, variable = v3, value = 32).pack(side=LEFT, anchor=W)
a33 = Radiobutton(iframe3a, text="Very Important", padx = 20, variable = v3, value = 33).pack(side=LEFT, anchor=W)


q4 = createQuestion("How important is having the option to download content?", 5, 2, 'powder blue', 'white')
#frame for radio buttons
iframe4a = Frame(frame)
iframe4a.pack(expand=1, fill=X, pady=30, padx=120)
v4 = IntVar()

a41 = Radiobutton(iframe4a, text="Indifferent", padx = 20, variable = v4, value = 41).pack(side=LEFT, anchor=W)
a42 = Radiobutton(iframe4a, text="Somewhat Important", padx = 20, variable = v4, value = 42).pack(side=LEFT, anchor=W)
a43 = Radiobutton(iframe4a, text="Very Important", padx = 20, variable = v4, value = 43).pack(side=LEFT, anchor=W)


q5 = createQuestion("How many personal accounts will be associated with the membership?", 5, 2, 'powder blue', 'white')
#frame for radio buttons
iframe5 = Frame(frame)
iframe5.pack(expand=1, fill=X, pady=10, padx=140)
v5 = IntVar()

a51 = Radiobutton(iframe5, text="1-2 Devices", padx = 20, variable = v5, value = 51).pack(side=LEFT, anchor=W)
a52 = Radiobutton(iframe5, text="3-4 Devices", padx = 20, variable = v5, value = 52).pack(side=LEFT, anchor=W)
a53 = Radiobutton(iframe5, text="5-6 Devices", padx = 20, variable = v5, value = 53).pack(side=LEFT, anchor=W)


q6 = createQuestion("On how many devices will you use the streaming platform?", 5, 2, 'powder blue', 'white')
#frame for radio buttons
iframe6 = Frame(frame)
iframe6.pack(expand=1, fill=X, pady=10, padx=180)
v6 = IntVar()

a61 = Radiobutton(iframe6, text="1", padx = 20, variable = v6, value = 61).pack(side=LEFT, anchor=W)
a62 = Radiobutton(iframe6, text="2", padx = 20, variable = v6, value = 62).pack(side=LEFT, anchor=W)
a63 = Radiobutton(iframe6, text="3-4", padx = 20, variable = v6, value = 63).pack(side=LEFT, anchor=W)
a64 = Radiobutton(iframe6, text="5+", padx = 20, variable = v6, value = 64).pack(side=LEFT, anchor=W)


q7 = createQuestion("How important to you is having access to international entertainment?", 5, 2, 'powder blue', 'white')
#frame for radio buttons
iframe7 = Frame(frame)
iframe7.pack(expand=1, fill=X, pady=10, padx=120)
v7 = IntVar()

a71 = Radiobutton(iframe7, text="Indifferent", padx = 20, variable = v7, value = 71).pack(side=LEFT, anchor=W)
a72 = Radiobutton(iframe7, text="Somewhat Important", padx = 20, variable = v7, value = 72).pack(side=LEFT, anchor=W)
a73 = Radiobutton(iframe7, text="Very Important", padx = 20, variable = v7, value = 73).pack(side=LEFT, anchor=W)


q8 = createQuestion("What is your minimum preferred video quality ", 5, 2, 'powder blue', 'white')
#frame for radio buttons
iframe8 = Frame(frame)
iframe8.pack(expand=1, fill=X, pady=10, padx=60)
v8 = IntVar()

a81 = Radiobutton(iframe8, text="Indifferent", padx = 20, variable = v8, value = 81).pack(side=LEFT, anchor=W)
a82 = Radiobutton(iframe8, text="Standard Definition", padx = 20, variable = v8, value = 82).pack(side=LEFT, anchor=W)
a83 = Radiobutton(iframe8, text="High Definition", padx = 20, variable = v8, value = 83).pack(side=LEFT, anchor=W)
a84 = Radiobutton(iframe8, text="Ultra High Definition", padx = 20, variable = v8, value = 84).pack(side=LEFT, anchor=W)


q9 = createQuestion("How important is having access to subtitles? ", 5, 2, 'powder blue', 'white')
#frame for radio buttons
iframe9 = Frame(frame)
iframe9.pack(expand=1, fill=X, pady=10, padx=120)
v9 = IntVar()

a91 = Radiobutton(iframe9, text="Indifferent", padx = 20, variable = v9, value = 91).pack(side=LEFT, anchor=W)
a92 = Radiobutton(iframe9, text="Somewhat Important", padx = 20, variable = v9, value = 92).pack(side=LEFT, anchor=W)
a93 = Radiobutton(iframe9, text="Very Important", padx = 20, variable = v9, value = 93).pack(side=LEFT, anchor=W)


q10 = createQuestion("Is watching original series' something that interests you?", 5, 2, 'powder blue', 'white')

iframe10 = Frame(frame)
iframe10.pack(expand=1, fill=X, pady=10, padx=120)
v10 = IntVar()

a101 = Radiobutton(iframe10, text="Indifferent", padx = 20, variable = v10, value = 101).pack(side=LEFT, anchor=W)
a102 = Radiobutton(iframe10, text="Somewhat Interested", padx = 20, variable = v10, value = 102).pack(side=LEFT, anchor=W)
a103 = Radiobutton(iframe10, text="Very Interested", padx = 20, variable = v10, value = 103).pack(side=LEFT, anchor=W)


q11 = createQuestion("If you could only watch one movie for the rest of your life, what would it be?", 5, 2, 'powder blue', 'white')
iframe11 = Frame(frame)
iframe11.pack(expand=1, fill=X, pady=10, padx=120)
v11 = IntVar()

a111 = Radiobutton(iframe11, text="The Breakfast Club", padx = 20, variable = v11, value = 111).pack(side=LEFT, anchor=W)
a112 = Radiobutton(iframe11, text="The Terminator", padx = 20, variable = v11, value = 112).pack(side=LEFT, anchor=W)
a113 = Radiobutton(iframe11, text="Mary Poppins", padx = 20, variable = v11, value = 113).pack(side=LEFT, anchor=W)



lowerPanel = Frame(frame)
lowerPanel.pack(expand=1, fill=X, pady=20, padx=5)
resultsButton = Button(lowerPanel, text="Show Me My Results!", padx = 50, pady = 5, command=results).pack(side=RIGHT, anchor=NE)
restartButton = Button(lowerPanel, text="Start Over!", padx = 50, pady = 5, command=restart).pack(side=LEFT, anchor=SW)







if __name__ == '__main__':
    window.mainloop()
