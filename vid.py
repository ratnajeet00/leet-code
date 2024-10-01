import win32evtlog

# Function to read Windows Event Log
def read_event_log(log_type='Security', event_id=4663):
    server = 'localhost'  # Name of the target computer to get logs from
    log_type = log_type
    events = []
    
    try:
        log_handle = win32evtlog.OpenEventLog(server, log_type)
        total_events = win32evtlog.GetNumberOfEventLogRecords(log_handle)
        events = []
        
        for i in range(total_events):
            event = win32evtlog.ReadEventLog(log_handle, win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ, 0)
            for e in event:
                if e.EventID & 0xFFFF == event_id:  # Check for specific event ID
                    event_data = e.StringInserts
                    events.append(event_data)
    except Exception as e:
        print(f"Error reading event log: {e}")
    
    return events

# Example usage
def check_file_access(file_path):
    events = read_event_log()
    for event in events:
        if event and file_path in event:
            print(f"File '{file_path}' accessed by application. Event details: {event}")

# Check the file access
file_path = r'C:\Users\ratna\Downloads\Double_iSmart_2024_Hindi_Dubbed_Full_Movie_480p_Web-Dl.mp4'
check_file_access(file_path)
