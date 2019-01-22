# HaEW
Python script to calculate Halpha equivalent widths from photometry.
To run, place the script eq.py in the appropriate folder and compile. The script is run via a simple command haew. If you require to compute the errors on the haew, please contact me. Please note that the script is only applicable to VPHAS+ filter set in Vegamag. If you need to compute line widths for stars beyond spectral type M2, please contact me. 

haew(ri, rha, Av)

    Compute the photometric Halpha equivalent width given photometric colours in VPHAS+ riHa filter set.

    Returns the computed photometric Halpha equivalent width.
    
    Parameters
    ----------
    ri  : r-i photometric colour
    rha : r-Ha photometric colour
    Av  : Absolute value of extinction, where Av = 3.1 * E(B-V). 
        
    Returns
    -------
    eq : photometric Halpha equivalent width
   
    Examples
    --------
    >>> haew(0.336,1.023,1) # Halpha equivalent width for an e.g. star with (r-i)=0.336, (r-Ha)=1.023, and an Av=1 with a reddening        law of Rv=3.1, Note that the ri, rha, Av and can also be inputed as equal length arrays. 
    >>> -140.1414661467111 # Returned Halpha equivalent width

    
    References
    ----------
    If you use this in your research, please cite Kalari et al. (2015) MNRAS, 453. 1026K for the stellar models, and Kalari (2019)  
    MNRAS accepted for the code. 
