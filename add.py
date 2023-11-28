import sys
import uuid
import datetime

# Function to add a new evidence item to the chain of custody
def add(case_id, item_ids, handler, organization):
    # Check if the required parameters are provided
    if not case_id or not item_ids or not handler or not organization:
        print("Error: Insufficient arguments provided.")
        sys.exit(1)
    
    # Load existing data or create an empty dictionary for the chain of custody
    # This should ideally be replaced with a mechanism to load blockchain data
    chain_of_custody = {}
    
    # Iterate over each item ID provided and add to the chain of custody
    for item_id in item_ids:
        # Check if the item ID is unique (not already in the chain of custody)
        if item_id in chain_of_custody:
            print(f"Error: Item ID '{item_id}' already exists in the chain of custody.")
            sys.exit(1)
        
        # Create a new entry for the item in the chain of custody
        timestamp = datetime.datetime.utcnow().isoformat()
        entry = {
            'case_id': case_id,
            'handler': handler,
            'organization': organization,
            'status': 'CHECKEDIN',
            'timestamp': timestamp
        }
        
        # Add the entry to the chain of custody for the specific item ID
        chain_of_custody[item_id] = entry
    
    # Save the updated chain of custody (This is where you might write to a file or database)
    print("Items successfully added to the chain of custody.")

# Extracting command line arguments
# Example command line: python add.py <case_id> <item_id1> <item_id2> <handler> <organization>
if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 5:
        print("Error: Insufficient command-line arguments.")
        sys.exit(1)
    
    case_id = args[0]
    item_ids = args[1:-2]  # Exclude the last two arguments (handler and organization)
    handler = args[-2]
    organization = args[-1]
    
    # Call the add function with provided arguments
    add(case_id, item_ids, handler, organization)
