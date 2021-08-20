# In[]
import os
import numpy as np
import pandas as pd
from utils import *

# In[]
admissions_path = j_path('admissions.csv')
callout_path = j_path('callout.csv')
icustays_path = j_path('icustays.csv')
patients_path = j_path('patients.csv')
services_path = j_path('services.csv')
transfers_path = j_path('transfers.csv')

diagnoses_icd_path = j_path('diagnoses_icd.csv')

# In[]
admissions = read_admissions_data(admissions_path)

icustays = read_icustays_data(icustays_path)
patients, is_expire, not_expire = read_patients_data(patients_path)

diagnoses = read_diagnoses_icd_data(diagnoses_icd_path)


# In[]
callout = read_callout_data(callout_path)

# In[]
services = read_services_data(services_path)

# In[]
transfers = read_transfers_data(transfers_path)
