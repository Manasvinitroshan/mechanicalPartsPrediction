# Mechanical Parts Price Prediction

Utilizing Machine Learning Models to Forecast Pricing on Mechanical Components and Automate Sourcing

## Authors

- Manas Kumar Singh<sup>1</sup>
- Shreya Kumari<sup>1</sup>
- Pranjal Singh<sup>2</sup>

<sup>1</sup>Erik Jonsson School of Engineering and Computer Science at The University of Texas at Dallas, Texas, USA  
<sup>2</sup>G. Narayanamma Institute of Technology and Science, Hyderabad, India

Correspondence: Shreya Kumari, Erik Jonsson School of Engineering and Computer Science at The University of Texas at Dallas, Texas, USA.  
Tel: 281-780-1418  
E-mail: [shreyautd@gmail.com](mailto:shreyautd@gmail.com)

## Abstract

In supply chain management, price quotations on machine components can be crucial in determining accurate pricing that may suit a business’s reliability and improve cost control. This project experiments with feasible machine learning models that employ previous material prices and properties such as part family, material grade, dimensions, thread type, and coating to determine the most optimal model. The model analysis determined that Gradient Boosting had a significant predictive accuracy and thus was the best-fit model to forecast pricing on mechanical components.

## Keywords

Supply chain management, price quotations, machine learning models, optical character recognition, gradient boosting

## Table of Contents

- [Introduction](#introduction)
- [Method](#method)
- [Results](#results)
- [Discussion](#discussion)
- [Conclusion](#conclusion)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Appendices](#appendices)

## Introduction

Supply chain management (SCM) is an integral part of any business function, and it has become increasingly prevalent within various industries such as healthcare, e-commerce, energy, and manufacturing. This research aims to manage costs within the manufacturing enterprise effectively and focuses on the mechanical components used in the oil and gas industry.

## Method

The methodology emphasizes using various datasets to forecast pricing on machine components and ultimately automate sourcing. Visual Studio Code is utilized with the Streamlit library to run the model. The ML models are trained using the training data and ultimately applied to present feasible prices based on the test set.

## Results

The study's results support the research's primary hypothesis that the gradient-boosting machine-learning model provides the most accurate prediction for forecasting the prices of mechanical components. The model has the lowest RMSE of $36.56, the lowest MAPE of 6.16%, and the highest R² value of 0.9883.

## Discussion

The results of this study contribute to the inexorable growth of literature on machine learning applications within supply chain management. Utilizing predictive models for automated sourcing, this research helps link machine learning advancements with its practical application.

## Conclusion

This research proves that the gradient boosting model can revolutionize price forecasting by automating sourcing within the manufacturing sector. Future studies could explore integrating additional features to the model, such as market trends and regional cost variations.

## Installation

To get started with the Mechanical Parts Prediction project, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Manasvinitroshan/mechanicalPartsPrediction.git
    cd mechanicalPartsPrediction
    ```

2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use the prediction models, follow these steps:

1. **Prepare your dataset:**
    Ensure your dataset is in the correct format as required by the scripts.

2. **Run the Jupyter Notebook to train the model:**
    ```bash
    jupyter notebook train_model.ipynb
    ```
    Open the `train_model.ipynb` file in Jupyter Notebook and follow the instructions to train the model.

3. **Make predictions:**
    ```bash
    python predict.py --model_path path/to/saved/model --data_path path/to/new/data.csv
    ```

## Contributing

We welcome contributions to improve Mechanical Parts Prediction. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin my-feature-branch`
5. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, feel free to contact us at [shreyautd@gmail.com](mailto:shreyautd@gmail.com).

## Appendices

### Appendix A: GitHub Repository

All the machine learning models relevant to this research are available on GitHub.  
The repository can be accessed through this [link](https://github.com/Manasvinitroshan/mechanicalPartsPrediction).

### Appendix B: Relevant Datasets Utilized

The datasets utilized for this research are linked within the repository.

