##############################
# This is a config file for local side software.
# Note to use raw string for regex pattern and oracle library directory.
##############################

# Interval between database upload. Default is 5min
# Unit: min
interval = 5

logfile_dir = r"C:\Users\harry\Documents\Radio_atten\ignore"


# Note to use raw string here.
regex_pattern = r"(?:InterfacRx.+)(-\d{2})(?:\sdBm\s{3})(\d{2}:\d{2}:\d{2}\s\d{2}-\d{2}-\d{4})(?:\n.+\s)(-\d{2})"

oracle = {
    "lib_dir" : r"C:/XXXX/XXXX/instantclient_21_7",
    "user" : "You know who I am",
    "password" : "Obviously I can not tell you",
    "dsn" : "db_name"
}

