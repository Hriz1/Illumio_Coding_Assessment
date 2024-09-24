# Here Importing the CSV module for this program

import csv

# Function to load the lookup table from a CSV file

def load_lookup_table(lookup_file):
    lookup = {}
    # Open the CSV file and read it using a dictionary reader
    with open(lookup_file, mode='r') as file:
        reader = csv.DictReader(file)
        # For each row, create a key using dstport and protocol, and stores the tag as the value
        for row in reader:
            key = (row['dstport'], row['protocol'].lower())  # Converting protocol to lowercase due to case insensitive
            lookup[key] = row['tag']
    return lookup

# Function to process flow logs and count tags and port/protocol combinations
def process_flow_logs(flow_log_file, lookup_table):
    tag_count = {}
    port_protocol_count = {}
    
    # Open the flow log file and read it using a CSV reader
    with open(flow_log_file, mode='r') as file:
        reader = csv.reader(file, delimiter=' ')
        for row in reader:
            # Skipping the empty rows or rows with only spaces
            if not row or len(row) == 1 and row[0] == '':
                continue

            # Skipping the rows that don't have enough columns (malformed rows)
            if len(row) < 6:
                print(f"Skipping malformed row: {row}")
                continue

            # Extracting the dstport and protocol from the rows
            dstport = row[5]
            # Identifying the type of protocols based on its number as per the IANA(https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) (TCP=6, UDP=17) 
            protocol = 'tcp' if row[6] == '6' else 'udp' if row[6] == '17' else 'icmp'
            key = (dstport, protocol)
            
            # Find the corresponding tag in the lookup table, or use 'Untagged' if not found
            tag = lookup_table.get(key, 'Untagged')
            
            # Update the count for this tag
            tag_count[tag] = tag_count.get(tag, 0) + 1
            
            # Update the count for the port/protocol combination
            port_protocol_count[key] = port_protocol_count.get(key, 0) + 1

    return tag_count, port_protocol_count

# Function to write the results to output CSV files
def write_output(tag_count, port_protocol_count):
    # Write tag counts to 'tag_counts.csv'
    with open('tag_counts.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Tag', 'Count'])
        for tag, count in tag_count.items():
            writer.writerow([tag, count])
    
    # Write port/protocol combination counts to 'port_protocol_counts.csv'
    with open('port_protocol_counts.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Port', 'Protocol', 'Count'])
        for (port, protocol), count in port_protocol_count.items():
            writer.writerow([port, protocol, count])

# Main function to run the entire program
def main():
    # Load the lookup table from the CSV file
    lookup_table = load_lookup_table('lookup_table.csv')
    # Process the flow logs and get the tag and port/protocol counts
    tag_count, port_protocol_count = process_flow_logs('flow_log.txt', lookup_table)
    # Write the results to CSV files
    write_output(tag_count, port_protocol_count)

# Calling the main function
if __name__ == '__main__':
    main()