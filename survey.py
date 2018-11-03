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


#1 Location
def location(ans):         #Hulu only in Japan
    if ans == 1:                    #If they select option 1
        L[0] += 10          
        L[1] += 9 
        L[2] += 8

        L[3] += 10
        L[4] += 9
        L[5] += 8
        L[6] += 7

        L[7] += 9
        L[8] += 10

    elif ans == 2:                  #If they select option 2
        L[0] += 10
        L[1] += 9
        L[2] += 8

        L[3] -= 10000
        L[4] -= 10000
        L[5] -= 10000
        L[6] -= 10000

        L[7] += 9
        L[8] += 10

    elif ans == 3:                  #If they select option 3
        L[0] += 10
        L[1] += 9
        L[2] += 8  

        L[3] -= 100
        L[4] -= 100
        L[5] -= 100
        L[6] -= 100

        L[7] += 9
        L[8] += 10

    elif ans == 4:                  #If they select option 4
        L[0] += 10
        L[1] += 9
        L[2] += 8  

        L[3] -= 100
        L[4] -= 100
        L[5] -= 100
        L[6] -= 100

        L[7] += 9
        L[8] += 10

    elif ans == 5:                  #If they select option 5
        L[0] += 10
        L[1] += 9
        L[2] += 8 

        L[3] -= 100
        L[4] -= 100
        L[5] -= 100
        L[6] -= 100

        L[7] += 9
        L[8] += 10

    elif ans == 6:                  #If they select option 
        L[0] += 10
        L[1] += 9
        L[2] += 8 

        L[3] += 10
        L[4] += 9
        L[5] += 8
        L[6] += 7

        L[7] += 9
        L[8] += 10
        
    elif ans == 7:                  #If they select option 5
        L[0] += 10
        L[1] += 9
        L[2] += 8 

        L[3] -= 100
        L[4] -= 100
        L[5] -= 100
        L[6] -= 100

        L[7] += 0
        L[8] += 0

    elif ans == 7:                  #If they select option 5
        L[0] += 10
        L[1] += 9
        L[2] += 8 

        L[3] -= 100
        L[4] -= 100
        L[5] -= 100
        L[6] -= 100

        L[7] += 9
        L[8] += 10

    return L

#2 Budget
def budget(ans):
    if ans == 1:                    #If they select option 1
        L[0] += 5          
        L[1] += 2 
        L[2] += 1  

        L[3] += 5
        L[4] += 3
        L[5] += 2
        L[6] += 1

        L[7] += 1
        L[8] += 5

    elif ans == 2:                  #If they select option 2
        L[0] += 6
        L[1] += 5
        L[2] += 4  

        L[3] += 5
        L[4] += 4
        L[5] += 2
        L[6] += 1

        L[7] += 5
        L[8] += 6

    elif ans == 3:                  #If they select option 3
        L[0] += 6
        L[1] += 5
        L[2] += 4  

        L[3] += 6
        L[4] += 5
        L[5] += 4
        L[6] += 3

        L[7] += 5
        L[8] += 6

    elif ans == 4:                  #If they select option 4
        L[0] += 6
        L[1] += 5
        L[2] += 4  

        L[3] += 6
        L[4] += 5
        L[5] += 4
        L[6] += 3

        L[7] += 5
        L[8] += 6

    elif ans == 5:                  #If they select option 5
        L[0] += 6
        L[1] += 5
        L[2] += 4 

        L[3] += 6
        L[4] += 5
        L[5] += 4
        L[6] += 3

        L[7] += 5
        L[8] += 6

    return L

#3 Kids Content
def kids(ans):         
    if ans == 1:                    
        L[0] += 10        
        L[1] += 9
        L[2] += 8 

        L[3] += 7
        L[4] += 6
        L[5] += 5
        L[6] += 4

        L[7] += 1
        L[8] += 2

    elif ans == 2:                  #If they select option 2
        L[0] += 10
        L[1] += 9
        L[2] += 8

        L[3] += 6
        L[4] += 5
        L[5] += 4
        L[6] += 3

        L[7] += 4
        L[8] += 5

    elif ans == 3:                  #If they select option 3
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
    if ans == 1:                    
        L[0] += 10        
        L[1] += 9
        L[2] += 8 

        L[3] += 0
        L[4] += 0
        L[5] += 0
        L[6] += 0

        L[7] += 3
        L[8] += 4

    elif ans == 2:                  #If they select option 2
        L[0] += 10
        L[1] += 10
        L[2] += 10

        L[3] += 4
        L[4] += 4
        L[5] += 4
        L[6] += 4

        L[7] += 6
        L[8] += 6

    elif ans == 3:                  #If they select option 3
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

