from sklearn import svm
from svmutil import *
from feature_vector import *

trainOb = filterTweets()
testOb = filterTweets('Testing.csv')

result = trainOb.getSVMFeatures()
problem = svm_problem(result['labels'], result['feature_vector'])
#'-q' option suppress console output
param = svm_parameter('-q')
param.kernel_type = LINEAR
classifier = svm_train(problem, param)
#svm_save_model(classifierDumpFile, classifier)

#Test the classifier
test_feature_vector = testOb.getSVMFeatures()['feature_vector']
#p_labels contains the final labeling result
p_labels, p_accs, p_vals = svm_predict([0] * len(test_feature_vector),test_feature_vector, classifier)
