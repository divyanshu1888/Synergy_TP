import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt

def get_relationships():
    return [
        ('Biochem', 'input_value', 'signal'), 
        ('Electronics', 'input_value', 'signal'), 
        ('Electronics', 'temperature_c', 'signal'),
        ('Mechanical', 'input_value', 'signal'), 
        ('Mechanical', 'input_value', 'stress_mpa')
    ]

def get_valid_data(df, domain, x_col, y_col):
    domain_data = df[df['domain'] == domain]
    return domain_data.dropna(subset=[x_col, y_col])

def calculate_correlations(df):
    """Calculates correlations, fit metrics, and error metrics all at once."""
    results = []
    
    for domain, x_col, y_col in get_relationships():
        valid_data = get_valid_data(df, domain, x_col, y_col)
        
        if len(valid_data) > 1:
            x = valid_data[x_col].values
            y = valid_data[y_col].values
            
            # 1. Correlations
            p_corr, _ = pearsonr(x, y)
            s_corr, _ = spearmanr(x, y)
            
            # 2. Linear Fit
            x_reshaped = x.reshape(-1, 1)
            model = LinearRegression()
            model.fit(x_reshaped, y)
            y_pred = model.predict(x_reshaped)
            
            # 3. Error Metrics
            r_squared = model.score(x_reshaped, y)
            mae = mean_absolute_error(y, y_pred)
            rmse = np.sqrt(mean_squared_error(y, y_pred))
            
            # Append everything as a single dictionary
            results.append({
                'domain': domain,
                'x_variable': x_col,
                'y_variable': y_col,
                'n_samples': len(valid_data),
                'pearson': round(p_corr, 4),
                'spearman': round(s_corr, 4),
                'slope': round(model.coef_[0], 4),
                'intercept': round(model.intercept_, 4),
                'r_squared': round(r_squared, 4),
                'mae': round(mae, 4),
                'rmse': round(rmse, 4)
            })
            
    return pd.DataFrame(results)

# Aliases to satisfy the required assignment interface
def fit_calibration_line(df):
    return calculate_correlations(df)

def calculate_fit_metrics(df):
    return calculate_correlations(df)

def save_correlation_summary(df, output_path):
    float_columns = df.select_dtypes(include=['float64']).columns
    new_df = df.copy()
    new_df[float_columns] = new_df[float_columns].round(4)
    new_df.to_csv(output_path, index=False)

def plot_calibration_curve(summary_df, domain, output_path):
    # This expects the replicate_summary DataFrame to access mean and confidence intervals
    domain_data = summary_df[summary_df['domain'] == domain]
    
    if len(domain_data) > 0:
        plt.figure(figsize=(8, 6))
        
        y_err = domain_data['confidence_interval_upper'] - domain_data['mean_signal']
        
        plt.errorbar(
            x=domain_data['input_value'], 
            y=domain_data['mean_signal'], 
            yerr=y_err, 
            fmt='o-', 
            capsize=5, 
            label=f'{domain} Data'
        )
                     
        plt.title(f'Calibration Curve: {domain}')
        plt.xlabel('Input Value')
        plt.ylabel('Mean Signal')
        plt.grid(True, linestyle='--')
        plt.legend()
        
        plt.savefig(output_path)
        plt.close()

def plot_signal_input_scatter(df, output_path):
    plt.figure(figsize=(10, 6))
    domains = ['Biochem', 'Electronics', 'Mechanical']
    
    for current_domain in domains:
        domain_data = df[df['domain'] == current_domain]
        
        plt.scatter(
            domain_data['input_value'], 
            domain_data['signal'], 
            label=current_domain
        )
                    
    plt.title('Raw Signal vs Input Value by Domain')
    plt.xlabel('Input Value')
    plt.ylabel('Raw Signal')
    plt.grid(True, linestyle='--')
    plt.legend()
    
    plt.savefig(output_path)
    plt.close()