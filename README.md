# Cleaner Script

A Python script for cleaning various temporary and unnecessary files on your Windows PC.

## Features

- Clean specified directories
- Clean browser caches for Google Chrome and Mozilla Firefox
- Clean system logs
- Clean temporary files

## Configuration

The cleaning script can be configured using the `cleaner_config.ini` file.

### Cleaning Settings

In the `[Cleaning]` section of the configuration file, you can specify the following:

- `directories`: Comma-separated list of directories to clean.
- `browser_cache_paths`: Comma-separated list of paths for browser caches.
- `system_logs_path`: Path to system logs.
- `temp_files_path`: Path to temporary files.

### Logging Settings

In the `[Logging]` section, you can control logging settings:

- `enable_logging`: Set to `True` to enable logging.
- `log_file_path`: Specify the path for the log file.

### Advanced Settings

In the `[Advanced]` section, you can find advanced settings:

- `skip_in_use_files`: Set to `True` to skip files that are in use during the cleaning process.

## Usage

1. Configure the cleaning settings in the `cleaner_config.ini` file.
2. Run the script and choose the cleaning options from the menu.

## Example Configuration

```ini
[Cleaning]
directories = C:\Users\YourUsername\Downloads, C:\Path\To\Additional\Folder
browser_cache_paths = C:\Users\YourUsername\AppData\Local\Google\Chrome\User Data\Default\Cache, C:\Users\YourUsername\AppData\Roaming\Mozilla\Firefox\Profiles
system_logs_path = C:\Windows\Logs
temp_files_path = C:\Windows\Temp

[Logging]
enable_logging = True
log_file_path = cleaning_log.txt

[Advanced]
skip_in_use_files = True
