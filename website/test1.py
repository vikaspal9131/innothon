import scipy.io

file_path = 'uploads/E00007.mat'
mat_data = scipy.io.loadmat(file_path)
print(mat_data['val'])  # Check keys to find the ECG data
