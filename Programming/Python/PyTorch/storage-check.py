import torch

# Create a tensor
tensor = torch.tensor([1, 2, 3])

# Get the underlying storage
storage = tensor.storage()

# Check if it is a storage object
print(torch.is_storage(storage))  # True

# Check if a tensor itself is storage
print(torch.is_storage(tensor))  # False
