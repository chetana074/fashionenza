import torch

# print(torch.version.cuda) # check CUDA version
# print(torch.backends.cudnn.version()) # check cuDNN version
# print(torch.cuda.is_available()) # check if CUDA is available
# print(torch.cuda.device_count()) # check the number of available CUDA devices
# print(torch.cuda.get_device_name()) # check the name of the current CUDA device

print(torch.backends.ocl.get_device_properties(torch.device('cpu'))) # check OpenCL device properties

print(torch.backends.ocl.is_available()) # check if OpenCL is available
if torch.backends.ocl.is_available():
    print(torch.backends.ocl.get_device_properties(torch.device('cpu'))) # check OpenCL device properties