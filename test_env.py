import sys
import numpy as np

def main():
    print("--- Virtual Environment Test ---")
    print(f"Python Executable: {sys.executable}")
    print(f"Python Version: {sys.version.split()[0]}")
    
    # Test NumPy functionality
    arr = np.array([1, 2, 3, 4, 5])
    print(f"NumPy Array successfully created: {arr}")
    print(f"Array mean: {np.mean(arr)}")

if __name__ == "__main__":
    main()
