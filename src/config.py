# config.py

DB_PATH = "gas_monitoring.db"
TABLE_NAME = "gas_monitoring"

RANDOM_STATE = 42
TEST_SIZE = 0.2
N_ESTIMATORS = 200

CATEGORICAL_COLS = [
    'HVAC Operation Mode', 
    'Ambient Light Level', 
    'Time of Day', 
    'CO_GasSensor', 
    'Activity Level'
]
DROP_COLS = ['Session ID']