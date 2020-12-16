import builtins as exceptions
# many unsupported attribute of types lib in python 3
import types
import re
import math
from collections import defaultdict
import numpy
import scipy
#import metabolite

import cobra
from cobra import Metabolite, Reaction, Gene
from cobra.flux_analysis import deletion, moma, phenotype_phase_plane
from cobra.core.solution import get_solution
#from cobra.manipulation import modify

#from ..analysis import FCA, Pareto, RWFM, MOMA, ROOM, GeometricFBA, MinSolve
#from ..analysis import Graph, FluxSum, FVA, MinSolve, Scan
#from ..manipulation import Reversible
#from ..classes.flux import flux
# rom ..io import Network


class Reaction(cobra.Reaction):
    """
    Reaction inherits from the cobra package reaction that holds information relates to reactions
    with the added list of proteins(enzymes), metabolite exchange rate equation (rate_equation), and exchange rate constants (rate_constant) defined.

    Parameters
    ----------
    proteins: dict of enzyme id and name
    rate_equation: metabolite exchange rate equation
    rate_constant: metabolite exchange constant
    """

    def __init__(self, id=None, name='', subsystem='', lower_bound=float('-inf'), upper_bound=float('inf'), proteins={}, rate_constant=1, rate_equation='conc ** coef'):
        super().__init__(id=id, name=name, subsystem=subsystem,
                         lower_bound=lower_bound, upper_bound=upper_bound)
        self.proteins = proteins
        self.useable = True
        self.all_mets_has_formula = True
        self.rate_equation = rate_equation
        self.rate_constant = rate_constant
