import pandas as pd
from sklearn . model_selection import train_test_split
from sklearn . ensemble import RandomForestClassifier
from sklearn . metrics import f1_score

# Load data
train = pd . read_csv ('../ data / train .csv ')
X = train . drop ('target ', axis =1)
y = train ['target ']

# Split into train / validation
X_train , X_val , y_train , y_val = train_test_split (X , y , test_size =0.2 , random_state
=42)

# Train a baseline model
clf = RandomForestClassifier ( n_estimators =100 , random_state =42)
clf . fit ( X_train , y_train )

# Evaluate
y_pred = clf . predict ( X_val )
score = f1_score ( y_val , y_pred , average ='macro ')
print ( f'Validation F1 Score : { score :.4f}')

# Make predictions on test set
test = pd . read_csv ('../ data / test .csv ')
test_preds = clf . predict ( test )
pd . DataFrame ({ 'id ': test ['id '] , 'target ': test_preds }) . to_csv ('../ submissions /
sample_submission . csv ', index = False )
