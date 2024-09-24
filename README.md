# Technical Assessment

## Description
This project parses AWS flow log data and maps each row to a tag based on a lookup table. The lookup table is defined in a CSV file, containing `dstport`, `protocol`, and `tag`. The program outputs:

- A count of matches for each tag.
- A count of matches for each port/protocol combination.

## Requirements
- Python 3.x (Tested on Python 3.8+)
- No external libraries are required.

## Assumptions
- The program supports **version 2** of the AWS flow logs.
- The only supported protocols are **TCP**, **UDP**, and **ICMP**.
- The `lookup_table.csv` is case-insensitive for matching protocol.
- Flow logs are in a consistent format as per the AWS documentation.
- The program handles large flow log files (up to 10MB) efficiently.

## Input Files
1. **Flow logs**: 
   - A plain text file (ASCII) containing the flow log data.
  
2. **Lookup table**: 
   - A CSV file containing three columns: `dstport`, `protocol`, and `tag`.

### Sample Lookup Table Format:
```csv
dstport,protocol,tag
25,tcp,sv_P1
443,tcp,sv_P2
993,tcp,email
```
### Sample Flow Log Data:

```

2 123456789012 eni-0a1b2c3d 10.0.1.201 198.51.100.2 443 49153 6 25 20000 1620140761 1620140821 ACCEPT OK

```

### Output Files
  - tag_counts.csv: Contains the count of matches for each tag.

    `Format: Tag, Count`

  - port_protocol_counts.csv: Contains the count of matches for each port/protocol combination.

    `Format: Port, Protocol, Count`

# How to Run the Program

  - Clone this repository to your local machine using:
    ```
    https://github.com/Hriz1/Illumio_Coding_Assessment.git
    ```

  - Ensure that you have both the flow log file `flow_logs.txt` and the lookup table file `lookup_table.csv` in the project directory.

### Run the Python script:
  - python `main.py`
  -  The output files `tag_counts.csv` and `port_protocol_counts.csv` will be generated in the same directory.

## Directory Structure

```
flow_logs.txt              # Input: Flow log data
lookup_table.csv           # Input: Lookup table (port, protocol, tag)
main.py                    # Main Python script
tag_counts.csv             # Output: Tag counts
port_protocol_counts.csv   # Output: Port/protocol counts
README.md                  # Project documentation
```

## Tests

The program has been tested on:
  - Sample flow logs provided in the assessment.
  - Custom lookup tables with multiple tag mappings.
  - Different protocol formats (TCP, UDP, ICMP).
