"""This script is used to synthesize generated parts of this library."""

import synthtool as synth
import synthtool.gcp as gcp

gapic = gcp.GAPICGenerator()

library = gapic.py_library("datacatalog", "v1beta1", include_protos=True, generator_args=["--dev_samples"])

synth.copy(library)
