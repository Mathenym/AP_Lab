import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from scipy.optimize import curve_fit

def hist_uncal(data,bin):
    
    xmin=min(data)
    xmax=max(data)

    fig,axes = plt.subplots(1,1,figsize=(9.0,8.0),sharex=True)
    ax1 = axes
    
    ax1.hist(data,bins = bin,histtype = "step",color ='blue',label = 'Data',linewidth="2")
    
    print(max(data),min(data))   
   
    ax1.set_xlabel('ADC Channel',size = '20')
    ax1.set_ylabel('Count',size = '20')
    ax1.set_title('Uncalibrated',size ='20')
    ax1.set_xlim([0,800]) 
    ax1.set_yscale('log')
    ax1.grid(True)
    ax1.yaxis.grid(True,which='minor',linestyle='--')
    ax1.legend(loc=1,prop={'size':18})
    ax1.tick_params(axis='both', labelsize = '15')
    #plt.savefig('Figures/background_det01994.png')

    plt.show()
    
    
def hist_cal(data,bin):
    
    xmin=min(data)
    xmax=max(data)

    fig,axes = plt.subplots(1,1,figsize=(9.0,8.0),sharex=True)
    ax1 = axes
    
    ax1.hist(data,bins = bin, histtype = "step",color ='blue',label = 'Data',linewidth="2")
    
    print(max(data),min(data))   
    
    #Where sodium peaks should be: 
    plt.axvline(x=511,color='k', linestyle='--')
    plt.axvline(x=1274,color='k', linestyle='--')
    plt.axvline(x=1785,color='k', linestyle='--')
    plt.axvline(x=2614,color='k', linestyle='--')

    
    ax1.set_xlabel('Energy [keV]',size = '20')
    ax1.set_ylabel('Count',size = '20')
    ax1.set_title('Calibrated',size ='20')
    ax1.set_xlim([0,3000]) 
    ax1.set_yscale('log')
    ax1.grid(True)
    ax1.yaxis.grid(True,which='minor',linestyle='--')
    ax1.legend(loc=1,prop={'size':18})
    ax1.tick_params(axis='both', labelsize = '15')
    #plt.savefig('Figures/background_det01994.png')

    plt.show()
    