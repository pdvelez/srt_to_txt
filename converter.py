import os
import argparse


def convert_srt(args):

    dir_path = args.p
    dest_path = args.d
    dest_file_name = args.n

    dir_contents = os.listdir(dir_path)

    consolidated_data = ""
    file_count = 0

    for f in dir_contents:

        if f.endswith(".srt"):
            with open(os.path.join(dir_path, f), 'r') as srt:
                consolidated_data += f + "\n"
                consolidated_data += srt.read() + "\n"
                consolidated_data += "-" * 30 + "\n"

            file_count += 1

    with open(os.path.join(dest_path, dest_file_name), "w") as f:
        f.write(consolidated_data)

    print "Consolidated {} files.".format(file_count)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Converts and consolidates .srt files to .txt")

    parser.add_argument('-p',
                        help="Path to .srt files.",
                        required=True)

    parser.add_argument('-d',
                        help="Destination file path.",
                        required=True)

    parser.add_argument('-n',
                        help="Destination file name.",
                        default="consolidated_text.txt")

    args = parser.parse_args()

    convert_srt(args)
