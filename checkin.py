import sys
import datetime

# Function to perform checkin of an evidence item
def checkin(item_id, handler, organization, chain_of_custody):
    # Check if the required parameters are provided
    if not item_id or not handler or not organization:
        print("Error: Insufficient arguments provided.")
        sys.exit(1)
    
    # Check if the item ID exists in the chain of custody
    if item_id not in chain_of_custody:
        print(f"Error: Item ID '{item_id}' does not exist in the chain of custody.")
        sys.exit(1)
    
    # Check if the item is already checked in
    if chain_of_custody[item_id]['status'] == 'CHECKEDIN':
        print("Error: Item is already checked in. Cannot perform another checkin.")
        sys.exit(1)
    
    # Update the chain of custody entry with checkin information
    timestamp = datetime.datetime.utcnow().isoformat()
    chain_of_custody[item_id]['status'] = 'CHECKEDIN'
    chain_of_custody[item_id]['handler'] = handler
    chain_of_custody[item_id]['organization'] = organization
    chain_of_custody[item_id]['timestamp'] = timestamp
    
    # Save the updated chain of custody (This is where you might write to a file or database)
    print(f"Item '{item_id}' successfully checked in.")

# Extracting command line arguments
# Example command line: python checkin.py <item_id> <handler> <organization>
if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 3:
        print("Error: Invalid number of command-line arguments.")
        sys.exit(1)
    
    item_id, handler, organization = args
    
    # Load existing data or create an empty dictionary for the chain of custody
    # This should ideally be replaced with a mechanism to load blockchain data
    chain_of_custody = {}  # Assuming chain_of_custody is a dictionary
    
    # Call the checkin function with provided arguments
    checkin(item_id, handler, organization, chain_of_custody)
