import radical.pilot as rp

## Hard coded path for gromacs --- Can be removed if the variable $PATH is modfiied for the purpose
### MUST BE SET IF THE FOLDER IS NOT ACCESSIBLE 
PATH="/lustre/atlas/scratch/aleang9/csc108/gromacs/bin/"

def createCU(cores):
	'''
	Example -- Creation of a CU descriptor for running gromacs.
	'''
	cu = rp.ComputeUnitDescription() # Create a new CU descriptor
	# Set pre-execution commands
	cu.pre_exec=["module load boost","module load fftw","module load cudatoolkit","module use --append /lustre/atlas/world-shared/bip103/modules","module load openmpi/STATIC"]
	# set  the command to run
	cu.executable=[PATH+"gmx_mpi"] 
	# set the arguments for the executable
	cu.arguments=["mdrun","-ntomp",str(cores), "-nb", "cpu","-s","topol.tpr","-c","out.gro"]
	# Stage the input files
	cu.input_staging = ["topol.tpr"]
	# Set open-mpi
	cu.mpi = True
	# Set the number of cores
	cu.cores=cores
	return cu 
