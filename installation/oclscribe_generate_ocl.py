#===== start the modelioscribes framework ==========================================
import os 
WORKSPACE_DIRECTORY=Modelio.getInstance().getContext().getWorkspacePath().toString()
execfile(os.path.join(WORKSPACE_DIRECTORY,'macros','modelioscribes_startup.py'))
#===================================================================================

scribeStartup('OCLScribe',"do_generate_ocl",selectedElements,True)
    



