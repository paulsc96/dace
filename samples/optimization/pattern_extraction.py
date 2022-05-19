# Copyright 2019-2022 ETH Zurich and the DaCe authors. All rights reserved.
import os
import dace
import numpy as np

from pathlib import Path

from dace import optimization as optim
from dace.sdfg import infer_types

if __name__ == '__main__':

    sdfg_path = Path(__file__).parent.parent.parent / "hI_8.sdfg"
    sdfg = dace.SDFG.from_file(sdfg_path)

    infer_types.infer_connector_types(sdfg)
    infer_types.set_default_schedule_and_storage_types(sdfg, None)

    dreport = None

    print("We got it")

    tuner = optim.OnTheFlyMapFusionTuner(sdfg, measurement=dace.InstrumentationType.GPU_Events)
    tuner.optimize(apply=True)
    exit()

    tuner = optim.SubgraphFusionTuner(sdfg, measurement=dace.InstrumentationType.GPU_Events)
    tuner.optimize(apply=True)

    #sdfg_path = Path(os.environ["HOME"]) / "projects/tuning-dace/hg-fvt-transient-tuned.sdfg"
    #sdfg.save(sdfg_path)

