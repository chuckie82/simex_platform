##########################################################################
#                                                                        #
# Copyright (C) 2015, 2016 Carsten Fortmann-Grote                        #
# Contact: Carsten Fortmann-Grote <carsten.grote@xfel.eu>                #
#                                                                        #
# This file is part of simex_platform.                                   #
# simex_platform is free software: you can redistribute it and/or modify #
# it under the terms of the GNU General Public License as published by   #
# the Free Software Foundation, either version 3 of the License, or      #
# (at your option) any later version.                                    #
#                                                                        #
# simex_platform is distributed in the hope that it will be useful,      #
# but WITHOUT ANY WARRANTY; without even the implied warranty of         #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
# GNU General Public License for more details.                           #
#                                                                        #
# You should have received a copy of the GNU General Public License      #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.  #
#                                                                        #
##########################################################################

""" Test module for the FEFFPhotonMatterInteractor.

    @author : CFG
    @institution : XFEL
    @creation 20161011

"""
import h5py
import os
import paths
import shutil
import unittest

import StringIO

# Import the class to test.
from SimEx.Calculators.AbstractPhotonInteractor import AbstractPhotonInteractor
from SimEx.Calculators.FEFFPhotonMatterInteractor import FEFFPhotonMatterInteractor
from SimEx.Calculators.FEFFPhotonMatterInteractor import FEFFPhotonMatterInteractorParameters
from SimEx.Calculators.FEFFPhotonMatterInteractor import _checkAndSetAmplitudeReductionFactor
from SimEx.Calculators.FEFFPhotonMatterInteractor import _checkAndSetAtoms
from SimEx.Calculators.FEFFPhotonMatterInteractor import _checkAndSetEdge
from SimEx.Calculators.FEFFPhotonMatterInteractor import _checkAndSetEffectivePathDistance
from SimEx.Calculators.FEFFPhotonMatterInteractor import _checkAndSetPotentials
from SimEx.Parameters.AbstractCalculatorParameters import AbstractCalculatorParameters

from TestUtilities import TestUtilities

class FEFFPhotonMatterInteractorTest(unittest.TestCase):
    """
    Test class for the FEFFPhotonMatterInteractor class.
    """

    @classmethod
    def setUpClass(cls):
        """ Setting up the test class. """

    @classmethod
    def tearDownClass(cls):
        """ Tearing down the test class. """

    def setUp(self):
        """ Setting up a test. """
        self.__files_to_remove = []
        self.__dirs_to_remove = []

    def tearDown(self):
        """ Tearing down a test. """
        # Clean up.
        for f in self.__files_to_remove:
            if os.path.isfile(f):
                os.remove(f)
        for p in self.__dirs_to_remove:
            if os.path.isdir(p):
                shutil.rmtree(p)

    def testShapedConstruction(self):
        """ Testing the construction of the class with parameters. """
        self.assertTrue( False )

    def testDefaultConstruction(self):
        """ Testing the default construction of the class. """

        feff = FEFFPhotonMatterInteractor()

        self.assertIsInstance( feff, AbstractPhotonInteractor )


