import pandas as pd
import numpy as np
import statsmodels.api as sm
from math import log

df_interest = pd.read_csv('LoanStats3c_update.csv', index_col=0)

cleanInterestRate = df_interest['int_rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
df_interest['int_rate'] = cleanInterestRate

X = df_interest[['annual_inc']]
y = df_interest['int_rate']

X = sm.add_constant(X)
est = sm.OLS(y, X).fit()

print est.summary()

X = df_interest.copy()
y = X.pop('int_rate')

print y.groupby(X.home_ownership).mean()

import statsmodels.formula.api as smf
df_interest['home_ownership_ord'] = pd.Categorical(df_interest.home_ownership).labels

est = smf.ols(formula="int_rate ~ home_ownership_ord + annual_inc", data=df_interest).fit()
print est.summary()

df_interest['home_ownership_ord'] = pd.Categorical(df_interest.home_ownership).labels

est = smf.ols(formula="int_rate ~ home_ownership_ord * annual_inc", data=df_interest).fit()
print est.summary()
