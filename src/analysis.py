# analysis helpers: load data and run baseline OLS with fixed effects

import pandas as pd
import statsmodels.formula.api as smf

def load_data(path='data/synthetic_data.csv'):
    return pd.read_csv(path)

def baseline_fe(df):
    # OLS with firm and year fixed effects via categorical dummies
    df = df.copy()
    formula = 'outcome ~ digital_index + treatment + C(firm_id) + C(year)'
    model = smf.ols(formula=formula, data=df).fit()
    return model

if __name__ == '__main__':
    df = load_data()
    model = baseline_fe(df)
    print(model.summary())
