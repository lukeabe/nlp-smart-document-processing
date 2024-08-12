def load_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
