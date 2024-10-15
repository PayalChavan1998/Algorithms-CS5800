# Payal Chavan
# CS5800 Algorithms Summer 2024 (Seattle)
# Homework 2
# Date: 05/22/2024






# Function to decode the encrypted message
# encoded_number = number^(e) % N

def break_encryption(N, e, M_e):
    for M_original in range(1, N):
        if pow(M_original, e, N) == M_e:
            return M_original
    return None



if __name__ == "__main__":
    (N, e) = (252167, 11)
    M_e = 74904

    decoded_number = break_encryption(N, e, M_e)
    print(f"Encoded Number: {M_e} \t Decoded Number = {decoded_number}")
