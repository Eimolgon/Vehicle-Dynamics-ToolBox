# Vehicle Dynamics ToolBox

This repository contains various vehicle dynamics models including a bike stability model, a motorcycle stability model, a quarter car model, and a half car model. Each model is organized in its own directory with accompanying documentation, images, and interactive notebooks.

## Index

- [Directory Structure](#directory-structure)
- [Models](#models)
  - [Bike Stability Model](#bike-stability-model)
  - [Motorcycle Stability Model](#motorcycle-stability-model)
  - [Quarter Car Model](#quarter-car-model)
  - [Half Car Model](#half-car-model)
- [Documentation](#documentation)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [References](#references)

## Directory Structure

- `Bicycle/`: Contains the bike stability model code and related files.
- `Motorcycle/`: Contains the motorcycle stability model code and related files.
- `Quarter_car/`: Contains the quarter car model code and related files.
- `Half_car/`: Contains the half car model code and related files.
- `Images/`: Contains all the images used across the models.
- `Docs/`: Contains documentation explaining the theory behind each model.

## Models

### Bike Stability Model
Benchmark for bicycle stability models [1].

### Motorcycle Stability Model
This model predicts weave and wobble modes of vibration of the motorcycle. It is a simple model upgraded to include downforce [2].

### Quarter Car Model
This model represents a simplified version of a vehicle with one wheel and suspension system. It's useful for analyzing vertical dynamics and ride comfort.

### Half Car Model
This model includes two wheels (front and rear) and their respective suspension systems, allowing for more detailed analysis of vehicle dynamics including pitch and bounce motions.

## Documentation
The `Docs/` directory contains detailed explanations of the theoretical background for each model. This includes derivations of the equations of motion, assumptions made, and any simplifications used.


## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/vehicle-dynamics-models.git
    cd vehicle-dynamics-models
    ```

2. Install the necessary dependencies. It's recommended to use a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Explore the models:
    - Navigate to the directory of the model you are interested in.
    - Run the simulation scripts or open the interactive notebooks.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Make sure to update the documentation and include any necessary tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

We acknowledge the authors of the theoretical references used to develop these models.

## References

- [1] Meijaard, J. P., Papadopoulos, J. M., Ruina, A., & Schwab, A. L. (2007). Linearized dynamics equations for the balance and steer of a bicycle: A benchmark and review.
- [2] Lot, R., & Sadauckas, J.(2021). Motorcycle Design: Vehicle Dynamics, Concepts and Applications. (1st ed.). 