# Abaqus-J-integral
This repository uses python and the Abaqus odb API to calculate the J-integral for specific 3D problems. To do this, shape functions and integration procedures are implemented for the C3D20 element.

# Example 1 - J integral for through thickness crack in infinite plate 
This simple example is used to verify the implementation of the J-integral

# Example 2 - J integral for compact test specimen with interface 
The results of (Simha, N.K. et al 2005) are reproduced. Mainly, the material force in the interface is extracted and the J-integral is corrected to retain path independence. 

# Example 3 - J integral for three point bend specimen with high density of interfaces
Similar to Example 2, but with the addition of many interfaces.

# Documentation 
All theory and examples are presented in the [Summary](https://github.com/djm87/Abaqus-J-integral/blob/master/Documentation/Summary.pdf) document.

For the literature referenced in the summary document see the [Documentation](https://github.com/djm87/Abaqus-J-integral/tree/master/Documentation) folder.
