# minimal synthetic data generation and save

import pandas as pd
import numpy as np

RANDOM_SEED = 42

def generate_synthetic_panel(n_firms=200, n_years=10, start_year=2008):
    np.random.seed(RANDOM_SEED)
    firms = np.arange(1, n_firms+1)
    years = np.arange(start_year, start_year + n_years)
    rows = []
    for f in firms:
        firm_effect = np.random.normal(0, 1)
        for t_idx, y in enumerate(years):
            time_trend = 0.1 * t_idx
            digital_index = np.random.normal(0, 1) + 0.5 * (t_idx >= (n_years//2))
            treatment = 1 if (f % 5 == 0 and t_idx >= (n_years//2)) else 0
            noise = np.random.normal(0, 1)
            outcome = 0.5 * digital_index + 0.8 * treatment + firm_effect + time_trend + noise
            rows.append({
                'firm_id': f,
                'year': y,
                'digital_index': digital_index,
                'treatment': treatment,
                'outcome': outcome
            })
    df = pd.DataFrame(rows)
    return df

if __name__ == '__main__':
    df = generate_synthetic_panel()
    df.to_csv('data/synthetic_data.csv', index=False)
    print('Saved data/synthetic_data.csv', df.shape)
