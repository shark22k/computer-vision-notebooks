import torch
import random
import matplotlib.pyplot as plt

def plot_random_samples_with_predictions(model, test_data, class_names, device, k=9):
    """
    Randomly samples images from test data, makes predictions with the model,
    and plots the images with titles showing the actual label and the prediction.
    
    Parameters:
    - model: torch.nn.Module, the trained model to use for predictions.
    - test_data: list, a list of (image, label) tuples.
    - class_names: list, a list of class names corresponding to labels.
    - device: torch.device, the device to run model predictions on.
    - k: int, number of random samples to select and plot (default is 9).
    """
    # Set random seed for reproducibility
    random.seed(42)
    
    # Randomly sample test data
    test_samples, test_labels = [], []
    for sample, label in random.sample(list(test_data), k=k):
        test_samples.append(sample)
        test_labels.append(label)
    
    # Make predictions on sampled data
    pred_probs = make_predictions(model=model, data=test_samples, device=device)
    pred_classes = pred_probs.argmax(dim=1)
    
    # Set up plot
    plt.figure(figsize=(9, 9))
    nrows, ncols = 3, 3  # 3x3 grid for 9 samples
    for i, sample in enumerate(test_samples):
        # Create subplot
        plt.subplot(nrows, ncols, i+1)
        
        # Plot the sample image
        plt.imshow(sample.squeeze(), cmap="gray")
        
        # Determine prediction and true labels
        pred_label = class_names[pred_classes[i]]
        truth_label = class_names[test_labels[i]]
        
        # Set title color based on correctness
        title_color = "g" if pred_label == truth_label else "r"
        
        # Display title
        plt.title(f"Pred: {pred_label} | Truth: {truth_label}", fontsize=10, color=title_color)
        plt.axis(False)
    
    # Show plot
    plt.tight_layout()
    plt.show()

# Example usage:
# Assuming `model`, `test_data`, `class_names`, and `device` are defined
# plot_random_samples_with_predictions(model, test_data, class_names, device)
