from pylab import *
from scipy.optimize import curve_fit

def peak_fit(data,guess):
    
    #y,x = np.histogram(data,bins)

    #x=(x[1:]+x[:-1])/2 # for len(x)==len(y)

    def gaus(x,a,x0,sigma):
        return a*np.exp(-(x-x0)**2/(2*sigma**2))

    #def bimodal(x,mu1,sigma1,A1,mu2,sigma2,A2):
       # return gauss(x,mu1,sigma1,A1)+gauss(x,mu2,sigma2,A2)
        
        
    n,nx = np.histogram(data,normed = True,range=(1350,1500))

    xc = (nx[:-1] + nx[1:]) / 2


    popt,pcov = curve_fit(gaus,xc,n,p0=guess)
    
    print(popt)
    print(pcov)
    
    plt.plot(xc,gaus(xc,*popt),color='red',lw=3,label='model')
    plt.xscale('log')

    