import json
import pandas as pd


class FewShotPosts:  # few-shot posts manage karne ke liye class
    def __init__(self, file_path="data/processed_posts.json"):  # constructor me default file path set kar rahe hain
        self.df = None  # dataframe store karne ke liye variable
        self.unique_tags = None  # unique tags store karne ke liye variable
        self.load_posts(file_path)

    # self = current object ko refer karta hai (isse hum class ke variables aur methods access karte hain)
    def load_posts(self, file_path):  # JSON file load karke dataframe banane ke liye function
        with open(file_path, encoding='utf-8') as f:  # file open kar rahe hain
            posts = json.load(f)  # JSON data load kar rahe hain
            self.df = pd.json_normalize(posts)  # JSON ko dataframe me convert kar rahe hain
            self.df["length"] = self.df["line_count"].apply(self.categorize_length)
            all_tags = self.df["tags"].apply(lambda x: x).sum()
            self.unique_tags = set(list(all_tags))


    def categorize_length(self, line_count):
        if line_count < 5:
            return "Short"
        elif 5 <= line_count <= 10:
            return "Medium"
        else:
            return "Long"

    def get_tags(self):
        return self.unique_tags

    def get_filtered_posts(self, length, language, tag):
        df_filtered = self.df[
            (self.df['language'] == language) &
            (self.df['length'] == length) &
            (self.df['tags'].apply(lambda tags: tag in tags))
        ]
        return df_filtered.to_dict(orient='records')  # filtered dataframe return kar rahe hain


if __name__ == '__main__':
    fs = FewShotPosts()
    posts = fs.get_filtered_posts("Short", "English", "Job Search")
    print(posts)