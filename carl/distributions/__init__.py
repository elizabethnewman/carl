# -*- coding: utf-8 -*-
#
# Carl is free software; you can redistribute it and/or modify it
# under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""Distributions.

Note: This module is only meant to be a minimally working prototype for
      composing and fitting distributions. It is not meant to be a full fledged
      replacement of RooFit or alikes.
"""

from .base import DistributionMixin
from .base import TheanoDistribution

from .exponential import Exponential
from .normal import Normal
from .normal import MultivariateNormal
from .mixture import Mixture
from .uniform import Uniform

from .histogram import Histogram
from .kde import KernelDensity
from .sampler import Sampler

__all__ = ("DistributionMixin",
           "TheanoDistribution"
           "Exponential",
           "Normal",
           "MultivariateNormal",
           "Uniform",
           "Mixture",
           "Histogram",
           "KernelDensity",
           "Sampler")
