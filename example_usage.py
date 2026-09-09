"""Example usage for SVD Skill."""
from client import SVDLowRank

def main():
    print("Executing SVD Power Iteration...")
    A = [[3.0, 0.0], [0.0, -2.0]]
    sigma, u, v = SVDLowRank.top_singular_triple(A)
    print(f"Top Singular Value: {sigma}")
    print(f"Left Singular Vector (u): {u}")
    print(f"Right Singular Vector (v): {v}")
    assert abs(sigma - 3.0) < 1e-2
    print("SVD Power Iteration verified successfully!")

if __name__ == "__main__":
    main()
