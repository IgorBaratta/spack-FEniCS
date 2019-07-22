# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyUfl(PythonPackage):
    """The Unified Form Language (UFL) is a domain specific language for
    declaration of finite element discretizations of variational forms. More
    precisely, it defines a flexible interface for choosing finite element
    spaces and defining expressions for weak forms in a notation close to
    mathematical notation."""

    homepage = "https://bitbucket.org/fenics-project/ufl"
    url = "https://bitbucket.org/fenics-project/ufl/downloads/ufl-2018.1.0.tar.gz"
    git = "https://bitbucket.org/fenics-project/ufl.git"

    version("master", branch="master")

    depends_on("py-setuptools", type="build")
