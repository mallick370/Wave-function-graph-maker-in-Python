# -*- coding: utf-8 -*-

"""
Created on Fri Feb  8 22:29:41 2019

@author: KIIT
"""

import quantumWellEnergy
import EnergyQuantum
import pyttsx3

if __name__ == '__main__':
    tts = pyttsx3.init()
    c="y"
    while(c=="y" or c=="Y"):
        tts.say("Press 1 to have graphs of wave function and probability density function of a particular quantum number\nPress 2 to know possible transitions of electrons from different band levels\n")
        tts.runAndWait()
        n=int(input("Enter your choice\nPress 1 to have graphs of wave function and probability density function of a particular quantum number\nPress 2 to know possible transitions of electrons from different band levels\n"))
        if(n==1):
            #quantumWellEnergy
            tts.say("Enter the value of principle quantum number\n")
            tts.runAndWait()
            n=int(input("Enter the value of principal quantum number\n"))
            tts.say("Enter the length of the quantum box or of the well in nanometers\n")
            tts.runAndWait()
            a=float(input("Enter the asked value\n"))
            quantumWellEnergy.plots(n,a)
            quantumWellEnergy.wavePlot(n,a)
            quantumWellEnergy.probabilityPlot(n,a)
            k=a*(10**(-9))#converting nanometer to meters
            quantumWellEnergy.energy(n,k)

        elif(n==2):
            tts.say("Enter the value of principal quantum number till where wavelengths are to be calculated\n")
            tts.runAndWait()
            n=int(input("Enter the asked value\nEnter the value of principal quantum number till where wavelengths are to be calculated\n"))
            tts.say("Enter the length of the quantum box or of the well in nanometers\n")
            tts.runAndWait()
            a=float(input("Enter the asked value\n"))
            EnergyQuantum.transitions(n,a)
        
        tts.say("Press y to continue or Press n to terminate\n")
        tts.runAndWait()
        c=input("Enter the choice\n")
    tts.say("It was Great to help you . will surely be happy to serve you again")
    tts.runAndWait()