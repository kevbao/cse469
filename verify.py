import sys
import hashlib

# Function to verify the blockchain integrity
def verify_blockchain(chain_of_custody):
    # Check if the chain of custody is empty or has only the initial block
    if not chain_of_custody or len(chain_of_custody) == 1:
        print("Error: Blockchain is empty or contains only the initial block.")
        return False
    
    # Initialize variables for verification
    previous_block = None
    for block_id, block in chain_of_custody.items():
        # Check if the current block's previous hash matches the hash of the previous block
        if previous_block and block['previous_hash'] != calculate_hash(previous_block):
            print(f"Error: Bad block detected at {block_id}.")
            return False
        
        # Additional verification rules can be added here
        
        previous_block = block
    
    # Verification successful if no issues found
    print("Blockchain verified. No issues found.")
    return True

# Function to calculate hash for a block
def calculate_hash(block):
    # Hashing logic - for example, using SHA-256
    # This function might differ based on your specific data structure
    
    # Example hashing logic:
    block_string = ''.join(str(value) for value in block.values()).encode()
    return hashlib.sha256(block_string).hexdigest()

# Main entry point
if __name__ == "__main__":
    # Load existing chain of custody data or create an empty dictionary
    # Replace this with your actual mechanism to load blockchain data
    chain_of_custody = {}  # Assuming chain_of_custody is a dictionary
    
    # Verify the blockchain integrity
    verify_blockchain(chain_of_custody)
