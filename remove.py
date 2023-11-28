import sys
import datetime

# Function to remove an evidence item from the chain of custody
def remove(item_id, reason, owner, chain_of_custody):
    # Check if the required parameters are provided
    if not item_id or not reason:
        print("Error: Insufficient arguments provided.")
        sys.exit(1)
    
    # Check if the item ID exists in the chain of custody
    if item_id not in chain_of_custody:
        print(f"Error: Item ID '{item_id}' does not exist in the chain of custody.")
        sys.exit(1)
    
    # Check if the item is already removed
    if chain_of_custody[item_id]['status'] == 'REMOVED':
        print("Error: Item is already removed. Cannot perform another removal.")
        sys.exit(1)
    
    # Update the chain of custody entry with removal information
    timestamp = datetime.datetime.utcnow().isoformat()
    chain_of_custody[item_id]['status'] = 'REMOVED'
    chain_of_custody[item_id]['reason'] = reason
    
    # If the reason is 'RELEASED', update owner information
    if reason == 'RELEASED' and owner:
        chain_of_custody[item_id]['owner'] = owner
    
    chain_of_custody[item_id]['timestamp'] = timestamp
    
    # Save the updated chain of custody (This is where you might write to a file or database)
    print(f"Item '{item_id}' successfully removed.")

# Extracting command line arguments
# Example command line: python remove.py <item_id> <reason> [<owner>]
if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 2:
        print("Error: Insufficient command-line arguments.")
        sys.exit(1)
    
    item_id, reason = args[:2]
    owner = args[2] if len(args) > 2 else None
    
    # Load existing data or create an empty dictionary for the chain of custody
    # This should ideally be replaced with a mechanism to load blockchain data
    chain_of_custody = {}  # Assuming chain_of_custody is a dictionary
    
    # Call the remove function with provided arguments
    remove(item_id, reason, owner, chain_of_custody)
