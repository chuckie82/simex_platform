INCLUDE(ExternalProject)

include(FindPythonModules)
find_python_module(Cython.Distutils REQUIRED)
find_python_module(numpy REQUIRED)
find_python_module(h5py REQUIRED)

INCLUDE(ExternalProject)
ExternalProject_Add(
recon_emc    
#URL https://db.tt/8CTthFkw
DOWNLOAD_COMMAND wget https://db.tt/8CTthFkw -O recon.tar.gz && tar xf recon.tar.gz && rm -rf recon_emc && mv s2e_recon recon_emc
#DOWNLOAD_NAME recon.tar.gz
PATCH_COMMAND ""
CONFIGURE_COMMAND ""
CMAKE_COMMAND ""
BUILD_IN_SOURCE 1
BUILD_COMMAND  bash -c "cd EMC_Src && ./compile_EMC"
INSTALL_COMMAND ""
)
           

ExternalProject_Get_Property(recon_emc SOURCE_DIR)
set (EMC_SOURCE_DIR ${SOURCE_DIR}/EMC_Src)

         
install(PROGRAMS ${EMC_SOURCE_DIR}/EMC DESTINATION ${BINDIR})   

install(DIRECTORY ${EMC_SOURCE_DIR}/quaternions
        DESTINATION ${CALCULATORS_DIR}/CalculatorUtilities
        )

install(FILES ${EMC_SOURCE_DIR}/runEMC.py DESTINATION  ${PYPATH})

  
install(DIRECTORY ${EMC_SOURCE_DIR}/supp_py_modules DESTINATION ${PYPATH}
                                        FILES_MATCHING
                                        PATTERN "*.py"
                                        PATTERN "*.so"                                        
                                        PATTERN "build" EXCLUDE
                                        PATTERN ".*" EXCLUDE
                                        )

           