#!python3

def colPreparation():
    LabelEncoder = ['Gender','Driving_License','Previously_Insured','Vehicle_Damage']
    oneHotEncoder =['Vehicle_Age','Policy_Sales_Channel','Region_Code']
    standardScaller = ['Age','Annual_Premium','Vintage']
    
    return LabelEncoder,oneHotEncoder, standardScaller