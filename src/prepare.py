from pathlib import Path
import pandas as pd

# имена папок, содержащие изображения мячей для гольфа и парашютов,
# сопоставлены с метками "golf ball" и "parachute"
FOLDERS_TO_LABELS = {
    "food": "food",
    "non_food": "non_food"
    }

def get_files_and_labels(source_path):
    """Принимает путь, указывающий на папку `data/raw/`.
    Функция перебирает все папки и подпапки, чтобы найти файлы
    с расширением jpeg. Метки присваиваются тем файлам, папки
    которых представлены в виде ключей в FOLDERS_TO_LABELS.
    Имена файлов и метки возвращаются в виде списков."""
    images = []
    labels = []
    for image_path in source_path.rglob("*/*.JPG"):
        filename = image_path.absolute()
        folder = image_path.parent.name
        if folder in FOLDERS_TO_LABELS:
            images.append(filename)
            label = FOLDERS_TO_LABELS[folder]
            labels.append(label)
    return images, labels

def save_as_csv(filenames, labels, destination):
    """Принимает список файлов, список меток и путь назначения.
    Имена файлов и метки форматируются как датафрейм pandas
    и сохраняются в виде csv-файла."""
    data_dictionary = {"filename": filenames, "label": labels}
    data_frame = pd.DataFrame(data_dictionary)
    data_frame.to_csv(destination)

def main(repo_path):
    """Запускает get_files_and_labels(), чтобы найти
    все изображения в папках data/raw/train/ и data/raw/val/.
    Имена файлов и соответствующие им метки сохраняются
    как два csv-файла в папке data/prepare/: train.csv
    и test.csv."""
    data_path = repo_path / "raw"
    train_path = data_path / "training"
    test_path = data_path / "validation"
    train_files, train_labels = get_files_and_labels(train_path)
    test_files, test_labels = get_files_and_labels(test_path)
    prepared = repo_path / "FoodvsNon-Food/data/prepared"
    save_as_csv(train_files, train_labels, prepared / "train.csv")
    save_as_csv(test_files, test_labels, prepared / "test.csv")

if __name__ == "__main__":
    repo_path = Path(__file__).parent.parent
    # print(repo_path / '2')
    main(repo_path)