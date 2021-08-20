import os
from numpy.lib.npyio import recfromtxt
import yaml
import pandas as pd
from utils.tools import *


def read_admissions_data(mimic3_path):
    admissions = df_from_csv(mimic3_path)
    admissions = admissions[
        [
            'subject_id', 'hadm_id', 'admittime', 'dischtime', 'deathtime',
            'admission_type', 'ethnicity', 'diagnosis'
        ]
    ]
    admissions.admittime = pd.to_datetime(admissions.admittime)
    admissions.dischtime = pd.to_datetime(admissions.dischtime)
    return admissions


def read_patients_data(mimic3_path):
    patients = df_from_csv(mimic3_path)
    patients.dob = pd.to_datetime(patients.dob)
    patients.dod = pd.to_datetime(patients.dod)
    is_expire = patients[
        patients.dod_hosp.notnull() | patients.dod_ssn.notnull()
    ]
    not_expire = patients[
        patients.dod_hosp.isnull() & patients.dod_ssn.isnull()
    ]
    return patients, is_expire, not_expire


def read_icustays_data(mimic3_path):
    icustays = df_from_csv(mimic3_path)
    icustays.intime = pd.to_datetime(icustays.intime)
    icustays.outtime = pd.to_datetime(icustays.outtime)
    return icustays


def read_diagnoses_icd_data(mimic3_path):
    d_icd_diagnoses_path = j_dic_path('d_icd_diagnoses.csv')
    codes = df_from_csv(d_icd_diagnoses_path)
    diagnoses = df_from_csv(mimic3_path)
    diagnoses = diagnoses.merge(codes, how='inner')
    return diagnoses


# unfinished


def read_callout_data(mimic3_path):
    callout = df_from_csv(mimic3_path)
    return callout


def read_services_data(mimic3_path):
    services = df_from_csv(mimic3_path)
    return services


def read_transfers_data(mimic3_path):
    transfers = df_from_csv(mimic3_path)
    return transfers
