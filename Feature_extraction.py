def feature_model(models):
  from tensorflow.keras.models import Model
  from numpy import expand_dims,argmax

  fmodels=[]
  for i in range(len(models)):
    feature_extractor= Model(inputs=models[i].inputs, outputs=models[i].layers[-6].output)
    fmodels.append(feature_extractor)

  return fmodels

def feature_extraction(models,img,label):
  from tensorflow.keras.models import Model
  from numpy import expand_dims,argmax

  value=[]
  value.append(argmax(label))
  print(argmax(label))
  img = expand_dims(img, axis=0)
  for i in range(len(models)):
    #feature_extractor= Model(inputs=models[i].inputs, outputs=models[i].layers[-6].output)
    
    pvalue = models[i].predict(img)
    pvalue = pvalue.flatten()

    
    for i in pvalue:
        value.append(i)


   

  return value

  #feature_extractor.summary()
fmodels= feature_model(models)

for i in range(X_train.shape[0]):
  values= feature_extraction(fmodels,X_train[i],y_labels[i])