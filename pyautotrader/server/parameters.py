import os
import glob
import joblib

from fastapi import HTTPException
from multiprocessing import Lock

mutex = Lock()
parameters = None


def get_parameters(model):
    global mutex
    global parameters
    try:
        mutex.acquire()
        if parameters is None:
            parameters_files = glob.glob(
                os.path.join(model, "*.parameters.pickle"))
            if len(parameters_files) < 0:
                raise HTTPException(
                    status_code=500, detail='Could no find the parameters file...')
            parameters = joblib.load(parameters_files[0])
        return parameters
    finally:
        mutex.release()
