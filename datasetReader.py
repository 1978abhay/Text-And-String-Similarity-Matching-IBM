import pandas as pd


def getStory(dataset_path: str, num: int) -> str:
    if dataset_path.endswith("json"):
        df = pd.read_json(dataset_path)
    elif dataset_path.endswith("csv"):
        df = pd.read_csv(dataset_path)
    else:
        raise ValueError("This func only works on csv and json files")

    for column in ["content", "description", "short_description", "raw_content"]:
        if column in df:
            return df[column][num]


if __name__ == "__main__":
    file = "output//clean_bbc_news_list_uk.json"
    print(getStory(file, 50))
