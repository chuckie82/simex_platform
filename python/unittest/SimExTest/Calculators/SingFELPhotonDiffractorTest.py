""" Test module for the SingFELPhotonDiffractor.

    @author : CFG
    @institution : XFEL
    @creation 20151109

"""
import os
import subprocess

import paths
import unittest


# Import the class to test.
from SimEx.Calculators.SingFELPhotonDiffractor import SingFELPhotonDiffractor
from TestUtilities import TestUtilities

class SingFELPhotonDiffractorTest(unittest.TestCase):
    """
    Test class for the SingFELPhotonDiffractor class.
    """

    @classmethod
    def setUpClass(cls):
        """ Setting up the test class. """
        cls.input_h5 = TestUtilities.generateTestFilePath('pmi_out_0000001.h5')

    @classmethod
    def tearDownClass(cls):
        """ Tearing down the test class. """
        del cls.input_h5

    def setUp(self):
        """ Setting up a test. """
        self.__files_to_remove = []
        self.__dirs_to_remove = []

    def tearDown(self):
        """ Tearing down a test. """
        for f in self.__files_to_remove:
            if os.path.isfile(f):
                os.remove(f)
        for d in self.__dirs_to_remove:
            if os.path.isdir(d):
                os.rmdir(d)

    def testConstruction(self):
        """ Testing the default construction of the class. """

        parameters={ 'number_of_uniform_rotations': 1,
                     'calculate_Compton' : False,
                     'slice_interval' : 100,
                     'number_of_slices' : 2,
                     'pmi_start_ID' : 1,
                     'pmi_stop_ID'  : 1,
                     'number_of_diffraction_patterns' : 2,
                     'beam_parameter_file' : TestUtilities.generateTestFilePath('s2e.beam'),
                     'beam_geometry_file' : TestUtilities.generateTestFilePath('s2e.geom'),
                   }

        # Construct the object.
        diffractor = SingFELPhotonDiffractor(parameters=parameters, input_path=self.input_h5, output_path='diffr_out.h5')

        self.assertIsInstance(diffractor, SingFELPhotonDiffractor)

    def testBackengine(self):
        """ Test that we can start a test calculation. """

        parameters={ 'number_of_uniform_rotations': 1,
                     'calculate_Compton' : False,
                     'slice_interval' : 100,
                     'number_of_slices' : 2,
                     'pmi_start_ID' : 1,
                     'pmi_stop_ID'  : 1,
                     'number_of_diffraction_patterns' : 2,
                     'beam_parameter_file' : TestUtilities.generateTestFilePath('s2e.beam'),
                     'beam_geometry_file' : TestUtilities.generateTestFilePath('s2e.geom'),
                     }

        # Construct the object.
        diffractor = SingFELPhotonDiffractor(parameters=parameters, input_path=self.input_h5, output_path='diffr_out.h5')

        # Call backengine.
        status = diffractor.backengine()

        # Check successful completion.
        self.assertEqual(status, 0)

        # Cleanup.
        self.__files_to_remove.append('prepHDF5.py')
        self.__files_to_remove.append('prepHDF5.pyc')
        self.__files_to_remove.append('diffr_out_0000001.h5')
        self.__files_to_remove.append('diffr_out_0000002.h5')
        self.__files_to_remove.append(os.path.join('pmi', 'pmi_out_0000001.h5'))
        self.__dirs_to_remove.append('pmi')

    def testBackenginePMIDirExistsEmpty(self):
        """ Test that we can start a test calculation if the pmi dir already exists and is empty. """

        # Create the pmi dir.
        os.mkdir('pmi')

        parameters={ 'number_of_uniform_rotations': 1,
                     'calculate_Compton' : False,
                     'slice_interval' : 100,
                     'number_of_slices' : 2,
                     'pmi_start_ID' : 1,
                     'pmi_stop_ID'  : 1,
                     'number_of_diffraction_patterns' : 2,
                     'beam_parameter_file' : TestUtilities.generateTestFilePath('s2e.beam'),
                     'beam_geometry_file' : TestUtilities.generateTestFilePath('s2e.geom'),
                     }

        # Construct the object.
        diffractor = SingFELPhotonDiffractor(parameters=parameters, input_path=self.input_h5, output_path='diffr_out.h5')

        # Call backengine.
        status = diffractor.backengine()

        # Check successful completion.
        self.assertEqual(status, 0)

        # Cleanup.
        self.__files_to_remove.append('prepHDF5.py')
        self.__files_to_remove.append('prepHDF5.pyc')
        self.__files_to_remove.append('diffr_out_0000001.h5')
        self.__files_to_remove.append('diffr_out_0000002.h5')
        self.__files_to_remove.append(os.path.join('pmi', 'pmi_out_0000001.h5'))
        self.__dirs_to_remove.append('pmi')

    def testBackenginePMIDirExistsNonEmpty(self):
        """ Test that we can start a test calculation if the pmi dir already exists and is not empty. """

        # Create the pmi dir.
        os.mkdir('pmi')
        ln_pmi_command = 'ln -s %s %s' % ( self.input_h5, 'pmi/')
        proc = subprocess.Popen(ln_pmi_command, shell=True)
        proc.wait()

        parameters={ 'number_of_uniform_rotations': 1,
                     'calculate_Compton' : False,
                     'slice_interval' : 100,
                     'number_of_slices' : 2,
                     'pmi_start_ID' : 1,
                     'pmi_stop_ID'  : 1,
                     'number_of_diffraction_patterns' : 2,
                     'beam_parameter_file' : TestUtilities.generateTestFilePath('s2e.beam'),
                     'beam_geometry_file' : TestUtilities.generateTestFilePath('s2e.geom'),
                     }

        # Construct the object.
        diffractor = SingFELPhotonDiffractor(parameters=parameters, input_path=self.input_h5, output_path='diffr_out.h5')

        # Call backengine.
        status = diffractor.backengine()

        # Check successful completion.
        self.assertEqual(status, 0)

        # Cleanup.
        self.__files_to_remove.append('prepHDF5.py')
        self.__files_to_remove.append('prepHDF5.pyc')
        self.__files_to_remove.append('diffr_out_0000001.h5')
        self.__files_to_remove.append('diffr_out_0000002.h5')
        self.__files_to_remove.append(os.path.join('pmi', 'pmi_out_0000001.h5'))
        self.__dirs_to_remove.append('pmi')

    def testRunWithParameters(self):
        """ Check we can run the backengine with a given parameter set. """

        parameters={ 'number_of_uniform_rotations': 1,
                     'calculate_Compton' : False,
                     'slice_interval' : 100,
                     'number_of_slices' : 2,
                     'pmi_start_ID' : 1,
                     'pmi_stop_ID'  : 1,
                     'number_of_diffraction_patterns' : 2,
                     'beam_parameter_file' : TestUtilities.generateTestFilePath('s2e.beam'),
                     'beam_geometry_file' : TestUtilities.generateTestFilePath('s2e.geom'),
                     }

        # Construct the object.
        diffractor = SingFELPhotonDiffractor(parameters=parameters, input_path=self.input_h5, output_path='diffr_out.h5')

        # Call backengine.
        status = diffractor.backengine()

        self.assertEqual(status, 0)





if __name__ == '__main__':
    unittest.main()