#5 of Devices
def simStream(ans):
    if ans == 1:
        L[0] += 10        
        L[1] += 10
        L[2] += 10 

        L[3]+= 10
        L[4]+= 10
        L[5]+= 10
        L[6]+= 10

        L[7]+= 10
        L[8]+= 10


    elif ans == 2:                  #If they select option 2
        L[0] += 0
        L[1] += 10
        L[2] += 10  

        L[3] += 0
        L[4] += 0
        L[5] += 10
        L[6] += 10

        L[7] += 10
        L[8] += 10


    elif ans == 3:                  #If they select option 3
        L[0] += 0
        L[1] += 0
        L[2] += 10

        L[3] += 0
        L[4] += 0
        L[5] += 10
        L[6] += 10

        L[7] += 8
        L[8] += 8


    elif ans == 4:                  #If they select option 4
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
    if ans == 1:                    
        L[0] += 10        
        L[1] += 10
        L[2] += 10 

        L[3] += 10
        L[4] += 10
        L[5] += 10
        L[6] += 10

        L[7] += 7
        L[8] += 7

    elif ans == 2:                  #If they select option 2
        L[0] += 10
        L[1] += 10
        L[2] += 10

        L[3] += 10
        L[4] += 10
        L[5] += 10
        L[6] += 10

        L[7] += 0
        L[8] += 0

    elif ans == 3:                  #If they select option 3
        L[0] += 7
        L[1] += 7
        L[2] += 7  

        L[3] += 10
        L[4] += 10
        L[5] += 10
        L[6] += 10

        L[7] += 0
        L[8] += 0
        
    return L

#7 Foreign Content
def foreign(ans):         #Hulu only in Japan
    if ans == 1:                    #If they select option 1
        L[0] += 10        
        L[1] += 10
        L[2] += 10 

        L[3] += 3
        L[4] += 3
        L[5] += 3
        L[6] += 3

        L[7] += 5
        L[8] += 5

    elif ans == 2:                  #If they select option 2
        L[0] += 10
        L[1] += 10
        L[2] += 10

        L[3] += 6
        L[4] += 6
        L[5] += 6
        L[6] += 6

        L[7] += 8
        L[8] += 8

    elif ans == 3:                  #If they select option 3
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


#8 Video Quality
def quality(ans):         
    if ans == 1:                    
        L[0] += 10        
        L[1] += 10
        L[2] += 10 

        L[3] += 10
        L[4] += 10
        L[5] += 10
        L[6] += 10

        L[7] += 10
        L[8] += 10

    elif ans == 2:                  #If they select option 2
        L[0] += 0
        L[1] += 10
        L[2] += 10

        L[3] += 10
        L[4] += 10
        L[5] += 10
        L[6] += 10

        L[7] += 10
        L[8] += 10

    elif ans == 3:                  #If they select option 3
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
    if ans == 1:                    
        L[0] += 10        
        L[1] += 10
        L[2] += 10 

        L[3] += 4
        L[4] += 4
        L[5] += 4
        L[6] += 4

        L[7] += 6
        L[8] += 6

    elif ans == 2:                  #If they select option 2
        L[0] += 10
        L[1] += 10
        L[2] += 10

        L[3] += 6
        L[4] += 6
        L[5] += 6
        L[6] += 6

        L[7] += 8
        L[8] += 8

    elif ans == 3:                  #If they select option 3
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


#10 Original Content
def originals(ans):

    if ans == 1:
        L[0] += 10       
        L[1] += 10
        L[2] += 10 

        L[3] += 6
        L[4] += 6
        L[5] += 6
        L[6] += 6

        L[7] += 2
        L[8] += 2


    elif ans == 2:                  #If they select option 2
        L[0] += 10
        L[1] += 10
        L[2] += 10

        L[3] += 8
        L[4] += 8
        L[5] += 8
        L[6] += 8

        L[7] += 5
        L[8] += 5


    elif ans == 3:                  #If they select option 3
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
    
def graph():

    objects = ('netflixBasic', 'netflixStandard', 'netflixPremium', 'huluBasic', 'huluBasicNoAds', 'huluBasicScreens', 'huluBasicScreensNoAds', 'aPrime', 'aPrimeStudent')
    x = np.arange(len(objects))
    performance = L

    plt.bar(x, performance, align='center', alpha=.5, color='midnightblue')
    plt.xticks(x, objects, size=8)
    plt.ylabel('Fit')
    plt.title('Best fit streaming service')
    plt.show()

def max():
    """ Provides the position of the maximum value of L,
    which gives us the streaming service with the highest points,
    ergo, the best fit.
    """
    ind_max=np.argmax(L)
    return ind_max