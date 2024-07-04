import numpy as np

def Damping_ratio(eigenvalue:complex) -> float:

    '''
    Function to calculate the Damping ratio of the given eigenvalue

    Input: Individual complex eigenvalue

    Output: Damping ratio of the given eigenvalue
    
    '''	

    real = np.real(eigenvalue)
    img = np.imag(eigenvalue)
    
    chi = -real/np.sqrt(real**2 + img**2)

    return chi



def filter_positive_imaginary_part(eigenvalues):

    '''
    Function to filter positive imaginary part of the eigenvalues

    Input: Array of eigenvalues

    Output: Array of eigenvalues with positive imaginary part
    
    '''	

    filtered_eigenvalues = [eig_val for eig_val in eigenvalues if eig_val.imag > 0 and eig_val.imag <= 70 and eig_val.real >= -15]
    
    return filtered_eigenvalues