# Log Retrieval Solution

## Solutions Considered

1.  **Naive Sequential Scan:**
    *   **Description:** Reading the log file line by line and checking the timestamp to see if it is from the given date.
    *   **Advantages:** Simple to implement.
    *   **Disadvantages:** Extremely slow for a large 1TB log file.
    *   **Why it was not selected:** Inefficient I/O, would take a lot of time.

2.  **Indexing:**
    *   **Description:** Creating an index of log dates to file offsets, this index would allow for faster lookup of dates.
    *   **Advantages:** Very fast for subsequent queries.
    *   **Disadvantages:** Requires a preprocessing step to build the index.
    *   **Why it was not selected:** Unnecessary overhead for a single query.

3.  **Optimized Sequential Scan with Early Exit:**
    *   **Description:** Reading the log file sequentially until the log date is greater than the target date.
    *   **Advantages:** Avoids reading unnecessary data, relatively easy to implement, no preprocessing overhead.
    *   **Disadvantages:** Might be slower for dates towards the end of the file if log distribution is not uniform.
    *   **Why it was selected:** Efficient single query performance, simple, and fits the constraints.

## Final Solution Summary

The chosen solution is the **Optimized Sequential Scan with Early Exit**. This method provides a good balance between simplicity and performance for a single query. It reads the file linearly but quits reading as soon as it is past the requested date. This optimizes for both time and memory. This approach also takes advantage of the fact that the logs are roughly evenly distributed and are sequential.

## Steps to Run

1.  **Clone the repository**
2.  **Save the `extract_logs.py` file in the `src` directory.**
3.  **Download `test_logs.log` using the provided curl command and put it in the root directory of the project.**
4.  **Run the script from the command line:**
    ```bash
    python src/extract_logs.py <YYYY-MM-DD>
    ```
    Replace `<YYYY-MM-DD>` with the desired date (e.g., `2024-12-01`).

5.  **The output will be in the `output` directory** in a file named `output_<YYYY-MM-DD>.txt`.
