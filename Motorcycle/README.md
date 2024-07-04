# Motorcycle lateral stability model

This Python script conducts an eigenvalue analysis to explore the stability characteristics of a dynamic system varying with longitudinal speed. The analysis involves computing eigenvalues, filtering for positive imaginary parts, and evaluating damping ratios. The results are visualized through scatter plots, root locus plots, and stability analyses.

The [description](./Docs/Motorcycle_model_description.md) is included in the repository.

## Dependencies

- `numpy`: For numerical computations and array operations.
- `matplotlib.pyplot`: For plotting and visualizing data.
- `labellines`: A utility for labeling lines on plots.
- `eigen_functions`: Custom functions `Damping_ratio` and `filter_positive_imaginary_part` for computing damping ratios and filtering eigenvalues.
- `MatrixA` and `MatrixE`: Custom modules for defining and computing matrices related to the dynamic system.

## Usage

1. Ensure all dependencies are installed using `pip install -r requirements.txt`.
2. Configure the parameters in `Parameters_Motorcycle.py` as required.
3. Run the script to generate and display:

   - **Root Locus Plot**: Visualizes eigenvalues with real and imaginary parts on a scatter plot.
   - **Stability Analysis**: Analyzes stability characteristics such as 'Wobble' and 'Weave' modes over varying speeds.
   - **Damping Factor Analysis**: Evaluates the damping factor across speed ranges.

## Algorithm Overview

1. **Initialization**:
   - Initialize matrices `E` and its inverse `E_inv` using `MatrixE`.
   - Define speed range (`Speed_range`).

2. **Matrix Computations**:
   - Compute matrix `A` for each speed `V_x` in `Speed_range` using `MatrixA`.

3. **Eigenvalue Analysis**:
   - Compute eigenvalues of `E_inv * A` matrix products.
   - Filter eigenvalues to retain those with positive imaginary parts using `filter_positive_imaginary_part`.
   - Calculate damping ratios (`chi_weave` and `chi_wobble`) using `Damping_ratio`.

4. **Plotting**:
   - **Root Locus Plot**: Scatter plot of eigenvalues (`u2`) with annotations for 'Wobble' and 'Weave' modes. Includes stability regions and damping factor lines.
   - **Stability Analysis Plot**: Plots the influence of longitudinal speed on stability ('Wobble' and 'Weave').
   - **Damping Factor Plot**: Displays how damping factor varies with speed.

5. **Visualization Enhancements**:
   - Annotations and visual aids (like shaded regions) enhance readability and interpretation of stability and damping analyses.

## Example Outputs

- Example root locus plot demonstrating eigenvalue distribution.
- Stability analysis plot showing 'Wobble' and 'Weave' behavior over speed.
- Damping factor plot illustrating variations with speed.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

