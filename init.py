import sys
import datetime

# Function to initialize the blockchain or create the initial block
def initialize_blockchain():
    # Initialize the blockchain or create the initial block
    # You might create the initial block with default values
    
    # For example:
    initial_block = {
        'previous_hash': None,
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'case_id': None,
        'item_id': None,
        'status': 'INITIAL',
        'handler': None,
        'organization': None,
        'data_length': 14,
        'data': "Initial block"
    }
    
    # Save or return the initial block (This is where you might save it to a file)
    return initial_block

# Main entry point
if __name__ == "__main__":
    # Perform initialization and retrieve the initial block
    initial_block = initialize_blockchain()
    
    # Print or perform any further operations with the initial block
    print("Blockchain initialized with the initial block:")
    print(initial_block)
