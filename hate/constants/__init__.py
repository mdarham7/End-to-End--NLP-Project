import os

from datetime import datetime

# Common constants
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

# Data Ingestion Constants
ARTIFACTS_DIR: str = "artifacts"

BUCKET_NAME: str = "nlproject123"

S3_DATA_FOLDER: str = "data"




# Data transformation constants 
LABEL = 'label'
TWEET = 'tweet'
DATA_TRANSFORMATION_ARTIFACTS_DIR = 'DataTransformationArtifacts'
TRANSFORMED_FILE_NAME = "final.csv"
DATA_DIR = "data"
ID = 'id'
AXIS = 1
INPLACE = True
DROP_COLUMNS = ['Unnamed: 0','count','hate_speech','offensive_language','neither']
CLASS = 'class'


# Model training constants
MODEL_TRAINER_ARTIFACTS_DIR = 'ModelTrainerArtifacts'
TRAINED_MODEL_DIR = 'trained_model'
TRAINED_MODEL_NAME = 'model.h5'
X_TEST_FILE_NAME = 'x_test.csv'
Y_TEST_FILE_NAME = 'y_test.csv'

X_TRAIN_FILE_NAME = 'x_train.csv'

RANDOM_STATE = 42
EPOCH = 1
BATCH_SIZE = 128
VALIDATION_SPLIT = 0.2


# Model Architecture constants
MAX_WORDS = 50000
MAX_LEN = 300
LOSS = 'binary_crossentropy'
METRICS = ['accuracy']
ACTIVATION = 'sigmoid'

#Model Evalution constants
MODEL_EVALUATION_ARTIFACTS_DIR = 'ModelEvaluationArtifacts'
BEST_MODEL_DIR = 'best_model'
MODEL_EVALUATION_FILE_NAME = 'loss.csv'


MODEL_NAME = 'model.h5'
APP_HOST = "0.0.0.0"
APP_PORT = 8080