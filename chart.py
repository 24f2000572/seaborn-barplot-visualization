import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set professional Seaborn style
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate realistic synthetic business data
np.random.seed(42)
products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
sales = np.random.randint(15000, 45000, size=5)

df = pd.DataFrame({
    "Product": products,
    "Quarterly Sales": sales
})

# Create figure sized for exactly 512x512 (dpi 64 × 8 inches = 512px)
plt.figure(figsize=(8, 8))

# Create barplot
sns.barplot(
    data=df,
    x="Product",
    y="Quarterly Sales",
)

# Professional styling
plt.title("Quarterly Sales Performance by Product", fontsize=20)
plt.xlabel("Product", fontsize=16)
plt.ylabel("Sales (USD)", fontsize=16)

# Save chart at exactly 512x512 pixels
plt.savefig("chart.png", dpi=64, bbox_inches="tight")

# Show preview (optional)
# plt.show()
