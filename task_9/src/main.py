import sys
import os
from replicate_statistics import load_data, calculate_replicate_statistics, save_replicate_summary
from correlation_analysis import (calculate_correlations, plot_calibration_curve, 
                                  plot_signal_input_scatter, save_correlation_summary)
from feature_engineering import (add_rolling_average, add_normalized_signal, add_power_feature, 
                                 add_error_percent, add_stress_ratio, add_ml_readiness_flag, save_engineered_features)

def main():
    # Make sure the user provided the correct command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python src/main.py <input_csv> <output_dir>")
        sys.exit(1)

    input_csv = sys.argv[1]
    output_dir = sys.argv[2]
    
    # Create the output directory if it doesn't exist yet
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # ----------------------------------------------------
    # Part 1: Replicate Statistics
    # ----------------------------------------------------
    print("Part 1: Replicate Statistics")
    df = load_data(input_csv)
    rep_summary = calculate_replicate_statistics(df)
    
    # Clean up floating point numbers to 4 decimal places before saving the summary
    float_cols = rep_summary.select_dtypes(include=['float64']).columns
    rep_summary_rounded = rep_summary.copy()
    rep_summary_rounded[float_cols] = rep_summary_rounded[float_cols].round(4)
    
    save_replicate_summary(rep_summary_rounded, os.path.join(output_dir, 'replicate_summary.csv'))

    # ----------------------------------------------------
    # Part 2: Correlation Analysis
    # ----------------------------------------------------
    print("Part 2: Correlation Analysis")
    
    # This single call computes correlations, linear fits, and error metrics altogether
    final_corr_summary = calculate_correlations(df)
    save_correlation_summary(final_corr_summary, os.path.join(output_dir, 'correlation_summary.csv'))
    calibration_columns = ['domain','x_variable','y_variable','n_samples','slope','intercept','r_squared','mae','rmse']
    
    final_corr_summary[calibration_columns].to_csv(
        os.path.join(output_dir, 'calibration_summary.csv'),
        index=False
    )

    # Generate the calibration curve plots using the replicate summary data
    for domain in ['Biochem', 'Electronics', 'Mechanical']:
        plot_path = os.path.join(output_dir, f'calibration_curve_{domain.lower()}.png')
        plot_calibration_curve(rep_summary_rounded, domain, plot_path)
        
    # Generate the main raw scatter plot
    scatter_path = os.path.join(output_dir, 'correlation_signal_input.png')
    plot_signal_input_scatter(df, scatter_path)

    # ----------------------------------------------------
    # Part 3: Feature Engineering
    # ----------------------------------------------------
    print("Part 3: Feature Engineering")
    
    # Apply all feature building steps sequentially
    df_engineered = add_rolling_average(df)
    df_engineered = add_normalized_signal(df_engineered)
    df_engineered = add_power_feature(df_engineered)
    df_engineered = add_error_percent(df_engineered)
    df_engineered = add_stress_ratio(df_engineered)
    df_engineered = add_ml_readiness_flag(df_engineered, rep_summary)
    
    # Save the complete dataset containing the engineered features
    save_engineered_features(df_engineered, os.path.join(output_dir, 'engineered_features.csv'))
    
    # Isolate and save only the rows that are completely stable and ready for ML models
    ml_ready_dataset = df_engineered[df_engineered['ml_ready']].copy()
    save_engineered_features(ml_ready_dataset, os.path.join(output_dir, 'ml_ready_dataset.csv'))
    
    print("Pipeline completed successfully!")

if __name__ == "__main__":
    main()