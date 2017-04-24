# SRT to TXT converter

This tool consolidates .srt files to a single .txt file. Each section is identified by the file's name.

## Usage

```
python converter.py -p <path_to_srt_dir> -d <destination_path> -n <destination_file_name>
```
* -p specifies the path to the directory that contains the .str files to be consolidated
* -d specifies the path where the consolidated .txt file will be created
* -n defines the name of the consolidated file. Set to consolidated_text.txt by default