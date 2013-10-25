##
# @file options.py
# @package openmoc.options
# @brief
# 
# @author William Boyd (wboyd@mit.edu)
# @date July 24, 2013


import getopt, sys

from datetime import datetime

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
    outputfile = "gol_data_%s.hdf5" %(datetime.now())






    def parseArguments(self):

        try:
            opts, args = getopt.getopt(sys.argv[1:], 
                                       'hx:y:t:s:f:',
                                       ['help',
                                        'numx=',
                                        'numy=',
                                        'numsteps=',
                                        'numsleep=',
                                        'outputfile='])

        except getopt.GetoptError as err:
            print ('WARNING'+ str(err))
            pass

        # Parse the command line arguments - error checking will occur
        # at the setter method level in C++
        for opt, arg in opts:

            # Print a report of all supported runtime options and exit
            if opt in ('-h', '--help'):

                print '{:-^80}'.format('')
                print '{: ^80}'.format('OpenMOC v.0.1.1 runtime options')
                print '{:-^80}'.format('')
                print

                help = '\t{: <35}'.format('-h, --help')
                help += 'Report OpenMOC runtime options\n'
                print help

                num_azim = '\t{: <35}'.format('-a, --num-azim=<4>')
                num_azim += 'the number of azimuthal angles\n'
                print num_azim

                track_spacing = '\t{: <35}'.format('-s, --track-spacing=<0.1>')
                track_spacing += 'The track spacing [cm]\n'
                print track_spacing

                max_iters = '\t{: <35}'.format('-i, --max-iters=<1000>')
                max_iters += 'The max number of source iterations\n'
                print max_iters

                tolerance = '\t{: <35}'.format('-c, --tolerance=<1E-5>')
                tolerance += 'The source convergence tolerance\n'
                print tolerance

                num_omp_threads = '\t{: <35}'.format('-t, --num-omp-threads=<1>')
                num_omp_threads += 'The number of OpenMP threads\n'
                print num_omp_threads

                num_gpu_threadblocks = '\t{: <35}'.format('-b, --num-gpu-threadblocks=<64>')
                num_gpu_threadblocks += 'The number of GPU threadblocks\n'
                print num_gpu_threadblocks

                num_gpu_threads = '\t{: <35}'.format('-g, --num-gpu-threads=<64>')
                num_gpu_threads += 'The number of GPU threads per block\n'
                print num_gpu_threads

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
                self.outputfile = str(arg)

           
            
