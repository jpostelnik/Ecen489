import numpy as np
import matplotlib.pyplot as plt

class SRAM_CIM:
    def __init__(self, rows=128, cols=128, adc_bits=3):
        self.rows = rows
        self.cols = cols
        self.adc_bits = adc_bits
        self.weights = np.random.choice([-1, 1], size=(rows, cols))  # binary weights

    def load_weights(self, weight_matrix):
        assert weight_matrix.shape == (self.rows, self.cols), "Weight matrix shape mismatch"
        self.weights = weight_matrix

    def compute_mac(self, input_vector):
        assert len(input_vector) == self.rows, "Input vector length mismatch"
        analog_outputs = np.dot(input_vector, self.weights)
        return analog_outputs

    def adc_quantize(self, analog_outputs):
        max_val = self.rows
        min_val = -self.rows
        levels = 2 ** self.adc_bits
        step = (max_val - min_val) / (levels - 1)
        quantized = np.round((analog_outputs - min_val) / step) * step + min_val
        return quantized

    def inference(self, input_vector, visualize=False):
        analog = self.compute_mac(input_vector)
        digital = self.adc_quantize(analog)

        if visualize:
            self.visualize_outputs(analog, digital)

        return digital

    def visualize_outputs(self, analog_outputs, quantized_outputs):
        x = np.arange(len(analog_outputs))
        plt.figure(figsize=(12, 5))

        # Plot analog outputs
        plt.subplot(1, 2, 1)
        plt.plot(x, analog_outputs, label="Analog MAC Output", color="blue")
        plt.title("Analog MAC Outputs")
        plt.xlabel("Column")
        plt.ylabel("MAC Output")
        plt.grid(True)

        # Plot quantized outputs
        plt.subplot(1, 2, 2)
        plt.stem(x, quantized_outputs, linefmt='g-', markerfmt='go', basefmt=" ")
        plt.title(f"Quantized Outputs ({self.adc_bits}-bit ADC)")
        plt.xlabel("Column")
        plt.ylabel("Quantized Value")
        plt.grid(True)

        plt.tight_layout()
        plt.show()

# ---- Example Usage ----
if __name__ == "__main__":
    sram = SRAM_CIM(adc_bits=3)
    input_vec = np.random.choice([-1, 1], size=(128,))
    output = sram.inference(input_vec, visualize=True)

