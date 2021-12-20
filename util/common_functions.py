
def get_file_content(file):
    with open(file, "r") as f:
        content = f.readlines()
    return content