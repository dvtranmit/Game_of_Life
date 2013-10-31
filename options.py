##
# @file options.py
# @modeled after openmoc.options
# 
# @authors Jasmeet Arora (jasmeet@mit.edu) 
#          Stephanie Pavlick (spavlick@mit.edu)
#          Davis Tran (dvtran@mit.edu)

# @date November 1, 2013


import getopt, sys

from datetime import datetime #imports date and time getter for default file naming

class options:

    #default x dimension
    numx = 20
    
    #default y dimension
    numy = 20

    #default number of timesteps
    numsteps = 10
   
    #default time to sleep (in seconds)
    numsleep = .5

    #default file name
    outputfile = "gol_data_%s.hdf5" %(str(datetime.now()).replace(" ", "_"))

    #default input file
    inputfile = ""






    def parseArguments(self):    #definiing the method parseArguments

        try:
            opts, args = getopt.getopt(sys.argv[1:], 
                                       'hx:y:t:s:f:i:', #each letter represents
                                       ['help',         #optional user
                                        'numx=',        #command line inputs
                                        'numy=',
                                        'numsteps=',
                                        'numsleep=',
                                        'outputfile='
                                        'inputfile='])

        except getopt.GetoptError as err:   #if user enters invalid command,
            print ('WARNING'+ str(err))     #error message is printed and 'pass'
            pass                            #allows the program to run on defaults

        # Parse the command line arguments
        for opt, arg in opts:

            # Print a report of all supported runtime options and exit
            if opt in ('-h', '--help'):

                print '{:-^80}'.format('')
                print '{: ^80}'.format('Game of Life v.1.0.0 runtime options')
                print '{:-^80}'.format('')
                print

                categories = '  {: <16}'.format('[command]')
                categories += '\t{: <18}'.format('[default]')
                categories += '[description]'
                print categories
                print

                help = '  {: <40}'.format('-h, --help')
                help += 'Report Game of Life runtime options\n'
                print help              
 
                numx = '  {: <14}'.format('-x, --numx')
                numx += '\t{: <18}'.format('20')
                numx += 'x-dimension of board\n'
                print numx

                numy = '  {: <14}'.format('-y, --numx')
                numy += '\t{: <18}'.format('20')
                numy += 'y-dimension of board\n'
                print numy

                numsteps = '  {: <10}'.format('-t, --numsteps')
                numsteps += '\t{: <18}'.format('10')
                numsteps += 'Number of timesteps\n'
                print numsteps

                numsleep = '  {: <10}'.format('-s, --numsleep')
                numsleep += '\t{: <18}'.format('0.5')
                numsleep += 'Sleep time of each timestep\n'
                print numsleep

                outputfile = '  {: <10}'.format('-f, --outputfile')
                outputfile += '\t{: <18}'.format('gol_data_datetime')
                outputfile += 'Names data file for simulation\n'
                print outputfile

                inputfile = '  {: <12}'.format('-i, --inputfile')
                inputfile += '\t{: <18}'.format('')
                inputfile += 'Runs game with existing file\n'
                print inputfile

                sys.exit()

            elif opt in ('-x', '--numx'):
                self.numx = int(arg)

            elif opt in ('-y', '--numy'):
                self.numy = int(arg)

            elif opt in ('-t', '--numsteps'):
                self.numsteps = int(arg)

            elif opt in ('-s', '--numsleep'):
                self.numsleep = float(arg)

            elif opt in ('-f', '--outputfile'):
                self.outputfile = str(arg) + ".hdf5"

            elif opt in ('-i', '--inputfile'):
                self.inputfile = str(arg)

           
            
