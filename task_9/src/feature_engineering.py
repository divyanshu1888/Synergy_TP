import pandas as pd
import numpy as np

def add_rolling_average(df):
    df = df.copy()
    df = df.sort_values(by=['domain', 'condition', 'time_step'])
    
    df['rolling_average_signal'] = df.groupby(['domain', 'condition'])['signal'].transform(
    lambda x: x.rolling(window=3, min_periods=1).mean()
    ).round(4)
    return df

def add_normalized_signal(df):
    # Calculate signal relative to baseline, avoiding division by zero or nulls
    df = df.copy()
    df['normalized_signal'] = np.nan
    valid_idx = df['baseline_signal'].notna() & (df['baseline_signal'] != 0)
    
    df.loc[valid_idx, 'normalized_signal'] = df.loc[valid_idx, 'signal'] / df.loc[valid_idx, 'baseline_signal']
    return df

def add_power_feature(df):
    # Power calculation (P = V * I) specific to the Electronics domain
    df = df.copy()
    df['power_w'] = np.nan
    is_electronics = (df['domain'] == 'Electronics') & df['voltage_v'].notna() & df['current_a'].notna()
    
    df.loc[is_electronics, 'power_w'] = df.loc[is_electronics, 'voltage_v'] * df.loc[is_electronics, 'current_a']
    return df

def add_error_percent(df):
    # Percentage deviation from the expected theoretical signal
    df = df.copy()
    df['error_percent'] = np.nan
    valid_idx = df['expected_signal'].notna() & (df['expected_signal'] != 0)
    
    df.loc[valid_idx, 'error_percent'] = (
        (df.loc[valid_idx, 'signal'] - df.loc[valid_idx, 'expected_signal']) 
        / df.loc[valid_idx, 'expected_signal']
    ) * 100
    return df

def add_stress_ratio(df):
    # Structural stress ratio relative to reference baseline for Mechanical domain
    df = df.copy()
    df['stress_ratio'] = np.nan
    is_mechanical = (df['domain'] == 'Mechanical') & df['reference_stress_mpa'].notna() & (df['reference_stress_mpa'] != 0)
    
    df.loc[is_mechanical, 'stress_ratio'] = df.loc[is_mechanical, 'stress_mpa'] / df.loc[is_mechanical, 'reference_stress_mpa']
    return df

def add_ml_readiness_flag(df, replicate_summary):
    # Merge the stability flags computed during the replicate analysis phase
    df = df.copy()
    merge_cols = ['domain', 'condition', 'input_type', 'input_value', 'input_unit', 'signal_unit']
    
    merged = pd.merge(
        df, 
        replicate_summary[merge_cols + ['stability_flag']], 
        on=merge_cols, 
        how='left'
    )
    
    # Verify presence of all critical features and ensure the entire replicate group is stable
    has_required_data = (
    df['signal'].notna() &
    df['expected_signal'].notna() &
    (df['expected_signal'] != 0) &
    df['input_value'].notna() &
    df['domain'].notna() &
    df['condition'].notna()
)
    
    df['stability_flag'] = merged['stability_flag'].values
    df['ml_ready'] = has_required_data & (df['stability_flag'] == 'stable')
    return df

def save_engineered_features(df, output_path):
    # Keep the working DataFrame safe by making a copy before rounding and exporting
    output_df = df.copy()
    float_cols = output_df.select_dtypes(include=['float64']).columns
    output_df[float_cols] = output_df[float_cols].round(4)
    output_df.to_csv(output_path, index=False)
