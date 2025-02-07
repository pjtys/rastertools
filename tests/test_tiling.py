#!/usr/bin/env python
# -*- coding: utf-8 -*-

import filecmp
from eolab.rastertools import Tiling

from . import utils4test

__author__ = "Olivier Queyrut"
__copyright__ = "Copyright 2019, CNES"
__license__ = "Apache v2.0"


__refdir = utils4test.get_refdir("test_tiling/")


def test_tiling_process_file(compare, save_gen_as_ref):
    # create output dir and clear its content if any
    utils4test.create_outdir()

    inputfile = "tif_file"
    geometryfile = "grid.geojson"

    tool = Tiling(utils4test.indir + geometryfile)
    tool.with_output(utils4test.outdir)
    tool.with_id_column("id", [77, 93])
    tool.process_file(utils4test.indir + inputfile + ".tif")

    gen_files = [inputfile + "_tile77.tif", inputfile + "_tile93.tif"]
    if compare:
        match, mismatch, err = utils4test.cmpfiles(utils4test.outdir, __refdir, gen_files)
        assert len(match) == 2
        assert len(mismatch) == 0
        assert len(err) == 0
    elif save_gen_as_ref:
        # save the generated files in the refdir => make them the new refs.
        utils4test.copy_to_ref(gen_files, __refdir)

    utils4test.clear_outdir()
