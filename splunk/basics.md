# Fields in Search Results

### Field Extraction 
    - field extractor utility: can be used to extract fields from your data that were not automatically extracted
    - commands : 
        | erex : dont need regex, need sample data
        | rex : need regex, dont need sample data, when possible --> use rex

### Enriching data with knowledge objects
    | eval : can be used for written a temporary field or replace an existing field's value
    Field Extractions -> field aliases -> calculated fields -> lookups --> event types --> tags