class FEFFPhotonMatterInteractorParametersTest(unittest.TestCase):
    """ Test class for the FEFFPhotonMatterInteractorParameters class. """

    @classmethod
    def setUpClass(cls):
        """ Setting up the test class. """

    @classmethod
    def tearDownClass(cls):
        """ Tearing down the test class. """

    def setUp(self):
        """ Setting up a test. """
        self.__files_to_remove = []
        self.__dirs_to_remove = []

        self.__atoms = (
                 [[ 0.00000,     0.00000,     0.00000], 'Cu',   0],
                 [[ 0.00000,     1.80500,    -1.80500], 'Cu',   1],
                 [[-1.80500,    -1.80500,     0.00000], 'Cu',   1],
                 [[ 1.80500,     0.00000,    -1.80500], 'Cu',   1],
                 [[ 0.00000,    -1.80500,     1.80500], 'Cu',   1],
                 [[ 1.80500,     1.80500,     0.00000], 'Cu',   1],
                 [[ 0.00000,    -1.80500,    -1.80500], 'Cu',   1],
                 [[-1.80500,     1.80500,     0.00000], 'Cu',   1],
                 [[ 0.00000,     1.80500,     1.80500], 'Cu',   1],
                 [[-1.80500,     0.00000,    -1.80500], 'Cu',   1],
                 [[-1.80500,     0.00000,     1.80500], 'Cu',   1],
                 [[ 1.80500,     0.00000,     1.80500], 'Cu',   1],
                 [[ 1.80500,    -1.80500,     0.00000], 'Cu',   1],
                 [[ 0.00000,    -3.61000,     0.00000], 'Cu',   1],
                 [[ 0.00000,     0.00000,    -3.61000], 'Cu',   1],
                 [[ 0.00000,     0.00000,     3.61000], 'Cu',   1],
                 [[-3.61000,     0.00000,     0.00000], 'Cu',   1],
                 [[ 3.61000,     0.00000,     0.00000], 'Cu',   1],
                 [[ 0.00000,     3.61000,     0.00000], 'Cu',   1],
                 [[-1.80500,     3.61000,     1.80500], 'Cu',   1],
                 [[ 1.80500,     3.61000,     1.80500], 'Cu',   1],
                 [[-1.80500,    -3.61000,    -1.80500], 'Cu',   1],
                 [[-1.80500,     3.61000,    -1.80500], 'Cu',   1],
                 [[ 1.80500,     3.61000,    -1.80500], 'Cu',   1],
                 [[-1.80500,    -3.61000,     1.80500], 'Cu',   1],
                 [[-3.61000,     1.80500,    -1.80500], 'Cu',   1],
                 [[ 1.80500,    -3.61000,     1.80500], 'Cu',   1],
                 [[ 3.61000,     1.80500,    -1.80500], 'Cu',   1],
                 [[-3.61000,     1.80500,     1.80500], 'Cu',   1],
                 [[-3.61000,    -1.80500,    -1.80500], 'Cu',   1],
                 [[ 3.61000,    -1.80500,     1.80500], 'Cu',   1],
                 [[ 1.80500,    -3.61000,    -1.80500], 'Cu',   1],
                 [[-3.61000,    -1.80500,     1.80500], 'Cu',   1],
                 [[ 3.61000,     1.80500,     1.80500], 'Cu',   1],
                 [[-1.80500,    -1.80500,     3.61000], 'Cu',   1],
                 [[-1.80500,    -1.80500,    -3.61000], 'Cu',   1],
                 [[ 1.80500,     1.80500,    -3.61000], 'Cu',   1],
                 [[ 1.80500,    -1.80500,    -3.61000], 'Cu',   1],
                 [[ 1.80500,    -1.80500,     3.61000], 'Cu',   1],
                 [[-1.80500,     1.80500,    -3.61000], 'Cu',   1],
                 [[-1.80500,     1.80500,     3.61000], 'Cu',   1],
                 [[ 1.80500,     1.80500,     3.61000], 'Cu',   1],
                 [[ 3.61000,    -1.80500,    -1.80500], 'Cu',   1],
                 [[ 3.61000,    -3.61000,     0.00000], 'Cu',   1],
                 [[ 3.61000,     0.00000,    -3.61000], 'Cu',   1],
                 [[ 3.61000,     0.00000,     3.61000], 'Cu',   1],
                 [[-3.61000,     3.61000,     0.00000], 'Cu',   1],
                 [[ 0.00000,     3.61000,     3.61000], 'Cu',   1],
                 [[-3.61000,     0.00000,     3.61000], 'Cu',   1],
                 [[-3.61000,    -3.61000,     0.00000], 'Cu',   1],
                 [[ 0.00000,    -3.61000,     3.61000], 'Cu',   1],
                 [[-3.61000,     0.00000,    -3.61000], 'Cu',   1],
                 [[ 3.61000,     3.61000,     0.00000], 'Cu',   1],
                 [[ 0.00000,    -3.61000,    -3.61000], 'Cu',   1],
                 [[ 0.00000,     3.61000,    -3.61000], 'Cu',   1],
                 [[ 0.00000,    -5.41500,     1.80500], 'Cu',   1],
                 [[ 1.80500,    -5.41500,     0.00000], 'Cu',   1],
                 [[ 0.00000,    -5.41500,    -1.80500], 'Cu',   1],
                 [[-1.80500,     0.00000,     5.41500], 'Cu',   1],
                 [[-5.41500,     0.00000,    -1.80500], 'Cu',   1],
                 [[ 5.41500,    -1.80500,     0.00000], 'Cu',   1],
                 [[-1.80500,     5.41500,     0.00000], 'Cu',   1],
                 [[ 5.41500,     0.00000,    -1.80500], 'Cu',   1],
                 [[-5.41500,    -1.80500,     0.00000], 'Cu',   1],
                 [[ 1.80500,     5.41500,     0.00000], 'Cu',   1],
                 [[ 5.41500,     1.80500,     0.00000], 'Cu',   1],
                 [[ 0.00000,     5.41500,    -1.80500], 'Cu',   1],
                 [[ 0.00000,    -1.80500,    -5.41500], 'Cu',   1],
                 [[ 0.00000,     5.41500,     1.80500], 'Cu',   1],
                 [[ 1.80500,     0.00000,     5.41500], 'Cu',   1],
                 [[ 0.00000,     1.80500,     5.41500], 'Cu',   1],
                 [[ 5.41500,     0.00000,     1.80500], 'Cu',   1],
                 [[ 1.80500,     0.00000,    -5.41500], 'Cu',   1],
                 [[ 0.00000,     1.80500,    -5.41500], 'Cu',   1],
                 [[ 0.00000,    -1.80500,     5.41500], 'Cu',   1],
                 [[-5.41500,     0.00000,     1.80500], 'Cu',   1],
                 [[-5.41500,     1.80500,     0.00000], 'Cu',   1],
                 [[-1.80500,     0.00000,    -5.41500], 'Cu',   1],
                 [[-1.80500,    -5.41500,     0.00000], 'Cu',   1],
                 )

        self.__potentials = None
        self.__edge = 'K'
        self.__amplitude_reduction_factor = 0.9
        self.__effective_path_distance = 5.5

    def tearDown(self):
        """ Tearing down a test. """
        # Clean up.
        for f in self.__files_to_remove:
            if os.path.isfile(f):
                os.remove(f)
        for p in self.__dirs_to_remove:
            if os.path.isdir(p):
                shutil.rmtree(p)

    def testShapedConstruction(self):
        """ Testing the construction of the class with parameters. """


        feff_parameters = FEFFPhotonMatterInteractorParameters(
                atoms=self.__atoms,
                potentials=self.__potentials,
                edge=self.__edge,
                effective_path_distance=self.__effective_path_distance,
                amplitude_reduction_factor=self.__amplitude_reduction_factor)

        self.assertIsInstance( feff_parameters, FEFFPhotonMatterInteractorParameters )

        # Check attributes
        self.assertEqual( feff_parameters._FEFFPhotonMatterInteractorParameters__atoms, self.__atoms)
        self.assertEqual( feff_parameters._FEFFPhotonMatterInteractorParameters__potentials, self.__potentials)
        self.assertEqual( feff_parameters._FEFFPhotonMatterInteractorParameters__edge, self.__edge)
        self.assertEqual( feff_parameters._FEFFPhotonMatterInteractorParameters__amplitude_reduction_factor, self.__amplitude_reduction_factor)
        self.assertEqual( feff_parameters._FEFFPhotonMatterInteractorParameters__effective_path_distance, self.__effective_path_distance)

    def testDefaultConstruction(self):
        """ Testing the default construction of the class. """

        feff = FEFFPhotonMatterInteractorParameters()

        self.assertIsInstance( feff, AbstractCalculatorParameters )

    def testQueries(self):
        """ Test that all queries return the correct value. """

        feff_parameters = FEFFPhotonMatterInteractorParameters(
                atoms=self.__atoms,
                potentials=self.__potentials,
                edge=self.__edge,
                effective_path_distance=self.__effective_path_distance,
                amplitude_reduction_factor=self.__amplitude_reduction_factor)

        # Check queries.
        self.assertEqual( feff_parameters.atoms, self.__atoms)
        self.assertEqual( feff_parameters.potentials, self.__potentials)
        self.assertEqual( feff_parameters.edge, self.__edge)
        self.assertEqual( feff_parameters.amplitude_reduction_factor, self.__amplitude_reduction_factor)
        self.assertEqual( feff_parameters.effective_path_distance, self.__effective_path_distance)

    def testFinalization(self):
        """ That that the finalization flag is set correctly. """
        feff_parameters = FEFFPhotonMatterInteractorParameters(
                atoms=self.__atoms,
                potentials=self.__potentials,
                edge=self.__edge,
                effective_path_distance=self.__effective_path_distance,
                amplitude_reduction_factor=self.__amplitude_reduction_factor)

        # Is finalized after construction.
        self.assertTrue(feff_parameters.finalized)

        # Change a parameter
        feff_parameters.edge='L1'
        self.assertFalse(feff_parameters.finalized)

        # Finalize.
        feff_parameters.finalize()
        self.assertTrue(feff_parameters.finalized)

    def testSetters(self):
        """ Test that setting parameters works correctly. """

        # Construct the object.
        feff_parameters = FEFFPhotonMatterInteractorParameters(
                atoms=self.__atoms,
                potentials=self.__potentials,
                edge=self.__edge,
                effective_path_distance=self.__effective_path_distance,
                amplitude_reduction_factor=self.__amplitude_reduction_factor)

        # Set new parameters.
        feff_parameters.atoms = self.__atoms[:10]
        feff_parameters.potentials = None
        feff_parameters.edge = 'L2'
        feff_parameters.amplitude_reduction_factor = 0.1
        feff_parameters.effective_path_distance = 5.0

         # Check attributes
        self.assertEqual( feff_parameters._FEFFPhotonMatterInteractorParameters__atoms, self.__atoms[:10])
        self.assertEqual( feff_parameters._FEFFPhotonMatterInteractorParameters__potentials, None )
        self.assertEqual( feff_parameters._FEFFPhotonMatterInteractorParameters__edge, 'L2' )
        self.assertEqual( feff_parameters._FEFFPhotonMatterInteractorParameters__amplitude_reduction_factor, 0.1 )
        self.assertEqual( feff_parameters._FEFFPhotonMatterInteractorParameters__effective_path_distance, 5.0 )

    def testCheckAndSetAtoms(self):
        """ Test the atom check and set utility. """

        # None
        self.assertRaises( TypeError, _checkAndSetAtoms, None )
        # Wrong type
        self.assertRaises( TypeError, _checkAndSetAtoms, 1 )
        # Empty
        self.assertRaises( TypeError, _checkAndSetAtoms, [] )
        # Wrong shape
        self.assertRaises( TypeError, _checkAndSetAtoms, [1.0, 'Cu', 0] )
        # [0] not an iterable
        self.assertRaises( TypeError, _checkAndSetAtoms, [[0.0, 'Cu', 0]] )
        ## [0] not of length 3
        self.assertRaises( TypeError, _checkAndSetAtoms, [[[0.0, 0.1], 'Cu', 0]] )
        # [1] not symbol
        self.assertRaises( TypeError, _checkAndSetAtoms, [[[0.0, 0.0, 0.0], 29, 0]] )
        # [1] not a correct symbol
        self.assertRaises( ValueError, _checkAndSetAtoms, [[[0.0, 0.0, 0.0], 'Xx', 0]] )
        # [2] not integer
        self.assertRaises( TypeError, _checkAndSetAtoms, [[[0.0, 0.0, 0.0], 'Cu', 'i']] )
        # 0 not in potential indices.
        self.assertRaises( ValueError, _checkAndSetAtoms, [[[0.0, 0.0, 0.0], 'Cu', 1]] )
        # Two 0's in potential indices.
        self.assertRaises( ValueError, _checkAndSetAtoms, [[[0.0, 0.0, 0.0], 'Cu', 0],[[0.1, 0.2, 0.3], 'Cu', 0]] )
        # Index missing.
        self.assertRaises( ValueError, _checkAndSetAtoms, [[[0.0, 0.0, 0.0], 'Cu', 0],[[0.1, 0.2, 0.3], 'Cu', 2]] )

        # Ok.
        self.assertEqual( _checkAndSetAtoms ([[[0.0, 0.0, 0.0], 'Cu', 0]]), [[[0.0, 0.0, 0.0], 'Cu', 0]] )

    def testCheckAndSetPotentials(self):
        """ Test the potential check and set utility. """

        # None.
        self.assertIs( _checkAndSetPotentials( None ), None)

        # Anything but None.
        self.assertRaises( ValueError, _checkAndSetPotentials, [[0, 29, 'Cu'], [1, 29, 'Cu']] )

    def testCheckAndSetEdge(self):
        """ Test the edge check and set utility. """

        # None.
        self.assertEqual( _checkAndSetEdge(None), 'K' )

        # Not a string
        self.assertRaises( TypeError, _checkAndSetEdge, 0 )

        # Not a valid edge designator.
        self.assertRaises( ValueError, _checkAndSetEdge, 'L' )

        # Lower case works.
        self.assertEqual( _checkAndSetEdge('k'), 'K' )
        # Ok.
        self.assertEqual( _checkAndSetEdge('L1'), 'L1' )

    def testCheckAndSetAmplitudeReductionFactor(self):
        """ Test the amplitude reduction factor check and set utility. """

        # None.
        self.assertEqual( _checkAndSetAmplitudeReductionFactor( None ), 1.0 )
        # Wrong type.
        self.assertRaises( TypeError, _checkAndSetAmplitudeReductionFactor, 'a' )
        # Outside range.
        self.assertRaises( ValueError, _checkAndSetAmplitudeReductionFactor, -1.4 )
        self.assertRaises( ValueError, _checkAndSetAmplitudeReductionFactor, 2.4 )

        # Int ok.
        self.assertEqual( _checkAndSetAmplitudeReductionFactor( 1 ), 1.0 )
        self.assertEqual( _checkAndSetAmplitudeReductionFactor( 0 ), 0.0 )

        # Float ok.
        self.assertEqual( _checkAndSetAmplitudeReductionFactor( 0.5), 0.5 )

    def testCheckAndSetEffectivePathDistance(self):
        """ Test the effective path distance check and set utility. """

        # None.
        self.assertEqual( _checkAndSetEffectivePathDistance( None ), None )
        # Wrong type.
        self.assertRaises( TypeError, _checkAndSetEffectivePathDistance, 'a' )
        # Outside range.
        self.assertRaises( ValueError, _checkAndSetEffectivePathDistance, -1.4 )

        # Int ok.
        self.assertEqual( _checkAndSetEffectivePathDistance( 1 ), 1.0 )
        self.assertEqual( _checkAndSetEffectivePathDistance( 0 ), 0.0 )
        self.assertEqual( _checkAndSetEffectivePathDistance( 2 ), 2.0 )

        # Float ok.
        self.assertEqual( _checkAndSetEffectivePathDistance( 0.5), 0.5 )

    def testSerialize(self):
        """ Check that the serialize() method produces a valid feff.inp file."""

        feff_parameters = FEFFPhotonMatterInteractorParameters(
                atoms=self.__atoms,
                potentials=self.__potentials,
                edge=self.__edge,
                effective_path_distance=self.__effective_path_distance,
                amplitude_reduction_factor=self.__amplitude_reduction_factor,
                )

        # Setup a stream to write to.
        stream = StringIO.StringIO()
        feff_parameters.serialize( stream = stream )




if __name__ == '__main__':
    unittest.main()

