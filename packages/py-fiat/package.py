# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyFiat(PythonPackage):
    """The FInite element Automatic Tabulator FIAT supports generation of
    arbitrary order instances of the Lagrange elements on lines, triangles, and
    tetrahedra. It is also capable of generating arbitrary order instances of
    Jacobi-type quadrature rules on the same element shapes. Further, H(div)
    and H(curl) conforming finite element spaces such as the families of
    Raviart-Thomas, Brezzi-Douglas-Marini and Nedelec are supported on
    triangles and tetrahedra. Upcoming versions will also support Hermite and
    nonconforming elements"""

    homepage = "https://github.com/FEniCS/fiat"
    git = "https://github.com/FEniCS/fiat.git"

    version("master", branch="master")
