# ajplanet

This repository contains a number of C codes that are useful for exoplanet work. In particular, here 
you will find codes to:

    - Model transit lightcurves.
    - Model radial velocities. 

It also contains a Pyhton directory that interfaces the C functions so that they can be called from 
Python (see below).

Compiling the C code
---------------------

To compile the C code edit the Makefile and do:

    'make'

Calling the module from Python
------------------------------

To call the module from Python, go to the `Python` folder in this module and do:

    `python setup.py build`

This will generate a `build` folder. Inside the folder, another folder 
will be created which starts with `lib.`, inside of which you will find 
the `ajplanet.so` file which is callable from Python. You can then issue:

    `python setup.py install`

or manually move that  file to a folder with your code and import it directly 
by doing `import ajplanet`, and use the functions inside the module.

You can compile and install ajplanet automatically by copying the following lines.

    git clone https://github.com/andres-jordan/ajplanet.git
    cd ajplanet
    make
    cd Python
    python setup.py build
    python setup.py install
    cd ../../
   
Modelling Radial Velocities with ajplanet
-----------------------------------------

The modelling of Radial Velocities is very simple. Just call the code from 
Python by doing:

   `ajplanet.pl_rv_array(times,gamma,K,omega,ecc,t0,P)`

Where `times` is an array of times, `gamma` is the center-of-mass velocity, 
`K` is the semi-amplitude, `omega` is the argument of periapsis (in radians), 
`ecc` is the eccentricity of the orbit, `t0` is the time of transit center and `P`
is the period of the orbit. This will return radial velocities at the input 
times with the same units as `K`.

